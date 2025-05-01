#Mapa2colores

#https://html-color.codes/olive

region = 'Latin America & Caribbean'
subregion = 'South America'
codigos_dep = ['76']
codigomdep = ['76']
codigos_muni = ['76109']
cpais = ['COL']
codigoc = ['50']

# Lista de nombres de capas a procesar
nombres_capas = ['OpenStreetMap', 'oceano', 'regiones_seleccionados', 'paises_seleccionados', 'departamentos', 'departamentos_seleccionados', 'MunicipiosDep2', 'municipios_seleccionados', 'Consejos2', 'veredas_en_consejos']
oceano_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Mundo/ne_10m_ocean/ne_10m_ocean.shp'
region_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Mundo/ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp'
pais_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Mundo/ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp'
departamentos_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Colombia Dane/ADMINISTRATIVO/MGN_DPTO_POLITICO.shp'
municipios_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Municipios/Municipios2/MGN_MPIO_POLITICO.shp'
consejos_path = '/Volumes/Disco J/Mapas/Consejo_Comunitario_Titulado/Consejo_Comunitario_Titulado.shp'
#veredas_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Veredas/CRVeredas_2020.shp'

# Lista de nombres de capas a procesar pc Andrey
#nombres_capas = ['OpenStreetMap', 'oceano', 'regiones_seleccionados', 'paises_seleccionados', 'departamentos', 'departamentos_seleccionados', 'MunicipiosDep2', 'municipios_seleccionados', 'Consejos2', 'veredas_en_consejos']

#oceano_path = '/run/user/1000/gvfs/smb-share:server=pc-de-javier.local,share=disco%20j/Mapas/Zonificacion Colombia/Mundo/ne_10m_ocean/ne_10m_ocean.shp'
#region_path = '/run/user/1000/gvfs/smb-share:server=pc-de-javier.local,share=disco%20j/Mapas/Zonificacion Colombia/Mundo/ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp'
#pais_path = '/run/user/1000/gvfs/smb-share:server=pc-de-javier.local,share=disco%20j/Mapas/Zonificacion Colombia/Mundo/ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp'
#departamentos_path = '/run/user/1000/gvfs/smb-share:server=pc-de-javier.local,share=disco%20j/Mapas/Zonificacion Colombia/Colombia Dane/ADMINISTRATIVO/MGN_DPTO_POLITICO.shp'
#municipios_path = '/run/user/1000/gvfs/smb-share:server=pc-de-javier.local,share=disco%20j/Mapas/Zonificacion Colombia/Municipios/Municipios2/MGN_MPIO_POLITICO.shp'
#consejos_path = '/run/user/1000/gvfs/smb-share:server=pc-de-javier.local,share=disco%20j/Mapas/Consejo_Comunitario_Titulado/Consejo_Comunitario_Titulado.shp'
#veredas_path = '/run/user/1000/gvfs/smb-share:server=pc-de-javier.local,share=disco%20j/Mapas/Zonificacion Colombia/Veredas/CRVeredas_2020.shp'


#Limpiar capas existentes
####################################

for nombre_capa in nombres_capas:
    # 1. Verificar si la capa ya existe
    capas_existentes = QgsProject.instance().mapLayersByName(nombre_capa)
    
    # 2. Eliminar todas las instancias (evita duplicados)
    if capas_existentes:
        for capa in capas_existentes:
            QgsProject.instance().removeMapLayer(capa)
        print(f"🗑️ Capa '{nombre_capa}' eliminada.")


# Cargar OpenStreetMap
############################################

osm_layer = QgsRasterLayer(
    'type=xyz&url=https://tile.openstreetmap.org/{z}/{x}/{y}.png&zmax=19&zmin=0',
    'OpenStreetMap',
    'wms'
)

if osm_layer.isValid():
    QgsProject.instance().addMapLayer(osm_layer)
else:
    print("Error al cargar OpenStreetMap")


# 1a. Cargar la capa de Oceano
##################################################
# Método correcto para cargar una capa vectorial
olayer = QgsVectorLayer(oceano_path, 'oceano', 'ogr')

