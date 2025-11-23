#Mapa2colores

#https://html-color.codes/olive

region = 'Latin America & Caribbean'
subregion = 'South America'
codigos_dep = ['76'] #76
codigomdep = ['76'] #76
codigos_muni = ['76109'] #18753
cpais = ['COL']



# Lista de nombres de capas a procesar
nombres_capas = ['OpenStreetMap', 'oceano', 'regiones_seleccionados', 'paises_seleccionados', 'departamentos', 'departamentos_seleccionados', 'MunicipiosDep2', 'municipios_seleccionados', 'Ecosis 2024', 'Ecosis 2018', 'Cobertura 2020', 'Cobertura 2018']
oceano_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Mundo/ne_10m_ocean/ne_10m_ocean.shp'
region_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Mundo/ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp'
pais_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Mundo/ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp'
departamentos_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Colombia Dane/ADMINISTRATIVO/MGN_DPTO_POLITICO.shp'
municipios_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Municipios/Municipios2/MGN_MPIO_POLITICO.shp'
consejos_path = '/Volumes/Disco J/Mapas/Consejo_Comunitario_Titulado/Consejo_Comunitario_Titulado.shp'
resguardos_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Resguardos/Resguardo_Indigena_Formalizado/Resguardo_Indigena_Formalizado.shp'
campesinas_path = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/ZPRNRMA_1125_2021/ZPRNRMA_1125_2021.shp'
coberturas_path = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Coberturas Vegetales/Corregidas Coberturas.gpkg'
ecosistemas_path = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Ecositemas/corregidos.gpkg'
coberturas_path1 = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Coberturas Vegetales/Corregidas Coberturas1.gpkg'
ecosistemas_path1 = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Ecositemas/corregidos1.gpkg'

vias_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Colombia Dane/VIAS/VIAS.shp'
vias2_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/INVIAS/Invias_Vias.gpkg'
linea_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Colombia Dane/URBANO/MGN_URB_LINEA.shp'
manzana_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Colombia Dane/URBANO/MGN_URB_MANZANA.shp'
nomenclatura_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Colombia Dane/URBANO/MGN_URB_NOMENCLATURA_VIAL.shp'
cultu_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Colombia Dane/RURAL/CBD_RUR_CULTU_PUNTO.shp'
hidro_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Colombia Dane/RURAL/CBD_RUR_HIDRO_LINEA.shp'
hipso_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Colombia Dane/RURAL/CBD_RUR_HIPSO_PUNTO.shp'
otrli_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Colombia Dane/RURAL/CBD_RUR_OTRLI_LINEA.shp'
ambitos_path = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Ambitos_Territoriales_PDET/Ambitos_Territoriales_PDET.shp'
zonip_path = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Zonificacion_PDET_agosto_2021/Zonificacion_PDET_agosto_2021.shp'
autoridades_path = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Autoridades Ambientales/Lim_AA_25k_2019.shp'
marinos_path = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Ecosistemas Marinos/Mapa_de_Ecosistemas_MEC_100K/Mapa_de_Ecosistemas_MEC_100K.shp'
coral_path = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Ecosistemas Marinos/FormacionesCoralinas_Oceanico/FormacionesCoralinas_Oceanico.shp'
rocoso_path = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Ecosistemas Marinos/Litoral_Rocoso/litoralrocoso_litoralrocoso.shp'
prioc_path = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Ecosistemas Marinos/Sitios_Prioritarios_Conservación_Caribe/Sitios_Prioritarios_Conservación_Caribe.shp'
priop_path = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Ecosistemas Marinos/Sitios_Prioritarios_Conservación_Pacífico/Sitios_Prioritarios_Conservación_Pacífico.shp'
forestal_path = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Gobernanza_Forestal/Gobernanza_Forestal.shp'
humedales_path = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Humedal_version3/Humedal_version3.shp'
paramos_path = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Paramos_Delimitados_Junio_2020/Paramos_Delimitados_Junio_2020.shp'
seco_path = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/BosqueSecoTropical_100K/geo_export_1c851a13-97b1-4163-9ea1-d300bad45e9e.shp'
parques_path = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Parque Nacionales/runap_-_Registro_Unico_Nacional_AP/runap_-_Registro_Unico_Nacional_AP.shp'
priocon_path = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Prioridad_Conpes/PCN_CONPES.shp'
recu_path = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Recuperacion/Recuperacion Corregidos.gpkg'
reha_path = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Rehabilitacion/Rehabilitacion corregido.gpkg'
resta_path = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Restauracion/Corregidos Restauracion.gpkg'

#veredas_path = '/Volumes/Disco J/Mapas/Zonificacion Colombia/Veredas/CRVeredas_2020.shp'

# Lista de nombres de capas a procesar pc Andrey
#nombres_capas = ['OpenStreetMap', 'oceano', 'regiones_seleccionados', 'paises_seleccionados', 'departamentos', 'departamentos_seleccionados', 'MunicipiosDep2', 'municipios_seleccionados', 'Consejos2', 'veredas_en_consejos']
# Lista de nombres de capas a procesar
nombres_capas = ['OpenStreetMap', 'oceano', 'regiones_seleccionados', 'paises_seleccionados', 'departamentos', 'departamentos_seleccionados', 'MunicipiosDep2', 'municipios_seleccionados', 'Consejos2', 'Ecosis 2024', 'Ecosis 2018', 'Cobertura 2020', 'Cobertura 2018', 'hipso', 'hidro', 'otrli', 'vias2', 'parques', 'seco', 'humedales', 'paramos', 'forestal', 'zonip', 'ambitos', 'procon', 'autoridades', 'coral', 'priop', 'prioc', 'coral', 'marinos', 'rocoso']

#oceano_path = '/run/user/1000/gvfs/smb-share:server=pc-de-javier.local,share=disco%20j/Mapas/Zonificacion Colombia/Mundo/ne_10m_ocean/ne_10m_ocean.shp'
#region_path = '/run/user/1000/gvfs/smb-share:server=pc-de-javier.local,share=disco%20j/Mapas/Zonificacion Colombia/Mundo/ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp'
#pais_path = '/run/user/1000/gvfs/smb-share:server=pc-de-javier.local,share=disco%20j/Mapas/Zonificacion Colombia/Mundo/ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp'
#departamentos_path = '/run/user/1000/gvfs/smb-share:server=pc-de-javier.local,share=disco%20j/Mapas/Zonificacion Colombia/Colombia Dane/ADMINISTRATIVO/MGN_DPTO_POLITICO.shp'
#municipios_path = '/run/user/1000/gvfs/smb-share:server=pc-de-javier.local,share=disco%20j/Mapas/Zonificacion Colombia/Municipios/Municipios2/MGN_MPIO_POLITICO.shp'
#consejos_path = '/run/user/1000/gvfs/smb-share:server=pc-de-javier.local,share=disco%20j/Mapas/Consejo_Comunitario_Titulado/Consejo_Comunitario_Titulado.shp'
#veredas_path = '/run/user/1000/gvfs/smb-share:server=pc-de-javier.local,share=disco%20j/Mapas/Zonificacion Colombia/Veredas/CRVeredas_2020.shp'

