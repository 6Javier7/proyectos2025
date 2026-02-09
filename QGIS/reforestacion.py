#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 02:26:06 2025

@author: javiermontanochiriboga
"""

# Cortar restauracion
##########################################################

# Cortar Consejos

consejos_path = '/Volumes/Disco J/Mapas/Consejo_Comunitario_Titulado/Consejo_seleccionados.shp'

#conlayer = iface.addVectorLayer(consejos_path, 'consejos', 'ogr')

conlayer = QgsVectorLayer(consejos_path, 'consejos', 'ogr') #asi no se muestra en la pantalla


restauracion_path = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Restauracion/Corregidos Restauracion.gpkg'

namer = 'restauracion'

# Cargar la capa
#reslayer = QgsVectorLayer(f"{restauracion_path}|layername={namer}", namer, "ogr")

reslayer = QgsVectorLayer(restauracion_path, namer, "ogr")



# 3. Configurar parámetros para el clip
params = {
        'INPUT': reslayer,    # Capa a cortar (restauracion)
        'OVERLAY': conlayer,  # Capa de corte (consejos)
        'OUTPUT': 'memory:'   # Salida en memoria
    }



# Ejecutar el algoritmo
result = processing.run("native:clip", params)

# Añadir resultado al proyecto
clipped_layer = result['OUTPUT']
QgsProject.instance().addMapLayer(clipped_layer)

#como hacer que cada poligono se corte en una capa diferente
#no hay zonas de restauracion en el consejo seleccionado

# Municipios
###########################################################



# Cargar capas
municipios_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Municipios/Municipios2/municipios_seleccionadosp.shp'
munlayer = QgsVectorLayer(municipios_path, 'municipios', 'ogr')


restauracion_path = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Restauracion/Corregidos Restauracion.gpkg'

namer = 'restauracion'

# Cargar la capa
#reslayer = QgsVectorLayer(f"{restauracion_path}|layername={namer}", namer, "ogr")

reslayer = QgsVectorLayer(restauracion_path, namer, "ogr")



# 3. Configurar parámetros para el clip
params = {
        'INPUT': reslayer,    # Capa a cortar (restauracion)
        'OVERLAY': munlayer,  # Capa de corte (consejos)
        'OUTPUT': 'memory:'   # Salida en memoria
    }



# Ejecutar el algoritmo
result = processing.run("native:clip", params)

# Añadir resultado al proyecto
clipped_layer = result['OUTPUT']
QgsProject.instance().addMapLayer(clipped_layer)

symbolresta = QgsFillSymbol.createSimple({
        'color': '71, 143, 0',  # '25, 100, 180' azul
        'color_border': '103, 146, 103',  # Color del borde
        'width_border': '0.3'  # Grosor del borde en mm
})


# Aplicar el símbolo a la capa
rendererresta = QgsSingleSymbolRenderer(symbolresta)
clipped_resta.setRenderer(rendererresta)

# Refrescar la capa para ver los cambios
clipped_resta.triggerRepaint()


# Recuperacion
###########################

# Cargar capas
municipios_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Municipios/Municipios2/municipios_seleccionadosp.shp'
munlayer = QgsVectorLayer(municipios_path, 'municipios', 'ogr')


recuperacion_path = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Recuperacion/Recuperacion Corregidos.gpkg'

namer = 'recuperacion'

# Cargar la capa
#reslayer = QgsVectorLayer(f"{recuperacion_path}|layername={namer}", namer, "ogr")

reclayer = QgsVectorLayer(recuperacion_path, namer, "ogr")



# 3. Configurar parámetros para el clip
params = {
        'INPUT': reclayer,    # Capa a cortar (recuperacion)
        'OVERLAY': munlayer,  # Capa de corte (consejos)
        'OUTPUT': 'memory:'   # Salida en memoria
    }



# Ejecutar el algoritmo
result = processing.run("native:clip", params)

# Añadir resultado al proyecto
clipped_layer = result['OUTPUT']
QgsProject.instance().addMapLayer(clipped_layer)

symbolrecu = QgsFillSymbol.createSimple({
        'color': '150, 168, 59',  # '25, 100, 180' azul
        'color_border': '122, 148, 46',  # Color del borde
        'width_border': '0.3'  # Grosor del borde en mm
})

# Aplicar el símbolo a la capa
rendererrecu = QgsSingleSymbolRenderer(symbolrecu)
clipped_recu.setRenderer(rendererrecu)

# Refrescar la capa para ver los cambios
clipped_recu.triggerRepaint()

# Rehabilitacion
###########################

# Cargar capas
municipios_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Municipios/Municipios2/municipios_seleccionadosp.shp'
munlayer = QgsVectorLayer(municipios_path, 'municipios', 'ogr')


rehabilitacion_path = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Rehabilitacion/Corregidos Rehabilitacion.gpkg'

namer = 'rehabilitacion'

# Cargar la capa
#reslayer = QgsVectorLayer(f"{rehabilitacion_path}|layername={namer}", namer, "ogr")

reclayer = QgsVectorLayer(rehabilitacion_path, namer, "ogr")



# 3. Configurar parámetros para el clip
params = {
        'INPUT': reclayer,    # Capa a cortar (rehabilitacion)
        'OVERLAY': munlayer,  # Capa de corte (consejos)
        'OUTPUT': 'memory:'   # Salida en memoria
    }



# Ejecutar el algoritmo
result = processing.run("native:clip", params)

# Añadir resultado al proyecto
clipped_layer = result['OUTPUT']
QgsProject.instance().addMapLayer(clipped_layer)

symbolreha = QgsFillSymbol.createSimple({
        'color': '112, 224, 0',  # '25, 100, 180' azul
        'color_border': '100, 140, 17',  # Color del borde
        'width_border': '0.3'  # Grosor del borde en mm
})

# Aplicar el símbolo a la capa
rendererreha = QgsSingleSymbolRenderer(symbolreha)
clipped_reha.setRenderer(rendererrecu)

# Refrescar la capa para ver los cambios
clipped_reha.triggerRepaint()


