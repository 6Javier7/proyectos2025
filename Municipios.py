#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 21:56:29 2025

@author: javiermontanochiriboga
"""

# Selecionar
##################################################

municipios_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Municipios/Municipios2/MGN_MPIO_POLITICO.shp'
#munlayer = iface.addVectorLayer(municipios_path, 'municipios', 'ogr')
munlayer = QgsVectorLayer(municipios_path, 'municipios', 'ogr') #asi no se muestra en la pantalla



#para ver la info de cada municipio
#for f in munlayer.getFeatures():
#  print('%s, %s' % (f['MPIO_CNMBR'], f['MPIO_CDPMP']))


codigos = [
    76109,  # Buenaventura
    19809,  # Timbiquí
    19318,  # Guapí
    52621,  # Roberto Payán
    27075,  # Bahía Solano
    19418,  # López de Micay
    20550,  # Pelaya
    27361,  # Istmina
    23672,  # San Antero
    23580,  # Puerto Libertador
    23686,  # San Pelayo
    44378,  # Hatonuevo
    52835,  # Tumaco
    73168,  # Chaparral
    70429,  # Majagual
    18001   # Florencia (Caquetá)
]




codigos1 = [id - 1 for id in ids1] # Hay que restarle menos 1


# Seleccionar por campo de código ("MPIO_CDPMP")
expresion = '"MPIO_CDPMP" IN ({})'.format(','.join([f"'{c}'" for c in codigos]))
munlayer.selectByExpression(expresion)

 # 3. Verificar selección y crear nueva capa
if munlayer.selectedFeatureCount() > 0:
        # Crear capa en memoria
        selection_layer = QgsVectorLayer(
            f"{munlayer.geometryType().name}?crs={munlayer.crs().authid()}",
            "municipios_seleccionados",
            "memory"
        )
        
        # Copiar estructura
        provider = selection_layer.dataProvider()
        provider.addAttributes(munlayer.fields())
        selection_layer.updateFields()
        
        # Copiar features
        provider.addFeatures(munlayer.selectedFeatures())
        
        # Añadir al proyecto
        QgsProject.instance().addMapLayer(selection_layer)
        print(f"¡Capa creada con {munlayer.selectedFeatureCount()} features!")
        
        # Opcional: Zoom a la selección
        iface.mapCanvas().zoomToSelected(selection_layer)
else:
        print("No se seleccionaron features")


#for field in comlayer.fields():
#    print(field)
#    print(field.name())
#    print(field.type())


#for f in comlayer.getFeatures():
#    print(f)

#for f in comlayer.getFeatures():
#  print('%s, %s, %s' % (f['NOMBRE'], f['TIPO_ACTO_'], f['NUMERO_ACT']))


import processing

output_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Municipios/Municipios2/municipios_seleccionadosp.shp'

processing.run("native:saveselectedfeatures", {
    'INPUT': munlayer,
    'OUTPUT': output_path
})

# Verificar creación
if os.path.exists(output_path):
    print("Archivo creado exitosamente!")



#for f in comlayer.getFeatures():
#  print('%s, %s, %s, %s' % (f['NOMBRE'], f['TIPO_ACTO_'], f['NUMERO_ACT'], f['OBJECTID']))

#for f in comlayer.getFeatures():
#  print('%s, %s, %s, %s' % (f['OBJECTID'], f['NOMBRE'], f['TIPO_ACTO_'], f['NUMERO_ACT']))


########################
# Amazonas


municipios_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Municipios/Municipios2/MGN_MPIO_POLITICO.shp'
#munlayer = iface.addVectorLayer(municipios_path, 'municipios', 'ogr')
munlayer = QgsVectorLayer(municipios_path, 'municipios', 'ogr') #asi no se muestra en la pantalla


codigos2 = [
    '52693',
    '52678',
    '52083',
    '52203',
    '05051',
    '05107',
    '05120',
    '05154',
    '05250',
    '05495',
    '05790',
    '05854',
    '05895',
    '05134',
    '27787',
    '27615',
    '27600',
    '27425',
    '27150',
    '27099',
    '19533',
    '19290',
    '18029',
    '18094',
    '18410',
    '18479',
    '18610',
    '18860',
    '18150',
    '18460',
    '18753'
]


# Seleccionar por campo de código ("MPIO_CDPMP")
expresion1 = '"MPIO_CDPMP" IN ({})'.format(','.join([f"'{c}'" for c in codigos2]))
munlayer.selectByExpression(expresion1)
print(expresion1)

 # 3. Verificar selección y crear nueva capa
if munlayer.selectedFeatureCount() > 0:
        # Crear capa en memoria
        selection_layer = QgsVectorLayer(
            f"{munlayer.geometryType().name}?crs={munlayer.crs().authid()}",
            "municipios_seleccionados2",
            "memory"
        )
        
        # Copiar estructura
        provider = selection_layer.dataProvider()
        provider.addAttributes(munlayer.fields())
        selection_layer.updateFields()
        
        # Copiar features
        provider.addFeatures(munlayer.selectedFeatures())
        
        # Añadir al proyecto
        QgsProject.instance().addMapLayer(selection_layer)
        print(f"¡Capa creada con {munlayer.selectedFeatureCount()} features!")
        
        # Opcional: Zoom a la selección
        iface.mapCanvas().zoomToSelected(selection_layer)
else:
        print("No se seleccionaron features")


import processing

output_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Municipios/Municipios2/municipios_seleccionadosp2.shp'

processing.run("native:saveselectedfeatures", {
    'INPUT': munlayer,
    'OUTPUT': output_path
})

# Verificar creación
if os.path.exists(output_path):
    print("Archivo creado exitosamente!")


# Cortar
###############################################################

#Cortar Ecosistemas
municipios_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Municipios/Municipios2/municipios_seleccionadosp.shp'

#munlayer = iface.addVectorLayer(municipios_path, 'municipios', 'ogr')
munlayer = QgsVectorLayer(municipios_path, 'municipios', 'ogr') #asi no se muestra en la pantalla


ecosistemas_path = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Ecositemas/corregidos.gpkg'

namee = 'Ecosistemas'

# Cargar la capa
#ecolayer = QgsVectorLayer(f"{ecosistemas_path}|layername={namee}", namee, "ogr")

ecolayer = QgsVectorLayer(ecosistemas_path, namee, "ogr")



# 3. Configurar parámetros para el clip
params = {
        'INPUT': ecolayer,    # Capa a cortar (ecosistemas)
        'OVERLAY': munlayer,  # Capa de corte (consejos)
        'OUTPUT': 'memory:'   # Salida en memoria
    }



# Ejecutar el algoritmo
result = processing.run("native:clip", params)

# Añadir resultado al proyecto
clipped_layer = result['OUTPUT']
QgsProject.instance().addMapLayer(clipped_layer)

#como hacer que cada poligono se corte en una capa diferente


#########################
#por municipio opcional

municipios_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Municipios/Municipios2/municipios_seleccionadosp.shp'

#munlayer = iface.addVectorLayer(municipios_path, 'municipios', 'ogr')
munlayer = QgsVectorLayer(municipios_path, 'municipios', 'ogr') #asi no se muestra en la pantalla


ecosistemas_path = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Ecositemas/corregidos.gpkg'

namee = 'Ecosistemas'

# Cargar la capa
#ecolayer = QgsVectorLayer(f"{ecosistemas_path}|layername={namee}", namee, "ogr")

ecolayer = QgsVectorLayer(ecosistemas_path, namee, "ogr")


# Versión más rápida usando selección por atributo
output_dir = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Ecositemas/Ecosistemas_por_Municipio/'
os.makedirs(output_dir, exist_ok=True)

for municipio in munlayer.getFeatures():
    # Seleccionar el municipio actual
    munlayer.selectByIds([municipio.id()])
    
    # Ejecutar clip directamente con selección
    params = {
        'INPUT': ecolayer,
        'OVERLAY': munlayer,
        'OUTPUT': 'memory:',
        'OVERLAY_FIELDS_PREFIX': ''  # Evitar prefijos en campos
    }
    
    result = processing.run("native:clip", params)
    
    if result['OUTPUT'] and result['OUTPUT'].featureCount() > 0:
        # Crear nombre seguro para archivo
        nombre = f"{municipio['MPIO_CDPMP']}_{municipio['MPIO_CNMBR']}"
        nombre = ''.join(c if c.isalnum() else '_' for c in nombre)
        output_path = os.path.join(output_dir, f"{nombre}.shp")
        
        # Guardar como Shapefile
        QgsVectorFileWriter.writeAsVectorFormat(
            result['OUTPUT'],
            output_path,
            'UTF-8',
            ecolayer.crs(),
            'ESRI Shapefile'
        )

        # Opcional: Cargar al proyecto
        capa_resultado = QgsVectorLayer(output_path, nombre, 'ogr')
        QgsProject.instance().addMapLayer(capa_resultado)

munlayer.removeSelection()





