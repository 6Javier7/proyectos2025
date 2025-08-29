#Mapa3colores

#Floresta Ombrófila Densa das Terras Baixas


#Plantilla

#Escala pais
#187837313

#Escala estados
#60082899

#Escala municipios
#6773082

#REGIÕES FITOECOLÓGICAS
#Classificação da Vegetação

#https://html-color.codes/olive

region = 'Latin America & Caribbean'
subregion = 'South America'
codigos_uf = ['26']
codigos_inter = ['2601']
codigomdep = ['26']
codigos_inme = ['260001'] #['260001', '260002']
codigos_muni = ['2607604'] #['2607604', '2607752', '2606200', '2605459']

# Lista de nombres de capas a procesar
nombres_capas = ['OpenStreetMap', 'oceano', 'regiones_seleccionados', 'pais', 'estados', 'intermedios', 'estados_seleccionados', 'MunicipiosEsp2', 'inter_seleccionados', 'InmeEsp2', 'muni_seleccionados', 'inmed_seleccionados', 'Municipios', 'Coberturasf', 'Coberturasl', 'coberturasl2', 'Mata Atlântica']
oceano_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Mundo/ne_10m_ocean/ne_10m_ocean.shp'
region_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Mundo/ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp'
pais_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Mundo/Brasil/BR_Pais_2024/BR_Pais_2024.shp'
UF_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Mundo/Brasil/BR_UF_2024/BR_UF_2024.shp'
inter_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Mundo/Brasil/BR_RG_Intermediarias_2024/BR_RG_Intermediarias_2024.shp'
inme_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Mundo/Brasil/BR_RG_Imediatas_2024/BR_RG_Imediatas_2024.shp'
municipios_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Mundo/Brasil/BR_Municipios_2024/BR_Municipios_2024.shp'
coberturasB_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Mundo/Brasil/vege_area/vege_area.gpkg'
Bioma_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Mundo/Brasil/biome_border/biome_border.shp'

# Ruta al archivo .qml
qmlf_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Mundo/Brasil/vege_area/simbologia_vege_area/vege_fito.qml'
qmll_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Mundo/Brasil/vege_area/simbologia_vege_area/vege_legenda.qml'
qmll2_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Mundo/Brasil/vege_area/simbologia_vege_area/vege_legenda2.qml'


# Lista de nombres de capas a procesar pc Andrey
#nombres_capas = ['OpenStreetMap', 'oceano', 'regiones_seleccionados', 'paises_seleccionados', 'departamentos', 'departamentos_seleccionados', 'MunicipiosDep2', 'municipios_seleccionados', 'Consejos2', 'veredas_en_consejos']

#oceano_path = '/run/user/1000/gvfs/smb-share:server=pc-de-javier.local,share=disco%20j/Mapas/Zonificacion Colombia/Mundo/ne_10m_ocean/ne_10m_ocean.shp'
#region_path = '/run/user/1000/gvfs/smb-share:server=pc-de-javier.local,share=disco%20j/Mapas/Zonificacion Colombia/Mundo/ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp'
#pais_path = '/run/user/1000/gvfs/smb-share:server=pc-de-javier.local,share=disco%20j/Mapas/Zonificacion Colombia/Mundo/ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp'
#departamentos_path = '/run/user/1000/gvfs/smb-share:server=pc-de-javier.local,share=disco%20j/Mapas/Zonificacion Colombia/Colombia Dane/ADMINISTRATIVO/MGN_DPTO_POLITICO.shp'
#municipios_path = '/run/user/1000/gvfs/smb-share:server=pc-de-javier.local,share=disco%20j/Mapas/Zonificacion Colombia/Municipios/Municipios2/MGN_MPIO_POLITICO.shp'
#consejos_path = '/run/user/1000/gvfs/smb-share:server=pc-de-javier.local,share=disco%20j/Mapas/Consejo_Comunitario_Titulado/Consejo_Comunitario_Titulado.shp'
#veredas_path = '/run/user/1000/gvfs/smb-share:server=pc-de-javier.local,share=disco%20j/Mapas/Zonificacion Colombia/Veredas/CRVeredas_2020.shp'

