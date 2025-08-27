#Mapa3colores

#https://html-color.codes/olive

region = 'Latin America & Caribbean'
subregion = 'South America'
cpais = ['MEX']
codigos_uf = ['14'] #Jalisco 14
codigos_muni = ['14120'] #Zapopan 14120



# Lista de nombres de capas a procesar
nombres_capas = ['OpenStreetMap', 'oceano', 'regiones_seleccionados', 'pais', 'estados', 'estados_seleccionados', 'MunicipiosEsp2', 'muni_seleccionados', 'Municipios']
oceano_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Mundo/ne_10m_ocean/ne_10m_ocean.shp'
region_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Mundo/ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp'
pais_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Mundo/ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp'
UF_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Mundo/Mexico/Shapefile - Estados/u_territorial_estados_mgn_inegi_2013.shp'
municipios_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Mundo/Mexico/Shapefile - Municipios/inegi_refmunicip_2010.shp'

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

# 1a. Cargar la capa de Brasil (Pais)
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


# 1a. Cargar la capa de Estados federales
#############################################
uflayer = iface.addVectorLayer(UF_path, 'estados', 'ogr')

if uflayer:
    # Crear un símbolo simple
    symbol = QgsFillSymbol.createSimple({
        'color': '230, 230, 230',  # Gris Claro
        'color_border': '180, 180, 180',  
        'width_border': '0.2'  # Grosor del borde en mm
    })

    uflayer.setOpacity(0.9)
    
    # Aplicar el símbolo a la capa
    uflayer.renderer().setSymbol(symbol)
    
    # Refrescar la capa para ver los cambios
    uflayer.triggerRepaint()
    iface.layerTreeView().refreshLayerSymbology(uflayer.id())

# Verificar carga correcta
if not uflayer.isValid():
    print("¡Error al cargar el shapefile!")
else:
# El else estaba vacío y mal indentado, así que lo eliminé


# 2. Seleccionar estado
#########################################################
    codigos_est = codigos_uf
    
    # Construir expresión de selección
    

    expression = "cvegeoedo IN ({})".format(','.join(["'{}'".format(c) for c in codigos_est]))

    uflayer.selectByExpression(expression)
    
    # 3. Verificar selección y crear nueva capa
    if uflayer.selectedFeatureCount() > 0:
        # Crear capa temporal
        selection_layer = QgsVectorLayer(
            "Polygon?crs={}".format(uflayer.crs().authid()),
            "estados_seleccionados",
            "memory"
        )

        # Copiar estructura de campos
        provider = selection_layer.dataProvider()
        provider.addAttributes(uflayer.fields())
        selection_layer.updateFields()
        
        # Copiar features seleccionadas
        features = uflayer.selectedFeatures()
        provider.addFeatures(features)
        selection_layer.updateExtents()
        
        # Añadir al proyecto
        QgsProject.instance().addMapLayer(selection_layer)
        print(f"¡Se seleccionaron {len(features)} estado(s)!")

        # Estilo diferenciado para selección
        highlight_symbol = QgsFillSymbol.createSimple({
            'color': '220, 208, 255',  # Vinotinto
            'outline_color': '75, 0, 130',  # Indigo
            'outline_width': '0.5'
        })
        selection_layer.renderer().setSymbol(highlight_symbol)
        selection_layer.setOpacity(0.9)


        # Zoom a la selección
        iface.mapCanvas().zoomToSelected(uflayer)
        iface.mapCanvas().refresh()

        uflayer.removeSelection()  # Elimina la selección actual

    else:
        print("No se encontraron Estados con los códigos especificados")
        print("Nombres de campos disponibles:", [field.name() for field in uflayer.fields()])


# 1b. Cargar la capa de intermedios seleccionados
# 1b. Cargar la capa de municipios seleccionados
####################################################################
munilayer = QgsVectorLayer(municipios_path, 'municipios', 'ogr')


# Verificar carga correcta
if not munilayer.isValid():
    print("¡Error al cargar el shapefile!")
else:
    
    # Construir expresión de selección
    expression = "cve_ent IN ({})".format(','.join(["'{}'".format(c) for c in codigos_est]))
    munilayer.selectByExpression(expression)
    
    # Verificar selección y crear nueva capa
    if munilayer.selectedFeatureCount() > 0:
        # Crear capa temporal
        selection_layer = QgsVectorLayer(
            "Polygon?crs={}".format(munilayer.crs().authid()),
            "Municipios",
            "memory"
        )

        # Copiar estructura de campos
        provider = selection_layer.dataProvider()
        provider.addAttributes(munilayer.fields())
        selection_layer.updateFields()
        
        # Copiar features seleccionadas
        features = munilayer.selectedFeatures()
        provider.addFeatures(features)
        selection_layer.updateExtents()
        selection_layer.setOpacity(0.9)
        
        # Añadir al proyecto
        QgsProject.instance().addMapLayer(selection_layer)
        print(f"¡Se seleccionaron {len(features)} municipio(s) de los estados especificados!")

        # Aplicar estilo a la capa recién creada
        symbol = QgsFillSymbol.createSimple({
            'color': '220, 208, 255',  # Vinotinto
            'outline_color': '75, 0, 130',  # Indigo
            'outline_width': '0.5'
        })
        selection_layer.renderer().setSymbol(symbol)
        selection_layer.triggerRepaint()
        munilayer.setOpacity(0.9)

        # Zoom a la selección
        iface.mapCanvas().setExtent(selection_layer.extent())
        iface.mapCanvas().refresh()
    else:
        print("No se encontraron inmediatos con los códigos de estados especificados")
        print("Nombres de campos disponibles:", [field.name() for field in munilayer.fields()])




# Verificar carga correcta
if not munilayer.isValid():
    print("¡Error al cargar el shapefile!")
else:
    # 2. Seleccionar features por código DANE
    
    
    # Construir expresión de selección
    expression = "cve_umun IN ({})".format(','.join(["'{}'".format(c) for c in codigos_muni]))

    munilayer.selectByExpression(expression)
    
    # 3. Verificar selección y crear nueva capa
    if munilayer.selectedFeatureCount() > 0:
        # Crear capa temporal
        selection_layer = QgsVectorLayer(
            "Polygon?crs={}".format(munilayer.crs().authid()),
            "muni_seleccionados",
            "memory"
        )
    
        # Copiar estructura de campos
        provider = selection_layer.dataProvider()
        provider.addAttributes(munilayer.fields())
        selection_layer.updateFields()
        
        # Copiar features seleccionadas
        features = munilayer.selectedFeatures()
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
        iface.mapCanvas().zoomToSelected(munilayer)
        iface.mapCanvas().refresh()
    else:
        print("No se encontraron municipios con los códigos especificados")
        print("Nombres de campos disponibles:", [field.name() for field in munilayer.fields()])