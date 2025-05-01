#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 12:03:14 2025

@author: javiermontanochiriboga
"""

import os
from qgis.core import *
from qgis.PyQt.QtGui import QColor

# Zonificacion PDET
###################################################3

# 1. Cargar capas

# Cargar capas
municipios_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Municipios/Municipios2/municipios_seleccionadosp.shp'

munlayer = QgsVectorLayer(municipios_path, 'municipios', 'ogr')

zoni_path = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Zonificacion_PDET_agosto_2021/Zonificacion_PDET_agosto_2021.shp'
zonilayer = QgsVectorLayer(zoni_path, 'Zonificacion PDET', "ogr")

# 3. Configurar parámetros para el clip
params = {
        'INPUT': zonilayer,    # Capa a cortar (coberturas)
        'OVERLAY': munlayer,  # Capa de corte (consejos)
        'OUTPUT': 'memory:'   # Salida en memoria
    }

output_dir = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Zonificacion_PDET_agosto_2021'
nombre_archivo = f"Zonificacion2.gpkg"
output_path = os.path.join(output_dir, nombre_archivo)

# Ejecutar el algoritmo
result = processing.run("native:clip", params)

# Añadir resultado al proyecto
clipped_layer = result['OUTPUT']
QgsProject.instance().addMapLayer(clipped_layer)

options = QgsVectorFileWriter.SaveVectorOptions()
options.driverName = "GPKG"
options.fileEncoding = "UTF-8"

error = QgsVectorFileWriter.writeAsVectorFormatV2(
                result['OUTPUT'],
                output_path,
                QgsCoordinateTransformContext(),
                options
            )


# 3. Guardar resultado
output_dir = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Zonificacion_PDET_agosto_2021'
nombre_archivo = "Zonificacion2.gpkg"
output_path = os.path.join(output_dir, nombre_archivo)

options = QgsVectorFileWriter.SaveVectorOptions()
options.driverName = "GPKG"
options.fileEncoding = "UTF-8"

error = QgsVectorFileWriter.writeAsVectorFormatV2(
    clipped_layer,
    output_path,
    QgsCoordinateTransformContext(),
    options
)

if error[0] == QgsVectorFileWriter.NoError:
    print("Capa guardada exitosamente!")
else:
    print("Error al guardar la capa:", error)

# Colores
######################################


# Función para aplicar estilo a una sola capa
def aplicar_estilo_capa(capa, campo_categoria, colores_por_valor, borde_color='0,0,0', grosor_borde=0.3):
    """
    Aplica simbología categorizada a una sola capa de polígonos
    
    Parámetros:
    - capa: Capa vectorial (QgsVectorLayer)
    - campo_categoria: Nombre del campo para categorizar
    - colores_por_valor: Diccionario {valor: (R,G,B)} con los colores
    - borde_color: Color del borde en formato 'R,G,B' (opcional)
    - grosor_borde: Grosor del borde en mm (opcional)
    """
    if not capa.isValid():
        print("Error: Capa no válida")
        return False
    
    if capa.geometryType() != QgsWkbTypes.PolygonGeometry:
        print("Error: La capa no es de polígonos")
        return False
    
    if campo_categoria not in [field.name() for field in capa.fields()]:
        print(f"Error: Campo '{campo_categoria}' no encontrado")
        return False
    
    # Crear categorías
    categories = []
    for valor, color_rgb in colores_por_valor.items():
        # Crear símbolo de relleno
        symbol = QgsFillSymbol.createSimple({
            'color': f'{color_rgb[0]},{color_rgb[1]},{color_rgb[2]}',
            'color_border': borde_color,
            'width_border': str(grosor_borde)
        })
        
        # Crear categoría
        category = QgsRendererCategory(valor, symbol, str(valor))
        categories.append(category)
    
    # Aplicar renderizador
    renderer = QgsCategorizedSymbolRenderer(campo_categoria, categories)
    capa.setRenderer(renderer)
    capa.triggerRepaint()
    
    # Actualizar la vista
    iface.layerTreeView().refreshLayerSymbology(capa.id())
    iface.mapCanvas().refresh()
    
    print(f"Estilo aplicado a la capa: {capa.name()}")
    return True

# Diccionario de colores (asegúrate de que las comas estén correctas)
coloresz = {
    'Preservación': (97, 194, 0),
    'Restauración': (94, 221, 193),
    'Uso sostenible para el aprovechamiento de la biodiversidad': (243, 156, 18),
    'Uso sostenible para el desarrollo': (248, 196, 113),
    'Protección por Alta Oferta de SSEE': (212, 23, 255),
    'Protección con uso sostenible': (158, 255, 200),
    'Uso productivo con protección': (150, 168, 59),
    'Uso productivo con reconversión': (255, 255, 95),
    'Uso productivo': (166, 66, 46)
}

# Cargar la capa (si no está ya cargada)
zoni_path = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Zonificacion_PDET_agosto_2021/Zonificacion2.gpkg'
zonilayer = QgsVectorLayer(zoni_path, 'Zonificacion PDET', "ogr")

if not zonilayer.isValid():
    print("Error al cargar la capa de zonificación")
else:
    # Añadir al proyecto si no está ya
    if not QgsProject.instance().mapLayersByName(zonilayer.name()):
        QgsProject.instance().addMapLayer(zonilayer)
    
    # Aplicar el estilo
    aplicar_estilo_capa(
        capa=zonilayer,
        campo_categoria='categoria',  # Cambia por el nombre real de tu campo
        colores_por_valor=coloresz,
        borde_color='0,0,0',
        grosor_borde=0.3
    )






