#def aplicar_estilo_qml_filtrado(capas, qml_path, campo_categorizacion=None):
#    """
#    Aplica estilo QML a múltiples capas, filtrando categorías inexistentes
#    """
#    capas_estilizadas = 0
#    
#    for item in capas:
#        # Obtener capa
#        if isinstance(item, QgsVectorLayer):
#            capa = item
#        elif isinstance(item, str):
#            found = QgsProject.instance().mapLayersByName(item)
#            if not found:
#                continue
#            capa = found[0]
#        else:
#            continue
#        
#        # Aplicar QML
#        if not capa.loadNamedStyle(qml_path):
#            continue
#        
#        # Filtrar categorías si es categorizado
#        renderer = capa.renderer()
#        if isinstance(renderer, QgsCategorizedSymbolRenderer):
#            # Detectar campo si no se especificó
#            if campo_categorizacion is None:
#                campo_categorizacion = renderer.classAttribute()
#            
#            # Filtrar categorías
#            valores_existentes = {str(feat[campo_categorizacion]) for feat in capa.getFeatures() 
#                                if feat[campo_categorizacion] not in [None, '']}
#            
#            nuevas_categorias = [cat for cat in renderer.categories() 
#                               if str(cat.value()) in valores_existentes]
#            
#            if nuevas_categorias:
#                nuevo_renderer = QgsCategorizedSymbolRenderer(campo_categorizacion, nuevas_categorias)
#                nuevo_renderer.setShowAllSymbols(False)
#                capa.setRenderer(nuevo_renderer)
#                capas_estilizadas += 1
#        
#        capa.triggerRepaint()
#    
#    return capas_estilizadas

# Aplicar a la capa cortada