#estilos
#########################
def aplicar_estilo_comun_a_capas(capas, campo, colores_por_valor, borde_color='0, 0, 0', grosor_borde=0.2):
    """
    Aplica la misma simbología categorizada a múltiples capas de polígonos
    
    Parámetros:
    - capas: Lista de capas vectoriales (QgsVectorLayer) o nombres de capas
    - campo: Nombre del campo común para categorizar
    - colores_por_valor: Diccionario {valor: (R,G,B)} con los colores para cada categoría
    - borde_color: Color del borde en formato 'R,G,B' (opcional)
    - grosor_borde: Grosor del borde en mm (opcional)
    
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
        for valor, color_rgb in colores_filtrados.items():  # ¡CAMBIADO! Usar colores_filtrados
            # Crear símbolo de relleno (siempre se ejecuta porque estamos usando colores_filtrados)
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
        capa.setRenderer(renderer)

        # ¡ESTA ES LA CLAVE! Configurar para no mostrar categorías vacías
        #renderer.setShowAllSymbols(False)  # Oculta categorías sin features
        
        capa.setRenderer(renderer)

        # Forzar actualización
        capa.triggerRepaint()
        iface.layerTreeView().refreshLayerSymbology(capa.id())
        
        capas_estilizadas += 1
        print(f"Estilo aplicado a capa: {capa.name()}")
    
    # Actualizar vista del mapa
    if capas_estilizadas > 0:
        iface.mapCanvas().refreshAllLayers()
    
    return capas_estilizadas

#Colores
###################################

colores_cov = {
            '1.1.1. Tejido urbano continuo': (204, 0, 0),
            '1.1.2. Tejido urbano discontinuo': (248, 0, 0),
            '1.2.1. Zonas industriales o comerciales': (204, 77, 42),
            '1.2.2. Red vial, ferroviaria y terrenos asociados': (217, 101, 69),
            '1.2.3. Zonas portuarias': (225, 132, 107),
            '1.2.4. Aeropuertos': (231, 156, 135),
            '1.2.5. Obras hidráulicas': (238, 185, 170),
            '1.3.1. Zonas de extracción minera': (167, 0, 204),
            '1.3.2. Zona de disposición de residuos': (212, 23, 255),
            '1.4.1. Zonas verdes urbanas': (255, 128, 128),
            '1.4.2. Instalaciones recreativas': (255, 176, 176),
            '2.1.1. Otros cultivos transitorios': (255, 255, 166),
            '2.1.2. Cereales': (255, 255, 95),
            '2.1.3. Oleaginosas y leguminosas': (238, 232, 0),
            '2.1.4. Hortalizas': (209, 206, 0),
            '2.1.5. Tubérculos': (181, 178, 0),
            '2.2.1. Cultivos permanentes herbáceos': (242, 205, 167),
            '2.2.2. Cultivos permanentes arbustivos': (237, 183, 128),
            '2.2.3. Cultivos permanentes arbóreos': (232, 161, 90),
            '2.2.4. Cultivos agroforestales': (227, 141, 54),
            '2.2.5. Cultivos confinados': (214, 122, 30),
            '2.3.1. Pastos limpios': (204, 255, 204),
            '2.3.2. Pastos arbolados': (158, 255, 158),
            '2.3.3. Pastos enmalezados': (158, 255, 200),
            '2.4.1. Mosaico de cultivos': (255, 230, 166),
            '2.4.2. Mosaico de pastos y cultivos': (255, 216, 117),
            '2.4.3. Mosaico de cultivos, pastos y espacios naturales': (255, 201, 64),
            '2.4.4. Mosaico de pastos con espacios naturales': (255, 183, 0),
            '2.4.5. Mosaico de cultivos con espacios naturales': (214, 154, 0),
            '3.1.1. Bosque denso': (71, 143, 0),
            '3.1.2. Bosque abierto': (85, 171, 0),
            '3.1.3. Bosque fragmentado': (97, 194, 0),
            '3.1.4. Bosque de galería y ripario': (112, 224, 0),
            '3.1.5. Plantación forestal': (128, 255, 0),
            '3.2.1. Herbazal': (204, 242, 78),
            '3.2.2. Arbustal': (172, 219, 15),
            '3.2.3. Vegetación secundaria o en transición': (150, 191, 13),
            '3.3.1. Zonas arenosas naturales': (194, 194, 194),
            '3.3.2. Afloramientos rocosos': (179, 179, 179),
            '3.3.3. Tierras desnudas y degradadas': (158, 158, 158),
            '3.3.4. Zonas quemadas': (138, 138, 138),
            '3.3.5. Zonas glaciares y nivales': (101, 101, 181),
            '4.1.1. Zonas Pantanosas': (166, 166, 255),
            '4.1.2. Turberas': (145, 145, 255),
            '4.1.3. Vegetación acuática sobre cuerpos de agua': (115, 115, 255),
            '4.2.1. Pantanos costeros': (204, 204, 255),
            '4.2.2. Salitral': (184, 184, 255),
            '4.2.3. Sedimentos expuestos en bajamar': (166, 166, 255),
            '5.1.1. Ríos': (0, 0, 248),
            '5.1.2. Lagunas, lagos y ciénagas naturales': (0, 128, 255),
            '5.1.3. Canales': (0, 178, 255),
            '5.1.4. Cuerpos de agua artificiales': (0, 206, 242),
            '5.2.1. Lagunas costeras': (69, 224, 245),
            '5.2.3. Estanques para acuicultura marina': (204, 246, 255)
        }

colores_cov1 = {
            '111': (204, 0, 0),
            '112': (248, 0, 0),
            '121': (204, 77, 42),
            '122': (217, 101, 69),
            '123': (225, 132, 107),
            '124': (231, 156, 135),
            '125': (238, 185, 170),
            '131': (167, 0, 204),
            '132': (212, 23, 255),
            '141': (255, 128, 128),
            '142': (255, 176, 176),
            '211': (255, 255, 166),
            '212': (255, 255, 95),
            '213': (238, 232, 0),
            '214': (209, 206, 0),
            '215': (181, 178, 0),
            '221': (242, 205, 167),
            '222': (237, 183, 128),
            '223': (232, 161, 90),
            '224': (227, 141, 54),
            '225': (214, 122, 30),
            '231': (204, 255, 204),
            '232': (158, 255, 158),
            '233': (158, 255, 200),
            '241': (255, 230, 166),
            '242': (255, 216, 117),
            '243': (255, 201, 64),
            '244': (255, 183, 0),
            '245': (214, 154, 0),
            '311': (71, 143, 0),
            '312': (85, 171, 0),
            '313': (97, 194, 0),
            '314': (112, 224, 0),
            '315': (128, 255, 0),
            '321': (204, 242, 78),
            '322': (172, 219, 15),
            '323': (150, 191, 13),
            '331': (194, 194, 194),
            '332': (179, 179, 179),
            '333': (158, 158, 158),
            '334': (138, 138, 138),
            '335': (101, 101, 181),
            '411': (166, 166, 255),
            '412': (145, 145, 255),
            '413': (115, 115, 255),
            '421': (204, 204, 255),
            '422': (184, 184, 255),
            '423': (166, 166, 255),
            '511': (0, 0, 248),
            '512': (0, 128, 255),
            '513': (0, 178, 255),
            '514': (0, 206, 242),
            '521': (69, 224, 245),
            '523': (204, 246, 255)
        }


colores_eco = {
            'Agroecosistema arrocero': (255, 245, 235),
            'Agroecosistema cafetero': (252, 239, 227),
            'Agroecosistema cañero': (250, 234, 220),
            'Agroecosistema de cultivos permanentes': (247, 224, 205),
            'Agroecosistema de cultivos transitorios': (247, 221, 200),
            'Agroecosistema de mosaico de cultivos y espacios naturales': (245, 211, 186),
            'Agroecosistema de mosaico de cultivos y pastos': (242, 204, 179),
            'Agroecosistema de mosaico de cultivos, pastos y espacios naturales': (240, 198, 173),
            'Agroecosistema de mosaico de pastos y espacios naturales': (240, 194, 165),
            'Agroecosistema forestal': (237, 188, 159),
            'Agroecosistema ganadero': (237, 183, 154),
            'Agroecosistema palmero': (235, 177, 145),
            'Agroecosistema papero': (235, 172, 141),
            'Agroecosistema platanero y bananero': (232, 165, 135),
            'Arbustal andino humedo': (162, 181, 65),
            'Arbustal basal humedo': (150, 168, 59),
            'Arbustal inundable andino': (131, 148, 46),
            'Arbustal inundable basal': (122, 138, 41),
            'Arbustal inundable costero': (125, 150, 36),
            'Arbustal inundable subandino': (112, 128, 36),
            'Arbustal subandino humedo': (103, 117, 30),
            'Bosque andino humedo': (42, 173, 42),
            'Bosque andino seco': (40, 163, 38),
            'Bosque basal humedo': (37, 158, 35),
            'Bosque basal seco': (35, 156, 33),
            'Bosque de galeria basal humedo': (32, 150, 30),
            'Bosque de galeria basal seco': (31, 145, 29),
            'Bosque de galeria inundable basal': (29, 143, 27),
            'Bosque de galeria inundable costero': (27, 138, 25),
            'Bosque fragmentado con pastos y cultivos': (21, 125, 19),
            'Bosque fragmentado con vegetacion secundaria': (22, 128, 20),
            'Bosque inundable andino': (20, 120, 18),
            'Bosque inundable basal': (19, 115, 16),
            'Bosque inundable costero': (18, 112, 15),
            'Bosque inundable subandino': (16, 107, 13),
            'Bosque mixto de guandal': (14, 102, 11),
            'Bosque ripario inundable subandino': (13, 97, 10),
            'Bosque subandino humedo': (12, 94, 9),
            'Bosque subandino seco': (11, 89, 8),
            'Complejos rocosos de los andes': (166, 66, 46),
            'Complejos rocosos de serranias': (138, 56, 36),
            'Coralino continental': (240, 98, 127),
            'Coralino oceanico': (122, 142, 245),
            'Cuerpo de agua artificial': (119, 150, 178),
            'Desierto': (252, 180, 10),
            'Fondos blandos': (237, 222, 50),
            'Fondos blandos con vegetacion no vascular': (190, 255, 232),
            'Fondos duros con vegetacion no vascular': (99, 209, 130),
            'Fondos duros no coralinos': (212, 157, 68),
            'Glaciares y nivales': (242, 241, 237),
            'Herbazal andino humedo': (204, 184, 55),
            'Herbazal basal humedo': (191, 173, 52),
            'Herbazal inundable andino': (179, 161, 48),
            'Herbazal inundable basal': (166, 150, 45),
            'Herbazal inundable costero': (153, 138, 41),
            'Herbazal inundable subandino': (140, 127, 38),
            'Herbazal subandino humedo': (128, 115, 34),
            'Lago Tectonico': (0, 183, 198),
            'Laguna Aluvial': (0, 181, 214),
            'Laguna costera': (0, 122, 165),
            'Laguna Glacial': (76, 206, 209),
            'Laguna Tectonica': (40, 196, 216),
            'Llanura mareal': (140, 224, 209),
            'Manglar': (9, 84, 7),
            'Manglar de aguas marinas': (8, 82, 6),
            'Manglar de aguas mixohalinas': (7, 77, 5),
            'Otras areas': (186, 186, 184),
            'Paramo': (132, 0, 168),
            'Playas costeras': (255, 255, 173),
            'Pradera de pastos marinos': (153, 235, 0),
            'Rio de Aguas Blancas': (0, 114, 198),
            'Rio de Aguas Claras': (0, 63, 119),
            'Rio de Aguas Negras': (0, 56, 107),
            'Sabana estacional': (250, 219, 20),
            'Sabana inundable': (84, 183, 198),
            'Sin informacion': (255, 255, 255),
            'Subxerofitia andina': (255, 0, 255),
            'Subxerofitia basal': (212, 110, 212),
            'Subxerofitia subandina': (255, 28, 206),
            'Territorio artificializado': (250, 5, 21),
            'Transicional transformado': (0, 96, 124),
            'Transicional transformado costero': (63, 96, 117),
            'Turbera andina': (94, 221, 161),
            'Turbera de paramo': (94, 221, 193),
            'Vegetacion secundaria': (96, 222, 64),
            'Xerofitia arida': (232, 88, 210),
            'Xerofitia desertica': (250, 95, 227),
            'Zona pantanosa andina': (58, 95, 158),
            'Zona pantanosa basal': (60, 88, 143),
            'Zona pantanosa subandina': (58, 73, 114),
            'Zonas arenosas naturales': (255, 255, 207),
            'Zonas pantanosas costeras': (59, 74, 115),
            'Zonas pantanosas salinas': (102, 147, 188)
        }


colores_eco1 = {
            'Agroecosistema Arrocero': (255, 248, 241),
            'Agroecosistema Cafetero': (253, 244, 235),
            'Agroecosistema Cañero': (252, 240, 231),
            'Agroecosistema Forestal': (242, 208, 188),
            'Agroecosistema Ganadero': (242, 205, 184),
            'Agroecosistema Palmero': (241, 200, 178),
            'Agroecosistema Papero': (241, 197, 175),
            'Agroecosistema Platanero y Bananero': (239, 192, 171),
            'Agroecosistema de Cultivos Permanentes': (249, 233, 220),
            'Agroecosistema de Cultivos Transitorios': (249, 231, 217),
            'Agroecosistema de Mosaico de Cultivos y Espacios Naturales': (248, 224, 207),
            'Agroecosistema de Mosaico de Cultivos y Pastos': (246, 219, 202),
            'Agroecosistema de Mosaico de Cultivos, Pastos y Espacios Naturales': (253, 215, 198),
            'Agroecosistema de Mosaico de Pastos y Espacios Naturales': (245, 212, 192),
            'Arbustal Andino Humedo': (190, 203, 122),
            'Arbustal Basal Humedo': (182, 194, 118),
            'Arbustal Inundable Andino': (168, 180, 109),
            'Arbustal Inundable Basal': (162, 173, 105),
            'Arbustal Inundable Costero': (159, 168, 103),
            'Arbustal Inundable Subandino': (155, 166, 102),
            'Arbustal Subandino Humedo': (149, 158, 98),
            'Bosque Andino Humedo': (106, 198, 106),
            'Bosque Andino Seco': (105, 191, 103),
            'Bosque Basal Humedo': (102, 187, 101),
            'Bosque Basal Seco': (101, 186, 100),
            'Bosque Fragmentado con Pastos y Cultivos': (91, 164, 90),
            'Bosque Fragmentado con Vegetacion Secundaria': (92, 166, 91),
            'Bosque Inundable Andino': (91, 161, 89),
            'Bosque Inundable Basal': (90, 157, 88),
            'Bosque Inundable Costero': (89, 155, 87),
            'Bosque Inundable Subandino': (88, 151, 86),
            'Bosque Ripario Inundable Subandino': (86, 144, 84),
            'Bosque Subandino Humedo': (85, 142, 83),
            'Bosque Subandino Seco': (84, 139, 82),
            'Bosque de Galeria Basal Humedo': (99, 182, 98),
            'Bosque de Galeria Basal Seco': (98, 178, 97),
            'Bosque de Galeria Inundable Basal': (97, 177, 95),
            'Bosque de Galeria Inundable Costero': (95, 173, 94),
            'Complejos Rocosos Andinos': (193, 123, 109),
            'Complejos Rocosos de Serranias': (173, 116, 102),
            'Coralino Continental': (245, 145, 165),
            'Coralino Oceanico': (162, 176, 248),
            'Cuerpo de Agua Artificial': (160, 182, 201),
            'Desierto': (253, 203, 84),
            'Fondos Blandos': (242, 232, 112),
            'Fondos Blandos con Vegetacion No Vascular': (210, 255, 239),
            'Fondos Duros No Coralinos': (225, 186, 124),
            'Fondos Duros con Vegetacion No Vascular': (146, 223, 168),
            'Glaciares y Nivales': (246, 245, 242),
            'Herbazal Andino Humedo': (219, 205, 115),
            'Herbazal Basal Humedo': (210, 198, 113),
            'Herbazal Inundable Andino': (202, 189, 110),
            'Herbazal Inundable Basal': (193, 182, 108),
            'Herbazal Inundable Costero': (184, 173, 105),
            'Herbazal Inundable Subandino': (175, 165, 103),
            'Herbazal Subandino Humedo': (166, 157, 100),
            'Laguna Aluvial': (77, 203, 226),
            'Laguna Costera': (77, 162, 192),
            'Laguna Glacial': (130, 221, 223),
            'Laguna Tectonica': (105, 214, 228),
            'Llanura Mareal': (175, 233, 223),
            'Manglar': (83, 135, 81),
            'Paramo': (169, 77, 194),
            'Playas Costeras': (255, 255, 198),
            'Pradera de Pastos Marinos': (184, 241, 77),
            'Rio de Aguas Blancas': (77, 156, 215),
            'Rio de Aguas Claras': (77, 121, 160),
            'Rio de Aguas Negras': (77, 116, 151),
            'Sabana Estacional': (252, 230, 91),
            'Sabana Inundable': (135, 205, 215),
            'Subxerofitia Andina': (255, 77, 255),
            'Subxerofitia Basal': (225, 154, 225),
            'Subxerofitia Subandina': (255, 96, 221),
            'Territorio Artificializado': (252, 80, 91),
            'Transicional Transformado': (77, 144, 163),
            'Transicional Transformado Costero': (121, 144, 158),
            'Turbera Andina': (142, 231, 189),
            'Turbera de Paramo': (142, 231, 212),
            'Vegetación Secundaria': (144, 232, 121),
            'Xerofitia Arida': (239, 138, 224),
            'Xerofitia Desertica': (252, 143, 235),
            'Zona Pantanosa Andina': (117, 143, 187),
            'Zona Pantanosa Basal': (119, 138, 177),
            'Zona Pantanosa Subandina': (118, 128, 157),
            'Zonas Arenosas Naturales': (255, 255, 221),
            'Zonas Pantanosas Costeras': (117, 128, 156),
            'Zonas Pantanosas Salinas': (148, 179, 208),
       }



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
        #print("IDs de features seleccionados:", selected_ids)
        print("Número de features en selection_layer:", selection_layer.featureCount())
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


# Obtener la capa activa

#forma
######################################
# Iterar sobre cada feature

# Después de crear selection_layer
#if selection_layer.featureCount() > 0:
#    # Obtener el PRIMER feature
#    first_feature = next(selection_layer.getFeatures())
#    geometry = first_feature.geometry()
#    wkt_string = geometry.asWkt()
#    print("WKT del primer municipio seleccionado:")
#    print(wkt_string)
#    
#    # Opcional: Si quieres trabajar solo con este feature, crea una nueva capa con solo él
#    single_feature_layer = QgsVectorLayer(
#        "Polygon?crs={}".format(selection_layer.crs().authid()),
#        "municipio_unico",
#        "memory"
#    )
#    provider = single_feature_layer.dataProvider()
#    provider.addAttributes(selection_layer.fields())
#    single_feature_layer.updateFields()
#    provider.addFeature(first_feature)
#    QgsProject.instance().addMapLayer(single_feature_layer)

# Obtener el primer feature de la capa de selección
first_feature = next(selection_layer.getFeatures())
geometry = first_feature.geometry()
wkt_string = geometry.asWkt()
print(wkt_string)  # WKT de solo UN municipio
for feature in selection_layer.getFeatures():
    geometry = feature.geometry()
    wkt_string = geometry.asWkt()  # Convertir geometría a WKT
    print(wkt_string)

#Coberturas y Ecosistemas
################

# Cargar la capa
coverlayer = QgsVectorLayer(coberturas_path, 'Coberturas', "ogr")


# 3. Configurar parámetros para el clip
params_coberturas = {
        'INPUT': coverlayer,    # Capa a cortar (ecosistemas)
        'OVERLAY': selection_layer,  # Capa de corte (consejos)
        'OUTPUT': 'memory:cov2018'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_coberturas = processing.run("native:clip", params_coberturas)
clipped_coberturas = result_coberturas['OUTPUT']
clipped_coberturas.setName("Cobertura 2018")
QgsProject.instance().addMapLayer(clipped_coberturas)


# Aplicar a capas por nombre
aplicar_estilo_comun_a_capas(
    capas = [clipped_coberturas],
    campo = 'nivel_3',  # Campo común en todas las capas
    colores_por_valor = colores_cov,
    borde_color = '0,0,0',    # Borde negro
    grosor_borde = 0.3        # 0.3 mm de grosor
)


# Cargar la capa
ecolayer = QgsVectorLayer(ecosistemas_path, 'Ecosistemas', "ogr")

# 3. Configurar parámetros para el clip
params_ecosistemas = {
        'INPUT': ecolayer,    # Capa a cortar (ecosistemas)
        'OVERLAY': selection_layer,  # Capa de corte (consejos)
        'OUTPUT': 'memory:eco2018'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_ecosistemas = processing.run("native:clip", params_ecosistemas)
clipped_ecosistemas = result_ecosistemas['OUTPUT']
clipped_ecosistemas.setName("Ecosis 2018")
QgsProject.instance().addMapLayer(clipped_ecosistemas)


# Aplicar a capas por nombre
aplicar_estilo_comun_a_capas(
    capas = [clipped_ecosistemas],
    campo = 'ECOS_GENER',  # Campo común en todas las capas
    colores_por_valor = colores_eco,
    borde_color = '0, 0, 0',    # Borde negro
    grosor_borde = 0.3        # 0.3 mm de grosor
)


# Cargar la capa
coverlayer1 = QgsVectorLayer(coberturas_path1, 'Coberturas20', "ogr")

# 3. Configurar parámetros para el clip
params_coberturas1 = {
        'INPUT': coverlayer1,    # Capa a cortar (ecosistemas)
        'OVERLAY': selection_layer,  # Capa de corte (consejos)
        'OUTPUT': 'memory:cov2020'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_coberturas1 = processing.run("native:clip", params_coberturas1)
clipped_coberturas2020 = result_coberturas1['OUTPUT']
clipped_coberturas2020.setName("Cobertura 2020")
QgsProject.instance().addMapLayer(clipped_coberturas2020)

# Aplicar a capas por nombre
aplicar_estilo_comun_a_capas(
    capas = [clipped_coberturas2020],
    campo = 'nivel_3',  # Campo común en todas las capas
    colores_por_valor = colores_cov1,
    borde_color = '0,0,0',    # Borde negro
    grosor_borde = 0.3        # 0.3 mm de grosor
)

# Cargar la capa
ecolayer1 = QgsVectorLayer(ecosistemas_path1, 'Ecosistemas20', "ogr")


# 3. Configurar parámetros para el clip
params_ecosistemas1 = {
        'INPUT': ecolayer1,    # Capa a cortar (ecosistemas)
        'OVERLAY': selection_layer,  # Capa de corte (consejos)
        'OUTPUT': 'memory:eco2024'   # Salida en memoria
    }


# Añadir resultado al proyecto
result_ecosistemas1 = processing.run("native:clip", params_ecosistemas1)
clipped_ecosistemas1 = result_ecosistemas1['OUTPUT']
clipped_ecosistemas1.setName("Ecosis 2024")
QgsProject.instance().addMapLayer(clipped_ecosistemas1)


# Aplicar a capas por nombre
aplicar_estilo_comun_a_capas(
    capas = [clipped_ecosistemas1],
    campo = 'ecos_gener',  # Campo común en todas las capas
    colores_por_valor = colores_eco1,
    borde_color = '0, 0, 0',    # Borde negro
    grosor_borde = 0.3        # 0.3 mm de grosor
)

#Corporaciones
################

# Cargar la capa
autoridadeslayer = QgsVectorLayer(autoridades_path, 'autoridades', "ogr")


# 3. Configurar parámetros para el clip
params_autoridades = {
        'INPUT': autoridadeslayer,    # Capa a cortar 
        'OVERLAY': selection_layer,  # Capa de corte
        'OUTPUT': 'memory:autoC'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_autoridades = processing.run("native:clip", params_autoridades)
clipped_autoridades = result_autoridades['OUTPUT']
clipped_autoridades.setName("autoridades")
QgsProject.instance().addMapLayer(clipped_autoridades)

#Forestal
################

# Cargar la capa
forestalayer = QgsVectorLayer(forestal_path, 'forestal', "ogr")


# 3. Configurar parámetros para el clip
params_forestal = {
        'INPUT': forestalayer,    # Capa a cortar 
        'OVERLAY': selection_layer,  # Capa de corte
        'OUTPUT': 'memory:forestalC'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_forestal = processing.run("native:clip", params_forestal)
clipped_forestal = result_forestal['OUTPUT']
clipped_forestal.setName("forestal")
QgsProject.instance().addMapLayer(clipped_forestal)

#Humedales
################

# Cargar la capa
humedaleslayer = QgsVectorLayer(humedales_path, 'humedales', "ogr")


# 3. Configurar parámetros para el clip
params_humedales = {
        'INPUT': humedaleslayer,    # Capa a cortar 
        'OVERLAY': selection_layer,  # Capa de corte
        'OUTPUT': 'memory:humedalesC'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_humedales = processing.run("native:clip", params_humedales)
clipped_humedales = result_humedales['OUTPUT']
clipped_humedales.setName("humedales")
QgsProject.instance().addMapLayer(clipped_humedales)

symbolh = QgsFillSymbol.createSimple({
        'color': '0, 166, 147',  # '25, 100, 180' azul
        'color_border': '1, 121, 111',  # Color del borde
        'width_border': '0.3'  # Grosor del borde en mm
})

# Aplicar el símbolo a la capa
rendererh = QgsSingleSymbolRenderer(symbolh)
clipped_humedales.setRenderer(rendererh)

# Refrescar la capa para ver los cambios
clipped_humedales.triggerRepaint()


#Paramos
################

# Cargar la capa
paramoslayer = QgsVectorLayer(paramos_path, 'paramos', "ogr")


# 3. Configurar parámetros para el clip
params_paramos = {
        'INPUT': paramoslayer,    # Capa a cortar 
        'OVERLAY': selection_layer,  # Capa de corte
        'OUTPUT': 'memory:ParamosC'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_paramos = processing.run("native:clip", params_paramos)
clipped_paramos = result_paramos['OUTPUT']
clipped_paramos.setName("paramos")
QgsProject.instance().addMapLayer(clipped_paramos)

symbolp = QgsFillSymbol.createSimple({
        'color': '178, 132, 190',  # '25, 100, 180' azul
        'color_border': '153, 102, 204',  # Color del borde
        'width_border': '0.3'  # Grosor del borde en mm
})

# Aplicar el símbolo a la capa
rendererp = QgsSingleSymbolRenderer(symbolp)
clipped_paramos.setRenderer(rendererp)

# Refrescar la capa para ver los cambios
clipped_paramos.triggerRepaint()



#Seco
################

# Cargar la capa
secolayer = QgsVectorLayer(seco_path, 'seco', "ogr")


# 3. Configurar parámetros para el clip
params_seco = {
        'INPUT': secolayer,    # Capa a cortar 
        'OVERLAY': selection_layer,  # Capa de corte
        'OUTPUT': 'memory:secoC'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_seco = processing.run("native:clip", params_seco)
clipped_seco = result_seco['OUTPUT']
clipped_seco.setName("seco")
QgsProject.instance().addMapLayer(clipped_seco)

symbols = QgsFillSymbol.createSimple({
        'color': '186, 135, 89',  # '25, 100, 180' azul
        'color_border': '160, 120, 90',  # Color del borde
        'width_border': '0.3'  # Grosor del borde en mm
})

# Aplicar el símbolo a la capa
renderers = QgsSingleSymbolRenderer(symbols)
clipped_seco.setRenderer(renderers)

# Refrescar la capa para ver los cambios
clipped_seco.triggerRepaint()

#Parques
################

# Cargar la capa
parqueslayer = QgsVectorLayer(parques_path, 'parques', "ogr")


# 3. Configurar parámetros para el clip
params_parques = {
        'INPUT': parqueslayer,    # Capa a cortar 
        'OVERLAY': selection_layer,  # Capa de corte
        'OUTPUT': 'memory:parquesC'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_parques = processing.run("native:clip", params_parques)
clipped_parques = result_parques['OUTPUT']
clipped_parques.setName("parques")
QgsProject.instance().addMapLayer(clipped_parques)

symbolpar = QgsFillSymbol.createSimple({
        'color': '0, 168, 107',  # '25, 100, 180' azul
        'color_border': '0, 117, 94',  # Color del borde
        'width_border': '0.3'  # Grosor del borde en mm
})

# Aplicar el símbolo a la capa
rendererpar = QgsSingleSymbolRenderer(symbolpar)
clipped_parques.setRenderer(rendererpar)

# Refrescar la capa para ver los cambios
clipped_parques.triggerRepaint()


#Pirorizados
################

# Cargar la capa
prioconlayer = QgsVectorLayer(priocon_path, 'priocon', "ogr")


# 3. Configurar parámetros para el clip
params_priocon = {
        'INPUT': prioconlayer,    # Capa a cortar 
        'OVERLAY': selection_layer,  # Capa de corte
        'OUTPUT': 'memory:prioC'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_priocon = processing.run("native:clip", params_priocon)
clipped_priocon = result_priocon['OUTPUT']
clipped_priocon.setName("priocon")
QgsProject.instance().addMapLayer(clipped_priocon)

colores_priocon = {
            'a': (212, 0, 0),
            'b': (249, 77, 0),
            'c': (255, 130, 67),
            'd': (255, 179, 0),
            'e': (255, 196, 12),
            'f': (255, 216, 0),
            'g': (255, 246, 0),
            'h': (255, 255, 0),
            }

# Aplicar a capas por nombre
aplicar_estilo_comun_a_capas(
    capas = [clipped_priocon],
    campo = 'PRIORIDAD',  # Campo común en todas las capas
    colores_por_valor = colores_priocon,
    borde_color = '0, 0, 0',    # Borde negro
    grosor_borde = 0.3        # 0.3 mm de grosor
)


#Vias
################

# Cargar la capa
viaslayer = QgsVectorLayer(vias_path, 'vias', "ogr")


# 3. Configurar parámetros para el clip
params_vias = {
        'INPUT': viaslayer,    # Capa a cortar 
        'OVERLAY': selection_layer,  # Capa de corte
        'OUTPUT': 'memory:viasC'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_vias = processing.run("native:clip", params_vias)
clipped_vias = result_vias['OUTPUT']
clipped_vias.setName("vias")
QgsProject.instance().addMapLayer(clipped_vias)

symbolv = QgsFillSymbol.createSimple({
        'color': '192, 192, 192',  # '25, 100, 180' azul
        'color_border': '128, 128, 128',  # Color del borde
        'width_border': '0.3'  # Grosor del borde en mm
})

# Aplicar el símbolo a la capa
rendererv = QgsSingleSymbolRenderer(symbolv)
clipped_vias.setRenderer(rendererv)

# Refrescar la capa para ver los cambios
clipped_vias.triggerRepaint()

#Vias2
################

# Cargar la capa
viaslayer2 = QgsVectorLayer(vias2_path, 'vias2', "ogr")


# 3. Configurar parámetros para el clip
params_vias2 = {
        'INPUT': viaslayer2,    # Capa a cortar 
        'OVERLAY': selection_layer,  # Capa de corte
        'OUTPUT': 'memory:vias2C'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_vias2 = processing.run("native:clip", params_vias2)
clipped_vias2 = result_vias2['OUTPUT']
clipped_vias2.setName("vias2")
QgsProject.instance().addMapLayer(clipped_vias2)

symbolv2 = QgsFillSymbol.createSimple({
        'color': '192, 192, 192',  # '25, 100, 180' azul
        'color_border': '128, 128, 128',  # Color del borde
        'width_border': '0.3'  # Grosor del borde en mm
})

# Aplicar el símbolo a la capa
rendererv2 = QgsSingleSymbolRenderer(symbolv2)
clipped_vias2.setRenderer(rendererv2)

# Refrescar la capa para ver los cambios
clipped_vias2.triggerRepaint()


#Linea
################

# Cargar la capa
linealayer = QgsVectorLayer(linea_path, 'linea', "ogr")


# 3. Configurar parámetros para el clip
params_linea = {
        'INPUT': linealayer,    # Capa a cortar 
        'OVERLAY': selection_layer,  # Capa de corte
        'OUTPUT': 'memory:lineaC'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_linea = processing.run("native:clip", params_linea)
clipped_linea = result_linea['OUTPUT']
clipped_linea.setName("linea")
QgsProject.instance().addMapLayer(clipped_linea)

#Nomenclatura
################

# Cargar la capa
nomelayer = QgsVectorLayer(nomenclatura_path, 'nomenclatura', "ogr")


# 3. Configurar parámetros para el clip
params_nomenclatura = {
        'INPUT': nomelayer,    # Capa a cortar 
        'OVERLAY': selection_layer,  # Capa de corte
        'OUTPUT': 'memory:nomeC'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_nomenclatura = processing.run("native:clip", params_nomenclatura)
clipped_nomenclatura = result_nomenclatura['OUTPUT']
clipped_nomenclatura.setName("nomenclatura")
QgsProject.instance().addMapLayer(clipped_nomenclatura)

#Cultu
################

# Cargar la capa
cultulayer = QgsVectorLayer(cultu_path, 'cultu', "ogr")


# 3. Configurar parámetros para el clip
params_cultu = {
        'INPUT': cultulayer,    # Capa a cortar 
        'OVERLAY': selection_layer,  # Capa de corte
        'OUTPUT': 'memory:cultuC'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_cultu = processing.run("native:clip", params_cultu)
clipped_cultu = result_cultu['OUTPUT']
clipped_cultu.setName("cultu")
QgsProject.instance().addMapLayer(clipped_cultu)

#Hipso
################

# Cargar la capa
hipsolayer = QgsVectorLayer(hidro_path, 'hidro', "ogr")


# 3. Configurar parámetros para el clip
params_hipso = {
        'INPUT': hipsolayer,    # Capa a cortar 
        'OVERLAY': selection_layer,  # Capa de corte
        'OUTPUT': 'memory:hipsoC'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_hipso = processing.run("native:clip", params_hipso)
clipped_hipso = result_hipso['OUTPUT']
clipped_hipso.setName("hipso")
QgsProject.instance().addMapLayer(clipped_hipso)


#OTRLI
################

# Cargar la capa
otrlilayer = QgsVectorLayer(otrli_path, 'hidro', "ogr")


# 3. Configurar parámetros para el clip
params_otrli = {
        'INPUT': otrlilayer,    # Capa a cortar 
        'OVERLAY': selection_layer,  # Capa de corte
        'OUTPUT': 'memory:otrliC'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_otrli = processing.run("native:clip", params_otrli)
clipped_otrli = result_otrli['OUTPUT']
clipped_otrli.setName("otrli")
QgsProject.instance().addMapLayer(clipped_otrli)

#Manzana
################

# Cargar la capa
manzanalayer = QgsVectorLayer(manzana_path, 'manzana', "ogr")


# 3. Configurar parámetros para el clip
params_manzana = {
        'INPUT': manzanalayer,    # Capa a cortar 
        'OVERLAY': selection_layer,  # Capa de corte
        'OUTPUT': 'memory:manzanaC'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_manzana = processing.run("native:clip", params_manzana)
clipped_manzana = result_manzana['OUTPUT']
clipped_manzana.setName("manzana")
QgsProject.instance().addMapLayer(clipped_manzana)

#Hidro
################

# Cargar la capa
hidrolayer = QgsVectorLayer(hidro_path, 'hidro', "ogr")


# 3. Configurar parámetros para el clip
params_hidro = {
        'INPUT': hidrolayer,    # Capa a cortar 
        'OVERLAY': selection_layer,  # Capa de corte
        'OUTPUT': 'memory:hidroC'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_hidro = processing.run("native:clip", params_hidro)
clipped_hidro = result_hidro['OUTPUT']
clipped_hidro.setName("hidro")
QgsProject.instance().addMapLayer(clipped_hidro)

symbol = QgsLineSymbol.createSimple({
    'color': '147, 204, 234',  # '25, 100, 180' azul
#   'color_border': '176, 208, 248',  # Color del borde
    'width': '0.3'  # Grosor del borde en mm
})

# Aplicar el símbolo a la capa
renderer = QgsSingleSymbolRenderer(symbol)
clipped_hidro.setRenderer(renderer)

# Refrescar la capa para ver los cambios
clipped_hidro.triggerRepaint()

#AmbitosPDET
################

# Cargar la capa
ambitoslayer = QgsVectorLayer(ambitos_path, 'ambitos', "ogr")


# 3. Configurar parámetros para el clip
params_ambitos = {
        'INPUT': ambitoslayer,    # Capa a cortar 
        'OVERLAY': selection_layer,  # Capa de corte
        'OUTPUT': 'memory:ambitosC'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_ambitos = processing.run("native:clip", params_ambitos)
clipped_ambitos = result_ambitos['OUTPUT']
clipped_ambitos.setName("ambitos")
QgsProject.instance().addMapLayer(clipped_ambitos)

# 1. Listar campos disponibles
print("📋 Campos disponibles:")
for field in clipped_ambitos.fields():
    print(f"   '{field.name()}'")
    
# 2. Verificar valores únicos en el campo de categoría
campo_buscado = 'categotia_'  # Ajusta este nombre si es necesario
valores_encontrados = set()


colores_ambitos = {
            'AEIA': (42, 128, 0),
            'Franja Estabilización': (150, 111, 214),
            'Frontera Agrícola': (255, 215, 0),
       }


# Aplicar a capas por nombre
aplicar_estilo_comun_a_capas(
    capas = [clipped_ambitos],
    campo = 'categoria_',  # Campo común en todas las capas
    colores_por_valor = colores_ambitos,
    borde_color = '0, 0, 0',    # Borde negro
    grosor_borde = 0.3        # 0.3 mm de grosor
)

#ZonificacionPDET
################

# Cargar la capa
zoniplayer = QgsVectorLayer(zonip_path, 'zonip', "ogr")


# 3. Configurar parámetros para el clip
params_zonip = {
        'INPUT': zoniplayer,    # Capa a cortar 
        'OVERLAY': selection_layer,  # Capa de corte
        'OUTPUT': 'memory:zonipC'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_zonip = processing.run("native:clip", params_zonip)
clipped_zonip = result_zonip['OUTPUT']
clipped_zonip.setName("zonip")
QgsProject.instance().addMapLayer(clipped_zonip)

colores_zonip = {
            'Preservación': (0, 102, 0),
            'Protección con uso sostenible': (208, 255, 20),
            'Protección por Alta Oferta de SSEE': (154, 78, 150),
            'Restauración': (128, 218, 235),
            'Uso productivo': (210, 105, 30),
            'Uso productivo con protección': (150, 165, 60),
            'Uso productivo con reconversión': (251, 236, 93),
            'Uso sostenible para el aprovechamiento de la biodiversidad': (250, 128, 114),
            'Uso sostenible para el desarrollo': (255, 127, 80),
            }

# Aplicar a capas por nombre
aplicar_estilo_comun_a_capas(
    capas = [clipped_zonip],
    campo = 'categoria',  # Campo común en todas las capas
    colores_por_valor = colores_zonip,
    borde_color = '0, 0, 0',    # Borde negro
    grosor_borde = 0.3        # 0.3 mm de grosor
)


# Cargar ecosistemas Marinos
############################################

#Cargar marinos

iface.addVectorLayer(marinos_path, 'marinos', 'ogr')
iface.addVectorLayer(coral_path, 'coral', 'ogr')
iface.addVectorLayer(rocoso_path, 'rocoso', 'ogr')
iface.addVectorLayer(prioc_path, 'prioc', 'ogr')
iface.addVectorLayer(priop_path, 'priop', 'ogr')
iface.addVectorLayer(campesinas_path, 'campesinas', 'ogr')


# 1b. Cargar la capa de resguardos
####################################################################

# Versión simplificada
resglayer = QgsVectorLayer(resguardos_path, 'resguardos', 'ogr')

if resglayer.isValid():
    # Seleccionar por códigos de municipio
    expression = "MUNICIPIO IN ({})".format(','.join(["'{}'".format(c) for c in codigos_muni]))
    resglayer.selectByExpression(expression)
    
    if resglayer.selectedFeatureCount() > 0:
        # Crear nueva capa con la selección
        selection_layer = QgsVectorLayer(
            "Polygon?crs={}".format(resglayer.crs().authid()),
            "resguardos_seleccionados", 
            "memory"
        )
        
        # Copiar TODOS los campos y TODAS las features
        provider = selection_layer.dataProvider()
        provider.addAttributes(resglayer.fields())
        selection_layer.updateFields()
        provider.addFeatures(resglayer.selectedFeatures())
        selection_layer.updateExtents()
        
        # Añadir al proyecto
        QgsProject.instance().addMapLayer(selection_layer)
        print(f"✅ Capa creada con {resglayer.selectedFeatureCount()} resguardos")
        
        # Estilo y zoom
        symbol = symbol = QgsFillSymbol.createSimple({
            'color': '253, 188, 180',  # Sunglow
            'color_border': '255, 135, 141',  # Indigo
            'width_border': '0.5'     # Grosor del borde
        })
        selection_layer.renderer().setSymbol(symbol)
        iface.mapCanvas().setExtent(selection_layer.extent())
        
    else:
        print("❌ No se encontraron resguardos")

# 1b. Cargar la capa de consejos
####################################################################

# Versión simplificada
resglayer = QgsVectorLayer(consejos_path, 'consejos', 'ogr')

if resglayer.isValid():
    # Seleccionar por códigos de municipio
    expression = "MUNICIPIO IN ({})".format(','.join(["'{}'".format(c) for c in codigos_muni]))
    resglayer.selectByExpression(expression)
    
    if resglayer.selectedFeatureCount() > 0:
        # Crear nueva capa con la selección
        selection_layer = QgsVectorLayer(
            "Polygon?crs={}".format(resglayer.crs().authid()),
            "consejos_seleccionados", 
            "memory"
        )
        
        # Copiar TODOS los campos y TODAS las features
        provider = selection_layer.dataProvider()
        provider.addAttributes(resglayer.fields())
        selection_layer.updateFields()
        provider.addFeatures(resglayer.selectedFeatures())
        selection_layer.updateExtents()
        
        # Añadir al proyecto
        QgsProject.instance().addMapLayer(selection_layer)
        print(f"✅ Capa creada con {resglayer.selectedFeatureCount()} consejos")
        
        # Estilo y zoom
        symbol = symbol = QgsFillSymbol.createSimple({
            'color': '220, 220, 220',  # Sunglow
            'color_border': '128, 128, 128',  # Indigo
            'width_border': '0.5'     # Grosor del borde
        })
        selection_layer.renderer().setSymbol(symbol)
        iface.mapCanvas().setExtent(selection_layer.extent())
        
    else:
        print("❌ No se encontraron consejos")

#Rehabilitacion
################

# Cargar la capa
rehalayer = QgsVectorLayer(reha_path, 'reha', "ogr")


# 3. Configurar parámetros para el clip
params_reha = {
        'INPUT': rehalayer,    # Capa a cortar 
        'OVERLAY': selection_layer,  # Capa de corte
        'OUTPUT': 'TEMPORARY_OUTPUT' #'memory:rehaC'   # Salida en memoria
    }

# Añadir resultado al proyecto
#result_reha = processing.run("native:clip", params_reha)
clipped_reha = result_reha['OUTPUT']
clipped_reha.setName("reha")
QgsProject.instance().addMapLayer(clipped_reha)

symbolreha = QgsFillSymbol.createSimple({
        'color': '255, 36, 0',  # '25, 100, 180' azul
        'color_border': '178, 34, 34',  # Color del borde
        'width_border': '0.3'  # Grosor del borde en mm
})

# Aplicar el símbolo a la capa
rendererreha = QgsSingleSymbolRenderer(symbolreha)
clipped_reha.setRenderer(rendererreha)

# Refrescar la capa para ver los cambios
clipped_reha.triggerRepaint()



#Recuperacion
################

# Cargar la capa
reculayer = QgsVectorLayer(recu_path, 'recu', "ogr")


# 3. Configurar parámetros para el clip
params_recu = {
        'INPUT': reculayer,    # Capa a cortar 
        'OVERLAY': selection_layer,  # Capa de corte
        'OUTPUT': 'TEMPORARY_OUTPUT' #'memory:recuC'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_recu = processing.run("native:clip", params_recu)
clipped_recu = result_recu['OUTPUT']
clipped_recu.setName("recu")
QgsProject.instance().addMapLayer(clipped_recu)

symbolrecu = QgsFillSymbol.createSimple({
        'color': '255, 117, 24',  # '25, 100, 180' azul
        'color_border': '249, 77, 0',  # Color del borde
        'width_border': '0.3'  # Grosor del borde en mm
})

# Aplicar el símbolo a la capa
rendererrecu = QgsSingleSymbolRenderer(symbolrecu)
clipped_recu.setRenderer(rendererrecu)

# Refrescar la capa para ver los cambios
clipped_recu.triggerRepaint()


#Restauracion
################

# Cargar la capa
restalayer = QgsVectorLayer(resta_path, 'resta', "ogr")


# 3. Configurar parámetros para el clip
params_resta = {
        'INPUT': restalayer,    # Capa a cortar 
        'OVERLAY': selection_layer,  # Capa de corte
        'OUTPUT': 'TEMPORARY_OUTPUT' #'memory:restaC'   # Salida en memoria
    }

# Añadir resultado al proyecto
result_resta = processing.run("native:clip", params_resta)
clipped_resta = result_resta['OUTPUT']
clipped_resta.setName("resta")
QgsProject.instance().addMapLayer(clipped_resta)


symbolresta = QgsFillSymbol.createSimple({
        'color': '228, 208, 10',  # '25, 100, 180' azul
        'color_border': '218, 165, 32',  # Color del borde
        'width_border': '0.3'  # Grosor del borde en mm
})


# Aplicar el símbolo a la capa
rendererresta = QgsSingleSymbolRenderer(symbolresta)
clipped_resta.setRenderer(rendererresta)

# Refrescar la capa para ver los cambios
clipped_resta.triggerRepaint()



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