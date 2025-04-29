#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 13:11:57 2025

@author: javiermontanochiriboga
"""


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