def aplicar_estilo_comun_a_capas(capas, campo=None, colores_por_valor=None, borde_color='0, 0, 0', grosor_borde=0.2, qml_path=None):
    """
    Aplica la misma simbología categorizada a múltiples capas de polígonos.
    Puede aplicar estilos desde QML o crear categorías programáticamente.
    
    Parámetros:
    - capas: Lista de capas vectoriales (QgsVectorLayer) o nombres de capas
    - campo: Nombre del campo común para categorizar (opcional si se usa QML)
    - colores_por_valor: Diccionario {valor: (R,G,B)} con los colores (opcional si se usa QML)
    - borde_color: Color del borde en formato 'R,G,B' (opcional)
    - grosor_borde: Grosor del borde en mm (opcional)
    - qml_path: Ruta al archivo QML para aplicar estilo (opcional)
    
    Retorna:
    - Número de capas a las que se aplicó el estilo correctamente
    """
    capas_estilizadas = 0
    
    # Convertir nombres de capas a objetos de capa si es necesario
    layers_to_style = []
    for item in capas:
        if isinstance(item, QgsVectorLayer):
            layers_to_style.append(item)
        elif isinstance(item, str):
            found_layers = QgsProject.instance().mapLayersByName(item)
            if found_layers:
                layers_to_style.extend(found_layers)
    
    for capa in layers_to_style:
        # Verificar que la capa sea válida y sea de polígonos
        if not capa.isValid():
            print(f"Advertencia: Capa '{capa.name()}' no es válida. Saltando...")
            continue
        
        if capa.geometryType() != QgsWkbTypes.PolygonGeometry:
            print(f"Advertencia: Capa '{capa.name()}' no es de polígonos. Saltando...")
            continue
        
        # OPCIÓN 1: Aplicar estilo desde archivo QML
        if qml_path:
            try:
                # PRIMERO: Cargar el estilo QML
                success = capa.loadNamedStyle(qml_path)
                if not success:
                    print(f"❌ Error al aplicar QML a capa: {capa.name()}")
                    continue
                
                # SEGUNDO: Filtrar categorías para mostrar solo las existentes
                renderer = capa.renderer()
                if renderer and renderer.type() == 'categorizedSymbol':
                    # Obtener valores únicos que existen en la capa cortada
                    valores_existentes = set()
                    campo_renderer = renderer.classAttribute()  # Campo usado en el QML
                    
                    for feature in capa.getFeatures():
                        valor = feature[campo_renderer]
                        if valor is not None and valor != '':
                            valores_existentes.add(valor)
                    
                    print(f"🔍 Valores existentes en {capa.name()}: {valores_existentes}")
                    
                    # SOLUCIÓN PARA DIFERENTES VERSIONES DE QGIS
                    try:
                        # Método para versiones más recientes de QGIS (3.x+)
                        renderer.setShowAllCategories(False)
                    except AttributeError:
                        try:
                            # Método para versiones más antiguas
                            renderer.setShowAllSymbols(False)
                        except AttributeError:
                            # Si ambos métodos fallan, crear un nuevo renderizador filtrado
                            print("⚠️  Creando renderizador filtrado manualmente...")
                            categories = []
                            
                            for cat in renderer.categories():
                                if cat.value() in valores_existentes:
                                    categories.append(cat)
                            
                            # Crear nuevo renderizador con solo categorías existentes
                            new_renderer = QgsCategorizedSymbolRenderer(campo_renderer, categories)
                            capa.setRenderer(new_renderer)
                
                # TERCERO: Forzar actualización
                capa.triggerRepaint()
                iface.layerTreeView().refreshLayerSymbology(capa.id())
                
                capas_estilizadas += 1
                print(f"✅ Estilo QML aplicado y filtrado a capa: {capa.name()}")
                
            except Exception as e:
                print(f"❌ Error cargando QML para {capa.name()}: {str(e)}")
                continue
        
        # OPCIÓN 2: Crear categorías programáticamente (tu código original)
        elif campo and colores_por_valor:
            # Verificar que el campo exista
            if campo not in [field.name() for field in capa.fields()]:
                print(f"Advertencia: Campo '{campo}' no encontrado en capa '{capa.name()}'. Saltando...")
                continue

            # Obtener valores únicos que realmente existen en la capa
            valores_existentes = set()
            for feature in capa.getFeatures():
                valor = feature[campo]
                if valor is not None and valor != '':
                    valores_existentes.add(valor)

            print(f"🔍 Valores existentes en {capa.name()}: {len(valores_existentes)}")
            print(f"🎨 Colores definidos: {len(colores_por_valor)}")

            # Filtrar colores para solo valores existentes
            colores_filtrados = {k: v for k, v in colores_por_valor.items() if k in valores_existentes}
            
            # Crear categorías SOLO para valores existentes
            categories = []
            for valor, color_rgb in colores_filtrados.items():
                # Crear símbolo de relleno
                symbol = QgsFillSymbol.createSimple({
                    'color': f'{color_rgb[0]},{color_rgb[1]},{color_rgb[2]}',
                    'color_border': borde_color,
                    'width_border': str(grosor_borde)
                })
                
                # Crear categoría
                category = QgsRendererCategory(valor, symbol, str(valor))
                categories.append(category)
            
            # Crear y asignar renderizador
            renderer = QgsCategorizedSymbolRenderer(campo, categories)
            
            # Manejar diferentes versiones de QGIS
            try:
                renderer.setShowAllCategories(False)
            except AttributeError:
                try:
                    renderer.setShowAllSymbols(False)
                except AttributeError:
                    pass  # Si no existe el método, continuar igual
            
            capa.setRenderer(renderer)
            capa.triggerRepaint()
            
            capas_estilizadas += 1
            print(f"🎨 Estilo programático aplicado a capa: {capa.name()}")
        else:
            print(f"⚠️  No se especificó método de estilización para: {capa.name()}")
    
    # Actualizar vista del mapa
    if capas_estilizadas > 0:
        iface.mapCanvas().refreshAllLayers()
    
    return capas_estilizadas

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
palayer = iface.addVectorLayer(pais_path, 'pais', 'ogr')


