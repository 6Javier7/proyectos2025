#Corregir geometrias

coberturas_path1 = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Coberturas Vegetales/Cobertura_de_la_tierra_100K_Periodo_2020_limite_administrativo/Shape limite Ambiental/e_cobertura_tierra_2020_amb.shp'
coberturas_path1a = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Coberturas Vegetales/Cobertura_de_la_tierra_100K_Periodo_2020_limite_administrativo/shape Limite admin/e_cobertura_tierra_2020_admin.shp'
ecosistemas_path1 = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Ecositemas/Mapa_Ecosistemas_Continentales_Costeros_Marinos_100K_2024/SHAPE/e_eccmc_100K_2024.shp'

output_path = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Coberturas Vegetales/Corregidas Coberturas1.gpkg'

# Cargar la capa
coverlayer1 = QgsVectorLayer(coberturas_path1, 'Coberturas20', "ogr")

processing.run("native:fixgeometries", {
    'INPUT': coverlayer1,
    'OUTPUT': output_path
})


output_path = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Ecositemas/corregidos1.gpkg'

# Cargar la capa
ecolayer1 = QgsVectorLayer(ecosistemas_path1, 'Coberturas20', "ogr")

processing.run("native:fixgeometries", {
    'INPUT': ecolayer1,
    'OUTPUT': output_path
})


coberturasB_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Mundo/Brasil/vege_area/vege_area.shp'
output_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Mundo/Brasil/vege_area/vege_area.gpkg'

# Cargar la capa
coverblayer = QgsVectorLayer(coberturasB_path, 'Coberturas20', "ogr")

processing.run("native:fixgeometries", {
    'INPUT': coverblayer,
    'OUTPUT': output_path
})
