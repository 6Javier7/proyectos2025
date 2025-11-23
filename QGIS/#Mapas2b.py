#Mapas2b

recu_path = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Recuperacion/Recuperacion Corregidos.gpkg'
reha_path = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Rehabilitacion/Rehabilitacion corregido.gpkg'
resta_path = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Restauracion/Corregidos Restauracion.gpkg'


#Rehabilitacion
################

# Cargar la capa
rehalayer = QgsVectorLayer(reha_path, 'reha', "ogr")

# Desactivar renderizado durante el proceso
QgsSettings().setValue('/qgis/enable_render', False)

try:
    # Procesamiento rápido sin refrescos de pantalla
    result_reha = processing.run("native:clip", {
        'INPUT': rehalayer,
        'OVERLAY': selection_layer,
        'OUTPUT': 'memory:'
    })
    
    clipped_reha = result_reha['OUTPUT']
    clipped_reha.setName("reha")
    
    # Aplicar símbolo UNA sola vez
    symbolreha = QgsFillSymbol.createSimple({
        'color': '255, 36, 0',
        'color_border': '178, 34, 34',
        'width_border': '0.3'
    })
    
    # CORRECCIÓN: Usar rendererreha en lugar de rendererrecu
    rendererreha = QgsSingleSymbolRenderer(symbolreha)
    clipped_reha.setRenderer(rendererreha)
    
finally:
    # Reactivar renderizado
    QgsSettings().setValue('/qgis/enable_render', True)

# Solo UN refresco al final - ESTA LÍNEA SOLA
QgsProject.instance().addMapLayer(clipped_reha)



#Recuperacion
################

# Cargar la capa
reculayer = QgsVectorLayer(recu_path, 'recu', "ogr")

# Desactivar renderizado durante el proceso
QgsSettings().setValue('/qgis/enable_render', False)

try:
    # Procesamiento rápido sin refrescos de pantalla
    result_recu = processing.run("native:clip", {
        'INPUT': reculayer,
        'OVERLAY': selection_layer,
        'OUTPUT': 'memory:'
    })
    
    clipped_recu = result_recu['OUTPUT']
    clipped_recu.setName("recu")
    
    # Aplicar símbolo UNA sola vez
    symbolrecu = QgsFillSymbol.createSimple({
        'color': '255, 117, 24',  # '25, 100, 180' azul
        'color_border': '249, 77, 0',  # Color del borde
        'width_border': '0.3'  # Grosor del borde en mm
})
    
    # CORRECCIÓN: Usar rendererrecu en lugar de rendererrecu
    rendererrecu = QgsSingleSymbolRenderer(symbolrecu)
    clipped_recu.setRenderer(rendererrecu)
    
finally:
    # Reactivar renderizado
    QgsSettings().setValue('/qgis/enable_render', True)

# Solo UN refresco al final - ESTA LÍNEA SOLA
QgsProject.instance().addMapLayer(clipped_recu)


#Restauracion
################

# Cargar la capa
restalayer = QgsVectorLayer(resta_path, 'resta', "ogr")

# Desactivar renderizado durante el proceso
QgsSettings().setValue('/qgis/enable_render', False)

try:
    # Procesamiento rápido sin refrescos de pantalla
    result_resta = processing.run("native:clip", {
        'INPUT': restalayer,
        'OVERLAY': selection_layer,
        'OUTPUT': 'memory:'
    })
    
    clipped_resta = result_resta['OUTPUT']
    clipped_resta.setName("resta")
    
    # Aplicar símbolo UNA sola vez
    symbolresta = QgsFillSymbol.createSimple({
        'color': '228, 208, 10',  # '25, 100, 180' azul
        'color_border': '218, 165, 32',  # Color del borde
        'width_border': '0.3'  # Grosor del borde en mm
})
    
    # CORRECCIÓN: Usar rendererresta en lugar de rendererresta
    rendererresta = QgsSingleSymbolRenderer(symbolresta)
    clipped_resta.setRenderer(rendererresta)
    
finally:
    # Reactivar renderizado
    QgsSettings().setValue('/qgis/enable_render', True)

# Solo UN refresco al final - ESTA LÍNEA SOLA
QgsProject.instance().addMapLayer(clipped_resta)