if palayer:
    # Crear un símbolo simple
    symbol = QgsFillSymbol.createSimple({
       'color': '250, 250, 250',  # Blanco hueso
       'color_border': '200, 200, 200',  # Gris
       'width_border': '0.3'
    })

    palayer.setOpacity(0.9)
    
    # Aplicar el símbolo a la capa
    palayer.renderer().setSymbol(symbol)
    
    # Refrescar la capa para ver los cambios
    palayer.triggerRepaint()
    iface.layerTreeView().refreshLayerSymbology(palayer.id())

# Verificar carga correcta
if not palayer.isValid():
    print("¡Error al cargar el shapefile!")


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
    

    expression = "CD_UF IN ({})".format(','.join(["'{}'".format(c) for c in codigos_est]))

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
####################################################################
interlayer = QgsVectorLayer(inter_path, 'intermedios', 'ogr')


# Verificar carga correcta
if not interlayer.isValid():
    print("¡Error al cargar el shapefile!")
else:
    
    # Construir expresión de selección
    expression = "CD_UF IN ({})".format(','.join(["'{}'".format(c) for c in codigos_est]))
    interlayer.selectByExpression(expression)
    
    # Verificar selección y crear nueva capa
    if interlayer.selectedFeatureCount() > 0:
        # Crear capa temporal
        selection_layer = QgsVectorLayer(
            "Polygon?crs={}".format(interlayer.crs().authid()),
            "MunicipiosEsp2",
            "memory"
        )

        # Copiar estructura de campos
        provider = selection_layer.dataProvider()
        provider.addAttributes(interlayer.fields())
        selection_layer.updateFields()
        
        # Copiar features seleccionadas
        features = interlayer.selectedFeatures()
        provider.addFeatures(features)
        selection_layer.updateExtents()
        selection_layer.setOpacity(0.9)
        
        # Añadir al proyecto
        QgsProject.instance().addMapLayer(selection_layer)
        print(f"¡Se seleccionaron {len(features)} municipio(s) de los estados especificados!")

        # Aplicar estilo a la capa recién creada
        symbol = QgsFillSymbol.createSimple({
            'color': '220, 208, 255',  # Vinotinto
            'color_border': '75, 0, 130',  # Indigo
            'width_border': '0.3'     # Grosor del borde
        })
        selection_layer.renderer().setSymbol(symbol)
        selection_layer.triggerRepaint()
        interlayer.setOpacity(0.9)

        # Zoom a la selección
        iface.mapCanvas().setExtent(selection_layer.extent())
        iface.mapCanvas().refresh()
    else:
        print("No se encontraron intermedios con los códigos de estados especificados")
        print("Nombres de campos disponibles:", [field.name() for field in interlayer.fields()])




# Verificar carga correcta
if not interlayer.isValid():
    print("¡Error al cargar el shapefile!")
else:
    # 2. Seleccionar features por código DANE
    
    
    # Construir expresión de selección
    expression = "CD_RGINT IN ({})".format(','.join(["'{}'".format(c) for c in codigos_inter]))

    interlayer.selectByExpression(expression)
    
    # 3. Verificar selección y crear nueva capa
    if interlayer.selectedFeatureCount() > 0:
        # Crear capa temporal
        selection_layer = QgsVectorLayer(
            "Polygon?crs={}".format(interlayer.crs().authid()),
            "inter_seleccionados",
            "memory"
        )
    
        # Copiar estructura de campos
        provider = selection_layer.dataProvider()
        provider.addAttributes(interlayer.fields())
        selection_layer.updateFields()
        
        # Copiar features seleccionadas
        features = interlayer.selectedFeatures()
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
        iface.mapCanvas().zoomToSelected(interlayer)
        iface.mapCanvas().refresh()
    else:
        print("No se encontraron municipios con los códigos especificados")
        print("Nombres de campos disponibles:", [field.name() for field in interlayer.fields()])

