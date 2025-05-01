#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 21:58:17 2025

@author: javiermontanochiriboga
"""


# Seleccion
#########################################################

import os
directorio_actual = os.getcwd()
print("Directorio de trabajo actual:", directorio_actual)

from qgis.core import QgsVectorLayer, QgsProject

# 1. Cargar el shapefile

consejos_path = '/Volumes/Disco J/Mapas/Consejo_Comunitario_Titulado/Consejo_Comunitario_Titulado.shp'
# consejos_layer = iface.addVectorLayer(consejos_path, 'consejos', 'ogr')
consejos_layer = QgsVectorLayer(consejos_path, 'consejos', 'ogr')
# te muestra el archivo de determinada capa


# Verificar carga correcta
if not consejos_layer.isValid():
    print("¡Error al cargar el shapefile!")
else:
    # 2. Seleccionar features por IDs
    ids1 = [54, 50, 268, 201, 257, 248, 237, 70]
    ids = [id - 1 for id in ids1] # Hay que restarle menos 1

    #Se seleccionan los IDs escogidos
    consejos_layer.selectByIds(ids)
    
    # 3. Verificar selección y crear nueva capa
    if consejos_layer.selectedFeatureCount() > 0:
        # Crear capa en memoria
        selection_layer = QgsVectorLayer(
            f"{consejos_layer.geometryType().name}?crs={consejos_layer.crs().authid()}",
            "consejos_seleccionados",
            "memory"
        )
        
        # Copiar estructura
        provider = selection_layer.dataProvider()
        provider.addAttributes(consejos_layer.fields())
        selection_layer.updateFields()
        
        # Copiar features
        provider.addFeatures(consejos_layer.selectedFeatures())
        
        # Añadir al proyecto
        QgsProject.instance().addMapLayer(selection_layer)
        print(f"¡Capa creada con {consejos_layer.selectedFeatureCount()} features!")
        
        # Opcional: Zoom a la selección
        iface.mapCanvas().zoomToSelected(selection_layer)
    else:
        print("No se seleccionaron features")


import processing

output_path = '/Volumes/Disco J/Mapas/Consejo_Comunitario_Titulado/Consejo_seleccionados.shp'

processing.run("native:saveselectedfeatures", {
    'INPUT': consejos_layer,
    'OUTPUT': output_path
})

# Verificar creación
if os.path.exists(output_path):
    print("Archivo creado exitosamente!")
    
    


# Cortar
##########################################################

# Cortar Consejos

consejos_path = '/Volumes/Disco J/Mapas/Consejo_Comunitario_Titulado/Consejo_seleccionados.shp'

#conlayer = iface.addVectorLayer(consejos_path, 'consejos', 'ogr')

conlayer = QgsVectorLayer(consejos_path, 'consejos', 'ogr') #asi no se muestra en la pantalla


ecosistemas_path = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Ecositemas/corregidos.gpkg'

namee = 'Ecosistemas'

# Cargar la capa
#ecolayer = QgsVectorLayer(f"{ecosistemas_path}|layername={namee}", namee, "ogr")

ecolayer = QgsVectorLayer(ecosistemas_path, namee, "ogr")



# 3. Configurar parámetros para el clip
params = {
        'INPUT': ecolayer,    # Capa a cortar (ecosistemas)
        'OVERLAY': conlayer,  # Capa de corte (consejos)
        'OUTPUT': 'memory:'   # Salida en memoria
    }



# Ejecutar el algoritmo
result = processing.run("native:clip", params)

# Añadir resultado al proyecto
clipped_layer = result['OUTPUT']
QgsProject.instance().addMapLayer(clipped_layer)

#como hacer que cada poligono se corte en una capa diferente


#############################

from qgis.core import QgsVectorLayer, QgsProject, QgsVectorFileWriter
import processing
import os

# Configurar rutas
consejos_path = '/Volumes/Disco J/Mapas/Consejo_Comunitario_Titulado/Consejo_seleccionados.shp'
ecosistemas_path = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Ecositemas/corregidos.gpkg'

# Cargar capas
conlayer = QgsVectorLayer(consejos_path, 'consejos', 'ogr')
ecolayer = QgsVectorLayer(ecosistemas_path, 'Ecosistemas', 'ogr')

# Verificar carga
if not conlayer.isValid() or not ecolayer.isValid():
    print("Error al cargar capas")
else:
    # Crear directorio de salida
    output_dir = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Ecositemas/Ecosistemas_por_Consejo/'
    os.makedirs(output_dir, exist_ok=True)
    
    # Procesar cada consejo individualmente
    for consejo in conlayer.getFeatures():
        # Crear capa temporal con solo este consejo
        temp_consejo = QgsVectorLayer("Polygon?crs=" + conlayer.crs().authid(), "temp_consejo", "memory")
        with edit(temp_consejo):
            temp_consejo.dataProvider().addAttributes(conlayer.fields())
            temp_consejo.updateFields()
            temp_consejo.dataProvider().addFeature(consejo)
        
        # Ejecutar clip
        params = {
            'INPUT': ecolayer,
            'OVERLAY': temp_consejo,
            'OUTPUT': 'memory:'
        }
        result = processing.run("native:clip", params)
        
        if result['OUTPUT'] and result['OUTPUT'].featureCount() > 0:
            # Nombre del archivo usando atributos del consejo
            nombre_archivo = f"Ecosistemas_{consejo['NOMBRE'].replace(' ', '_')}.gpkg"
            output_path = os.path.join(output_dir, nombre_archivo)
            
            # Guardar resultado en GeoPackage
            options = QgsVectorFileWriter.SaveVectorOptions()
            options.driverName = "GPKG"
            options.fileEncoding = "UTF-8"
            
            error = QgsVectorFileWriter.writeAsVectorFormatV2(
                result['OUTPUT'],
                output_path,
                QgsCoordinateTransformContext(),
                options
            )
            
            if error[0] == QgsVectorFileWriter.NoError:
                print(f"Creado: {nombre_archivo}")
                
                # Opcional: Cargar al proyecto
                capa_resultado = QgsVectorLayer(output_path, f"Ecosistemas_{consejo['NOMBRE']}", "ogr")
                QgsProject.instance().addMapLayer(capa_resultado)
            else:
                print(f"Error guardando {nombre_archivo}: {error[1]}")

    print("Proceso completado. Capas guardadas en:", output_dir)




# Cortar Coberturas
##########################################################

# Cortar Consejos

consejos_path = '/Volumes/Disco J/Mapas/Consejo_Comunitario_Titulado/Consejo_seleccionados.shp'

#conlayer = iface.addVectorLayer(consejos_path, 'consejos', 'ogr')

conlayer = QgsVectorLayer(consejos_path, 'consejos', 'ogr') #asi no se muestra en la pantalla


coberturas_path = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Coberturas Vegetales/Corregidas Coberturas.gpkg'

namec = 'Coberturas'

# Cargar la capa
#coverlayer = QgsVectorLayer(f"{coberturas_path}|layername={namec}", namec, "ogr")

coverlayer = QgsVectorLayer(coberturas_path, namec, "ogr")



# 3. Configurar parámetros para el clip
params = {
        'INPUT': coverlayer,    # Capa a cortar (coberturas)
        'OVERLAY': conlayer,  # Capa de corte (consejos)
        'OUTPUT': 'memory:'   # Salida en memoria
    }



# Ejecutar el algoritmo
result = processing.run("native:clip", params)

# Añadir resultado al proyecto
clipped_layer = result['OUTPUT']
QgsProject.instance().addMapLayer(clipped_layer)

#como hacer que cada poligono se corte en una capa diferente


#############################

from qgis.core import QgsVectorLayer, QgsProject, QgsVectorFileWriter
import processing
import os

# Configurar rutas
consejos_path = '/Volumes/Disco J/Mapas/Consejo_Comunitario_Titulado/Consejo_seleccionados.shp'
coberturas_path = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Coberturas Vegetales/Corregidas Coberturas.gpkg'

# Cargar capas
conlayer = QgsVectorLayer(consejos_path, 'consejos', 'ogr')
coverlayer = QgsVectorLayer(coberturas_path, 'Coberturas', 'ogr')

# Verificar carga
if not conlayer.isValid() or not coverlayer.isValid():
    print("Error al cargar capas")
else:
    # Crear directorio de salida
    output_dir = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Coberturas Vegetales/Coberturas_por_Consejo/'
    os.makedirs(output_dir, exist_ok=True)
    
    # Procesar cada consejo individualmente
    for consejo in conlayer.getFeatures():
        # Crear capa temporal con solo este consejo
        temp_consejo = QgsVectorLayer("Polygon?crs=" + conlayer.crs().authid(), "temp_consejo", "memory")
        with edit(temp_consejo):
            temp_consejo.dataProvider().addAttributes(conlayer.fields())
            temp_consejo.updateFields()
            temp_consejo.dataProvider().addFeature(consejo)
        
        # Ejecutar clip
        params = {
            'INPUT': coverlayer,
            'OVERLAY': temp_consejo,
            'OUTPUT': 'memory:'
        }
        result = processing.run("native:clip", params)
        
        if result['OUTPUT'] and result['OUTPUT'].featureCount() > 0:
            # Nombre del archivo usando atributos del consejo
            nombre_archivo = f"Coberturas_{consejo['NOMBRE'].replace(' ', '_')}.gpkg"
            output_path = os.path.join(output_dir, nombre_archivo)
            
            # Guardar resultado en GeoPackage
            options = QgsVectorFileWriter.SaveVectorOptions()
            options.driverName = "GPKG"
            options.fileEncoding = "UTF-8"
            
            error = QgsVectorFileWriter.writeAsVectorFormatV2(
                result['OUTPUT'],
                output_path,
                QgsCoordinateTransformContext(),
                options
            )
            
            if error[0] == QgsVectorFileWriter.NoError:
                print(f"Creado: {nombre_archivo}")
                
                # Opcional: Cargar al proyecto
                capa_resultado = QgsVectorLayer(output_path, f"Coberturas_{consejo['NOMBRE']}", "ogr")
                QgsProject.instance().addMapLayer(capa_resultado)
            else:
                print(f"Error guardando {nombre_archivo}: {error[1]}")

    print("Proceso completado. Capas guardadas en:", output_dir)



