# Verificar si la capa se cargó correctamente
if olayer.isValid():
    # Crear un símbolo simple para el océano (azul claro)
    symbol = QgsFillSymbol.createSimple({
        'color': '147, 204, 234',  # '25, 100, 180' azul
        'color_border': '176, 208, 248',  # Color del borde
        'width_border': '0.3'  # Grosor del borde en mm
    })
    
    olayer.setOpacity(0.9)

    # Aplicar el símbolo a la capa
    olayer.renderer().setSymbol(symbol)
    
    # Añadir la capa al proyecto si no está ya añadida
    if not QgsProject.instance().mapLayersByName('oceano'):
        QgsProject.instance().addMapLayer(olayer)
    
    # Refrescar la visualización
    olayer.triggerRepaint()
    iface.layerTreeView().refreshLayerSymbology(olayer.id())
    
    print("Capa de océano cargada y estilizada correctamente")
else:
    print("¡Error al cargar la capa de océano!")


# 1a. Cargar la capa de Abya Yala(regiones)
##################################################

relayer = QgsVectorLayer(region_path, 'region', 'ogr')

# Verificar carga correcta
if not relayer.isValid():
    print("¡Error al cargar el shapefile!")
else:
    # Construir expresión de selección (usando el campo REGION_WB)
    expression = f"REGION_WB = '{region}'"  # Buscar coincidencia exacta
        
    relayer.selectByExpression(expression)
    
    # Verificar selección y crear nueva capa
    if relayer.selectedFeatureCount() > 0:
        # Crear capa temporal
        selection_layer = QgsVectorLayer(
            "Polygon?crs={}".format(relayer.crs().authid()),
            "regiones_seleccionados",
            "memory"
        )

        # Copiar estructura de campos
        provider = selection_layer.dataProvider()
        provider.addAttributes(relayer.fields())
        selection_layer.updateFields()
        
        # Copiar features seleccionadas
        features = relayer.selectedFeatures()
        provider.addFeatures(features)
        selection_layer.updateExtents()
        
        # Añadir al proyecto
        QgsProject.instance().addMapLayer(selection_layer)
        print(f"¡Se seleccionaron {len(features)} país(es)!")
        
        # Aplicar estilo
        symbol = QgsFillSymbol.createSimple({
            'color': '250, 250, 250',  # Blanco hueso
            'color_border': '200, 200, 200',  # Gris
            'width_border': '0.3'
        })
        selection_layer.renderer().setSymbol(symbol)
        selection_layer.triggerRepaint()
        selection_layer.setOpacity(0.9)

        # Zoom a la selección
        iface.mapCanvas().setExtent(selection_layer.extent())
        iface.mapCanvas().refresh()

# 1a. Cargar la capa de Colombia (Pais)
#####################################################
palayer = QgsVectorLayer(pais_path, 'pais', 'ogr')



# Verificar carga correcta
if not palayer.isValid():
    print("¡Error al cargar el shapefile!")
else:
    # 2. Seleccionar features por código DANE
    codigos_pais = cpais
    
    # Construir expresión de selección
    

    expression = "SOV_A3 IN ({})".format(','.join(["'{}'".format(c) for c in codigos_pais]))

    palayer.selectByExpression(expression)
    
    # 3. Verificar selección y crear nueva capa
    if palayer.selectedFeatureCount() > 0:
        # Crear capa temporal
        selection_layer = QgsVectorLayer(
            "Polygon?crs={}".format(palayer.crs().authid()),
            "paises_seleccionados",
            "memory"
        )

        # Copiar estructura de campos
        provider = selection_layer.dataProvider()
        provider.addAttributes(palayer.fields())
        selection_layer.updateFields()
        
        # Copiar features seleccionadas
        features = palayer.selectedFeatures()
        provider.addFeatures(features)
        selection_layer.updateExtents()
        
        # Añadir al proyecto
        QgsProject.instance().addMapLayer(selection_layer)
        print(f"¡Se seleccionaron {len(features)} departamento(s)!")
        
        # Aplicar estilo a la capa recién creada
        symbol = QgsFillSymbol.createSimple({
            'color': '230, 230, 230',  # Gris Claro
            'color_border': '180, 180, 180',  # 
            'width_border': '0.1'     # Grosor del borde
        })
        selection_layer.renderer().setSymbol(symbol)
        selection_layer.triggerRepaint()
        selection_layer.setOpacity(0.9)

        # Zoom a la selección
        iface.mapCanvas().zoomToSelected(palayer)
        iface.mapCanvas().refresh()
    else:
        print("No se encontraron Paises con los códigos especificados")
        print("Nombres de campos disponibles:", [field.name() for field in palayer.fields()])