# 1b. Cargar la capa de inmediatos seleccionados
####################################################################
inmelayer = QgsVectorLayer(inme_path, 'inmemediatos', 'ogr')


# Verificar carga correcta
if not inmelayer.isValid():
    print("¡Error al cargar el shapefile!")
else:
    
    # Construir expresión de selección
    expression = "CD_RGINT IN ({})".format(','.join(["'{}'".format(c) for c in codigos_inter]))
    inmelayer.selectByExpression(expression)
    
    # Verificar selección y crear nueva capa
    if inmelayer.selectedFeatureCount() > 0:
        # Crear capa temporal
        selection_layer = QgsVectorLayer(
            "Polygon?crs={}".format(inmelayer.crs().authid()),
            "InmeEsp2",
            "memory"
        )

        # Copiar estructura de campos
        provider = selection_layer.dataProvider()
        provider.addAttributes(inmelayer.fields())
        selection_layer.updateFields()
        
        # Copiar features seleccionadas
        features = inmelayer.selectedFeatures()
        provider.addFeatures(features)
        selection_layer.updateExtents()
        selection_layer.setOpacity(0.9)
        
        # Añadir al proyecto
        QgsProject.instance().addMapLayer(selection_layer)
        print(f"¡Se seleccionaron {len(features)} municipio(s) de los estados especificados!")

        # Aplicar estilo a la capa recién creada
        symbol = QgsFillSymbol.createSimple({
            'color': '154, 185, 115',  # Oliva
            'color_border': '0, 100, 0',  # Dark green
            'width_border': '0.5'     # Grosor del borde
        })
        selection_layer.renderer().setSymbol(symbol)
        selection_layer.triggerRepaint()
        inmelayer.setOpacity(0.9)

        # Zoom a la selección
        iface.mapCanvas().setExtent(selection_layer.extent())
        iface.mapCanvas().refresh()
    else:
        print("No se encontraron inmemedios con los códigos de estados especificados")
        print("Nombres de campos disponibles:", [field.name() for field in inmelayer.fields()])




# Verificar carga correcta
if not inmelayer.isValid():
    print("¡Error al cargar el shapefile!")
else:
    # 2. Seleccionar features por código DANE
    
    
    # Construir expresión de selección
    expression = "CD_RGI IN ({})".format(','.join(["'{}'".format(c) for c in codigos_inme]))

    inmelayer.selectByExpression(expression)
    
    # 3. Verificar selección y crear nueva capa
    if inmelayer.selectedFeatureCount() > 0:
        # Crear capa temporal
        selection_layer = QgsVectorLayer(
            "Polygon?crs={}".format(inmelayer.crs().authid()),
            "inmed_seleccionados",
            "memory"
        )
    
        # Copiar estructura de campos
        provider = selection_layer.dataProvider()
        provider.addAttributes(inmelayer.fields())
        selection_layer.updateFields()
        
        # Copiar features seleccionadas
        features = inmelayer.selectedFeatures()
        provider.addFeatures(features)
        selection_layer.updateExtents()
        selection_layer.setOpacity(0.9)
        
        # Añadir al proyecto
        QgsProject.instance().addMapLayer(selection_layer)
        print(f"¡Se seleccionaron {len(features)} inmediato(s)!")

        # Aplicar estilo a la capa recién creada
        symbol = QgsFillSymbol.createSimple({
            'color': '255, 165, 0',  # Dark ORange
            'color_border': '205, 133, 63',  # Peru
            'width_border': '0.5'     # Grosor del borde
        })
        selection_layer.renderer().setSymbol(symbol)
        selection_layer.triggerRepaint()
        
        selection_layer.setOpacity(0.9)

        # Zoom a la selección
        iface.mapCanvas().zoomToSelected(inmelayer)
        iface.mapCanvas().refresh()
    else:
        print("No se encontraron inmediatos con los códigos especificados")
        print("Nombres de campos disponibles:", [field.name() for field in inmelayer.fields()])

        # 1b. Cargar la capa de municipios seleccionados
