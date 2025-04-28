#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 13:11:57 2025

@author: javiermontanochiriboga
"""


import os
directorio_actual = os.getcwd()
print("Directorio de trabajo actual:", directorio_actual)


municipios_path = 'Users/javiermontanochiriboga/Documents/Javier/Zona de Influencia/mpio/mpio.shp'
# munlayer = iface.addVectorLayer(municipios_path, 'municipios', 'ogr')
munlayer = QgsVectorLayer(municipios_path, 'municipios', 'ogr') #asi no se muestra en la pantalla

consejos_path = 'Users/javiermontanochiriboga/Documents/Javier/Zona de Influencia/Consejos_Comunitarios/COMUNIDAD_NEGRA_TITULADA.shp'
# comlayer = iface.addVectorLayer(consejos_path, 'consejos', 'ogr')
comlayer = QgsVectorLayer(consejos_path, 'consejos', 'ogr')
# te muestra el archivo de determinada capa

for field in comlayer.fields():
    print(field)
    print(field.name())
    print(field.type())

for f in comlayer.getFeatures():
    print(f)

for f in comlayer.getFeatures():
  print('%s, %s, %s' % (f['NOMBRE'], f['TIPO_ACTO_'], f['NUMERO_ACT']))
        
for f in comlayer.getFeatures():
  print('%s, %s, %s, %s' % (f['NOMBRE'], f['TIPO_ACTO_'], f['NUMERO_ACT'], f['OBJECTID']))

for f in comlayer.getFeatures():
  print('%s, %s, %s, %s' % (f['OBJECTID'], f['NOMBRE'], f['TIPO_ACTO_'], f['NUMERO_ACT']))



for f in comlayer.getFeatures():
  geom = f.geometry()
  print('%s, %s, %f, %f' % (f['NOMBRE'], f['CODIGO_DAN'],
         geom.asPoint().y(), geom.asPoint().x()))