# 1a. Cargar la capa de Colombia con departamentos
#############################################
deplayer = iface.addVectorLayer(departamentos_path, 'departamentos', 'ogr')


if deplayer:
    # Crear un símbolo simple
    symbol = QgsFillSymbol.createSimple({
        'color': '230, 230, 230',  # Gris Claro
        'color_border': '180, 180, 180',  
        'width_border': '0.2'  # Grosor del borde en mm
    })

    deplayer.setOpacity(0.9)
    
    # Aplicar el símbolo a la capa
    deplayer.renderer().setSymbol(symbol)
    
    # Refrescar la capa para ver los cambios
    deplayer.triggerRepaint()
    iface.layerTreeView().refreshLayerSymbology(deplayer.id())

# Verificar carga correcta
if not deplayer.isValid():
    print("¡Error al cargar el shapefile!")
else:

# 2. Seleccionar departamento
#########################################################
    codigos_dane = codigos_dep
    
    # Construir expresión de selección
    

    expression = "DPTO_CCDGO IN ({})".format(','.join(["'{}'".format(c) for c in codigos_dane]))

    deplayer.selectByExpression(expression)
    
    # 3. Verificar selección y crear nueva capa
    if deplayer.selectedFeatureCount() > 0:
        # Crear capa temporal
        selection_layer = QgsVectorLayer(
            "Polygon?crs={}".format(deplayer.crs().authid()),
            "departamentos_seleccionados",
            "memory"
        )

        # Copiar estructura de campos
        provider = selection_layer.dataProvider()
        provider.addAttributes(deplayer.fields())
        selection_layer.updateFields()
        
        # Copiar features seleccionadas
        features = deplayer.selectedFeatures()
        provider.addFeatures(features)
        selection_layer.updateExtents()
        
        # Añadir al proyecto
        QgsProject.instance().addMapLayer(selection_layer)
        print(f"¡Se seleccionaron {len(features)} departamento(s)!")

        # Estilo diferenciado para selección
        highlight_symbol = QgsFillSymbol.createSimple({
            'color': '220, 208, 255',  # Vinotinto
            'outline_color': '75, 0, 130',  # Indigo
            'outline_width': '0.5'
        })
        selection_layer.renderer().setSymbol(highlight_symbol)
        selection_layer.setOpacity(0.9)


        # Zoom a la selección
        iface.mapCanvas().zoomToSelected(deplayer)
        iface.mapCanvas().refresh()

        deplayer.removeSelection()  # Elimina la selección actual

    else:
        print("No se encontraron Departamentos con los códigos especificados")
        print("Nombres de campos disponibles:", [field.name() for field in deplayer.fields()])



# 1b. Cargar la capa de municipios seleccionados
####################################################################
munlayer = QgsVectorLayer(municipios_path, 'municipios', 'ogr')


# Verificar carga correcta
if not munlayer.isValid():
    print("¡Error al cargar el shapefile!")
else:
    # Definir códigos de departamento
    codigos_dep = codigomdep  # Reemplaza con tus códigos reales
    
    # Construir expresión de selección
    expression = "DPTO_CCDGO IN ({})".format(','.join(["'{}'".format(c) for c in codigos_dep]))
    munlayer.selectByExpression(expression)
    
    # Verificar selección y crear nueva capa
    if munlayer.selectedFeatureCount() > 0:
        # Crear capa temporal
        selection_layer = QgsVectorLayer(
            "Polygon?crs={}".format(munlayer.crs().authid()),
            "MunicipiosDep2",
            "memory"
        )

        # Copiar estructura de campos
        provider = selection_layer.dataProvider()
        provider.addAttributes(munlayer.fields())
        selection_layer.updateFields()
        
        # Copiar features seleccionadas
        features = munlayer.selectedFeatures()
        provider.addFeatures(features)
        selection_layer.updateExtents()
        selection_layer.setOpacity(0.9)
        
        # Añadir al proyecto
        QgsProject.instance().addMapLayer(selection_layer)
        print(f"¡Se seleccionaron {len(features)} municipio(s) de los departamentos especificados!")

        # Aplicar estilo a la capa recién creada
        symbol = QgsFillSymbol.createSimple({
            'color': '220, 208, 255',  # Vinotinto
            'color_border': '75, 0, 130',  # Indigo
            'width_border': '0.3'     # Grosor del borde
        })
        selection_layer.renderer().setSymbol(symbol)
        selection_layer.triggerRepaint()
        munlayer.setOpacity(0.9)

        # Zoom a la selección
        iface.mapCanvas().setExtent(selection_layer.extent())
        iface.mapCanvas().refresh()
    else:
        print("No se encontraron municipios con los códigos de departamento especificados")
        print("Nombres de campos disponibles:", [field.name() for field in munlayer.fields()])