####################################################################
munilayer = QgsVectorLayer(municipios_path, 'municipios', 'ogr')


# Verificar carga correcta
if not munilayer.isValid():
    print("¡Error al cargar el shapefile!")
else:
    
    # Construir expresión de selección
    expression = "CD_RGI IN ({})".format(','.join(["'{}'".format(c) for c in codigos_inme]))
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
        print(f"¡Se seleccionaron {len(features)} inmediato(s) de los estados especificados!")

        # Aplicar estilo a la capa recién creada
        symbol = QgsFillSymbol.createSimple({
            'color': '255, 165, 0',  # Dark ORange
            'color_border': '205, 133, 63',  # Peru
            'width_border': '0.6'     # Grosor del borde
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
    expression = "CD_MUN IN ({})".format(','.join(["'{}'".format(c) for c in codigos_muni]))

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
           'color': '173, 216, 230',  # Azul claro
           'color_border': '70, 130, 180',  # Azul acero
           'width_border': '0.2'  # Grosor del borde en mm
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

        #Coberturas y Ecosistemas
################

# Cargar la capa
coverblayer = QgsVectorLayer(coberturasB_path, 'Coberturas', "ogr")

# Aplicar el estilo QML
successf = coverblayer.loadNamedStyle(qmlf_path)

# Refrescar la capa para ver los cambios
coverblayer.triggerRepaint()

# 3. Configurar parámetros para el clip
params_coberturas = {
        'INPUT': coverblayer,    # Capa a cortar (ecosistemas)
        'OVERLAY': 'muni_seleccionados',  # Capa de corte (consejos)
        'OUTPUT': 'memory:covfito'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_coberturas = processing.run("native:clip", params_coberturas)
clipped_coberturas = result_coberturas['OUTPUT']
clipped_coberturas.setName("Coberturaf")
QgsProject.instance().addMapLayer(clipped_coberturas)
successf = clipped_coberturas.loadNamedStyle(qmlf_path)

# Aplicar el mismo QML a múltiples capas
#aplicar_estilo_qml_filtrado([clipped_coberturas], qmlf_path, 'fito')

aplicar_estilo_comun_a_capas(
    capas = [clipped_coberturas],
    qml_path = 'qmlf_path'
)

#duplicar
###

#Crear una copia de la capa
capa_duplicada1 = clipped_coberturas.clone()

# Cambiar el nombre para evitar conflictos
capa_duplicada1.setName("coberturasl")

# Agregar la copia al proyecto
QgsProject.instance().addMapLayer(capa_duplicada1)
successl = clipped_coberturas.loadNamedStyle(qmll_path)

# Aplicar el mismo QML a múltiples capas
#aplicar_estilo_qml_filtrado([capa_duplicada1], qmll_path, 'legenda')


#Crear una copia de la capa
capa_duplicada2 = clipped_coberturas.clone()

# Cambiar el nombre para evitar conflictos
capa_duplicada2.setName("coberturasl2")

# Agregar la copia al proyecto
QgsProject.instance().addMapLayer(capa_duplicada2)
successl2 = clipped_coberturas.loadNamedStyle(qmll2_path)

# Aplicar el mismo QML a múltiples capas
#aplicar_estilo_qml_filtrado([capa_duplicada2], qmll2_path, 'legenda2')

aplicar_estilo_comun_a_capas(
    capas = [capa_duplicada2],
    qml_path = 'qmll2_path'
)


#Mata Atlântica
################################

#coverblayer = QgsVectorLayer(coberturasB_path, 'Coberturas', "ogr")
#biomlayer = QgsVectorLayer(Bioma_path, 'Bioma', "ogr")
#
## 3. Configurar parámetros para el clip
#params_biomas = {
#        'INPUT': coverblayer,    # Capa a cortar (ecosistemas)
#        'OVERLAY': biomlayer,  # Capa de corte (consejos)
#        'OUTPUT': 'memory:covfito'   # Salida en memoria
#    }
#
## Añadir resultado al proyecto
#result_biomas = processing.run("native:clip", params_biomas)
#clipped_biomas = result_biomas['OUTPUT']
#clipped_biomas.setName("Mata Atlântica")
#QgsProject.instance().addMapLayer(clipped_biomas)
#successf = clipped_biomas.loadNamedStyle(qmll2_path)

# Capas visibles
#######################################################

# Obtener el árbol de capas
root = QgsProject.instance().layerTreeRoot()

# Lista para almacenar nombres de capas visibles
visible_layers = []

# Recorrer todos los nodos del árbol de capas
for node in root.findLayers():
    # Verificar si el nodo es visible
    if node.isVisible():
        layer = node.layer()
        if layer and layer.isValid():
            visible_layers.append(layer.name())

print("Capas visibles:", visible_layers)



#id: 822
#nome: ÁREA DE PROTEÇÃO AMBIENTAL BAÍA DE TODOS OS SANTOS
#categoria: Área de Proteção Ambiental
#grupo: US
#esfera: estadual
#ano_cria: 1999

#id: 1835
#nome: RESERVA EXTRATIVISTA DE CASSURUBá
#categoria: Reserva Extrativista
#grupo: US
#esfera: federal
#ano_cria: 2009

#id: 1222
#nome: APA SERRA DO MAR
#categoria: Área de Proteção Ambiental
#grupo: US
#esfera: estadual
#ano_cria: 1984

#id: 608
#nome: RESERVA BIOLÓGICA BOM JESUS
#categoria: Reserva Biológica
#grupo: PI
#esfera: federal
#ano_cria: 2012

#id: 1250
#nome: PARQUE NACIONAL DA SERRA DO ITAJAÍ
#categoria: Parque
#grupo: PI
#esfera: federal
#ano_cria: 2004

#id: 1155
#nome: ÁREA DE PROTEÇÃO AMBIENTAL DE CANANÉIA-IGUAPÉ-PERUÍBE
#categoria: Área de Proteção Ambiental
#grupo: US
#esfera: federal
#ano_cria: 1984

#id: 1155
#nome: ÁREA DE PROTEÇÃO AMBIENTAL DE CANANÉIA-IGUAPÉ-PERUÍBE
#categoria: Área de Proteção Ambiental
#grupo: US
#esfera: federal
#ano_cria: 1984

#id: 1630
#nome: ESTAÇÃO ECOLÓGICA JURÉIA-ITATINS
#categoria: Estação Ecológica
#grupo: PI
#esfera: estadual
#ano_cria: 1986


#id: 1946
#nome: ÁREA DE PROTEÇÃO AMBIENTAL DE GUARAQUEÇABA
#categoria: Área de Proteção Ambiental
#grupo: US
#esfera: federal
#ano_cria: 1985

#id: 2038
#nome: PARQUE NACIONAL RESTINGA DE JURUBATIBA
#categoria: Parque
#grupo: PI
#esfera: federal
#ano_cria: 1998

#id: 349
#nome: ÁREA DE PROTEÇÃO AMBIENTAL DE SANTA CRUZ
#categoria: Área de Proteção Ambiental
#grupo: US
#esfera: estadual
#ano_cria: 2008


#Formação Pioneira com influência marinha herbácea