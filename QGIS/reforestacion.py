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