# Verificar carga correcta
if not munlayer.isValid():
    print("¡Error al cargar el shapefile!")
else:
    # 2. Seleccionar features por código DANE
    codigos_dane = codigos_muni
    
    # Construir expresión de selección
    expression = "MPIO_CDPMP IN ({})".format(','.join(["'{}'".format(c) for c in codigos_dane]))

    munlayer.selectByExpression(expression)
    
    # 3. Verificar selección y crear nueva capa
    if munlayer.selectedFeatureCount() > 0:
        # Crear capa temporal
        selection_layer = QgsVectorLayer(
            "Polygon?crs={}".format(munlayer.crs().authid()),
            "municipios_seleccionados",
            "memory"
        )
    
        # Copiar estructura de campos
        provider = selection_layer.dataProvider()
        provider.addAttributes(munlayer.fields())
        selection_layer.updateFields()
        
        # Copiar features seleccionadas
        features = munlayer.selectedFeatures()
        provider.addFeatures(features)
        selection_layer.updateExtents()
        selection_layer.setOpacity(0.9)
        
        # Añadir al proyecto
        QgsProject.instance().addMapLayer(selection_layer)
        print(f"¡Se seleccionaron {len(features)} municipio(s)!")

        # Aplicar estilo a la capa recién creada
        symbol = QgsFillSymbol.createSimple({
            'color': '154, 185, 115',  # Oliva
            'color_border': '0, 100, 0',  # Dark green
            'width_border': '0.5'     # Grosor del borde
        })
        selection_layer.renderer().setSymbol(symbol)
        selection_layer.triggerRepaint()
        
        selection_layer.setOpacity(0.9)

        # Zoom a la selección
        iface.mapCanvas().zoomToSelected(munlayer)
        iface.mapCanvas().refresh()
    else:
        print("No se encontraron municipios con los códigos especificados")
        print("Nombres de campos disponibles:", [field.name() for field in munlayer.fields()])


# 1b. Cargar la capa de consejos
####################################################################

conlayer = QgsVectorLayer(consejos_path, 'consejos', 'ogr')



# Verificar carga correcta
if not conlayer.isValid():
    print("¡Error al cargar el shapefile!")
else:
    # Definir códigos de departamento
    codigos_con = codigoc  # Reemplaza con tus códigos reales
    
    # Construir expresión de selección
    expression = "OBJECTID IN ({})".format(','.join(["'{}'".format(c) for c in codigos_con]))
    conlayer.selectByExpression(expression)
    
    # Verificar selección y crear nueva capa
    if conlayer.selectedFeatureCount() > 0:
        # Crear capa temporal
        selection_layer = QgsVectorLayer(
            "Polygon?crs={}".format(conlayer.crs().authid()),
            "Consejos2",
            "memory"
        )

        # Copiar estructura de campos
        provider = selection_layer.dataProvider()
        provider.addAttributes(conlayer.fields())
        selection_layer.updateFields()
        
        # Copiar features seleccionadas
        features = conlayer.selectedFeatures()
        provider.addFeatures(features)
        selection_layer.updateExtents()
        selection_layer.setOpacity(0.9)
        
        # Añadir al proyecto
        QgsProject.instance().addMapLayer(selection_layer)
        print(f"¡Se seleccionaron {len(features)} municipio(s) de los departamentos especificados!")

        # Aplicar estilo a la capa recién creada
        symbol = QgsFillSymbol.createSimple({
            'color': '255, 204, 51',  # Sunglow
            'color_border': '218, 165, 32',  # Indigo
            'width_border': '0.5'     # Grosor del borde
        })
        selection_layer.renderer().setSymbol(symbol)
        selection_layer.triggerRepaint()
        conlayer.setOpacity(0.9)

        # Zoom a la selección
        iface.mapCanvas().setExtent(selection_layer.extent())
        iface.mapCanvas().refresh()
    else:
        print("No se encontraron municipios con los códigos de departamento especificados")
        print("Nombres de campos disponibles:", [field.name() for field in conlayer.fields()])




# Verificar carga correcta
if not conlayer.isValid():
    print("¡Error al cargar el shapefile!")
else:
    # 2. Seleccionar features por código DANE
    codigos_dane = codigos_muni
    
    # Construir expresión de selección
    expression = "MPIO_CDPMP IN ({})".format(','.join(["'{}'".format(c) for c in codigos_dane]))

    conlayer.selectByExpression(expression)
    
    # 3. Verificar selección y crear nueva capa
    if conlayer.selectedFeatureCount() > 0:
        # Crear capa temporal
        selection_layer = QgsVectorLayer(
            "Polygon?crs={}".format(conlayer.crs().authid()),
            "consejos_seleccionados",
            "memory"
        )
    
        # Copiar estructura de campos
        provider = selection_layer.dataProvider()
        provider.addAttributes(conlayer.fields())
        selection_layer.updateFields()
        
        # Copiar features seleccionadas
        features = conlayer.selectedFeatures()
        provider.addFeatures(features)
        selection_layer.updateExtents()
        selection_layer.setOpacity(0.9)
        
        # Añadir al proyecto
        QgsProject.instance().addMapLayer(selection_layer)
        print(f"¡Se seleccionaron {len(features)} municipio(s)!")

        # Aplicar estilo a la capa recién creada
        symbol = QgsFillSymbol.createSimple({
            'color': '154, 185, 115',  # Oliva
            'color_border': '0, 100, 0',  # Dark green
            'width_border': '0.4'     # Grosor del borde
        })
        selection_layer.renderer().setSymbol(symbol)
        selection_layer.triggerRepaint()
        
        selection_layer.setOpacity(0.9)

        # Zoom a la selección
        iface.mapCanvas().zoomToSelected(conlayer)
        iface.mapCanvas().refresh()
    else:
        print("No se encontraron municipios con los códigos especificados")
        print("Nombres de campos disponibles:", [field.name() for field in conlayer.fields()])

 # 2. Cargar capa de veredas
#        vlayer = QgsVectorLayer(veredas_path, 'veredas', 'ogr')
        
#        if not vlayer.isValid():
#            print("¡Error al cargar las veredas!")
#        else:
#            # Crear índice espacial de los consejos seleccionados
#            index = QgsSpatialIndex(selection_layer.getFeatures())
#            
#            # Encontrar veredas que intersectan
#            features_seleccionados = []
#            for vereda in vlayer.getFeatures():
#                if index.intersects(vereda.geometry().boundingBox()):
#                    for consejo in selection_layer.getFeatures():
#                        if vereda.geometry().intersects(consejo.geometry()):
#                            features_seleccionados.append(vereda)
#                            break
#            
#            # Crear capa de resultados
#            if features_seleccionados:
#                result_layer = QgsVectorLayer(
#                    "Polygon?crs={}".format(vlayer.crs().authid()),
#                    "veredas_en_consejos",
#                    "memory"
#                )
                
#                provider = result_layer.dataProvider()
#                provider.addAttributes(vlayer.fields())
#                result_layer.updateFields()
#                provider.addFeatures(features_seleccionados)
#                
#                # Estilo para veredas
#                vereda_symbol = QgsFillSymbol.createSimple({
#                    'color': '70, 130, 180, 100',  # Azul acero transparente
#                    'outline_color': '0, 0, 139',
#                    'outline_width': '0.3'
#                })
#                result_layer.renderer().setSymbol(vereda_symbol)
#                
#                QgsProject.instance().addMapLayer(result_layer)
                
                # Zoom a la extensión combinada
#                extent = result_layer.extent()
#                extent.combineExtentWith(selection_layer.extent())
#                iface.mapCanvas().setExtent(extent)
#                iface.mapCanvas().refresh()
#                
#                print(f"✅ {len(features_seleccionados)} veredas intersectan con los consejos seleccionados")
#            else:
#                print("⚠️ No hay intersecciones entre veredas y consejos")
#
####################################################

#localidades_path = '/Volumes/Disco A/Compartido/Fami/Javier/Nico/localidades.csv'

## Crear la URI del CSV (ajusta estos parámetros)
#uri = (
#    f"file://{localidades_path}?encoding=UTF-8"
#    f"&delimiter=,"
#    f"&xField=Longitud"  # Columna con coordenadas X
#    f"&yField=Latitud"   # Columna con coordenadas Y
#    f"&crs=EPSG:4326"    # Sistema de referencia (WGS84 en este caso)
#)
#
## Crear la capa vectorial
#csv_layer = iface.addVectorLayer(uri, "Samples", "delimitedtext")

# 1. Cargar el archivo CSV como capa de puntos
#localidades_path = '/Volumes/Disco A/Compartido/Fami/Javier/Nico/localidades.csv'
#uri = (
#    f"file://{localidades_path}?encoding=UTF-8"
#    f"&delimiter=,"
#    f"&xField=Longitud"  # Asegúrate que estos nombres coincidan con tus columnas
#    f"&yField=Latitud"
#    f"&crs=EPSG:4326"
#)

#csv_layer = QgsVectorLayer(uri, "localidades", "delimitedtext")
#if not csv_layer.isValid():
#    print("Error al cargar el CSV!")
#else:
#    QgsProject.instance().addMapLayer(csv_layer, False)

# 2. Cargar la capa de veredas
#veredas_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Veredas/CRVeredas_2020.shp'
#vlayer = QgsVectorLayer(veredas_path, 'veredas', 'ogr')
#if not vlayer.isValid():
#    print("Error al cargar las veredas!")
#else:
#    QgsProject.instance().addMapLayer(vlayer, False)

# Esperar un momento para que las capas se carguen
#import time
#time.sleep(2)

# 3. Verificar que las capas están cargadas
#vlayer = QgsProject.instance().mapLayersByName('veredas')[0]
#csv_layer = QgsProject.instance().mapLayersByName('localidades')[0]

# 4. Crear índice espacial para los puntos
#index = QgsSpatialIndex(csv_layer.getFeatures())

# 5. Seleccionar veredas que intersectan con puntos
#features_seleccionados = []
#for poligono in vlayer.getFeatures():
#    geom_poligono = poligono.geometry()
#    # Primero verificar por bounding box para eficiencia
#    ids_puntos = index.intersects(geom_poligono.boundingBox())
#    if ids_puntos:
#        # Luego verificar intersección exacta
#        for id_punto in ids_puntos:
#            punto = csv_layer.getFeature(id_punto)
#            if geom_poligono.intersects(punto.geometry()):
#                features_seleccionados.append(poligono)
#                break
#

# 6. Crear capa temporal con las veredas seleccionadas
#if features_seleccionados:
#    capa_temporal = QgsVectorLayer("Polygon?crs={}".format(vlayer.crs().authid()), 
#                                 "veredas_con_localidades", 
#                                 "memory")
#    
#    provider = capa_temporal.dataProvider()
#    provider.addAttributes(vlayer.fields())
#    capa_temporal.updateFields()
#    
#    provider.addFeatures(features_seleccionados)
#    
#    QgsProject.instance().addMapLayer(capa_temporal)
#    iface.mapCanvas().setExtent(capa_temporal.extent())
#    iface.mapCanvas().refresh()
    
#    print(f"Se creó capa temporal con {len(features_seleccionados)} veredas que contienen localidades")
#else:
#    print("No se encontraron veredas que intersecten con los puntos")


#Colores
##########################

#Amarillo
#d5b43c

#Verdes
#        # Aplicar estilo a la capa recién creada
#        symbol = QgsFillSymbol.createSimple({
#            'color': '107, 142, 35',  # Oliva
#            'color_border': '0, 100, 0',  # Dark green
#            'width_border': '0.5'     # Grosor del borde
#        })
#        selection_layer.renderer().setSymbol(symbol)

#    # Crear un símbolo simple
#    symbol = QgsFillSymbol.createSimple({
#        'color': '173, 216, 230',  # Azul claro
#        'color_border': '70, 130, 180',  # Azul acero
#        'width_border': '0.2'  # Grosor del borde en mm
#    })
#    
#    # Aplicar el símbolo a la capa
#    deplayer.renderer().setSymbol(symbol)

# Aplicar estilo a la capa recién creada
#        symbol = QgsFillSymbol.createSimple({
#            'color': '255, 165, 0',  # Dark ORange
#            'color_border': '205, 133, 63',  # Peru
#            'width_border': '0.5'     # Grosor del borde
#        })


