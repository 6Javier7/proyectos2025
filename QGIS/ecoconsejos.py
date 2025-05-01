from qgis.core import (
    QgsCategorizedSymbolRenderer,
    QgsRendererCategory,
    QgsFillSymbol,
    QgsSymbol,
    QgsVectorLayer
)
from qgis.PyQt.QtGui import QColor


def cargar_capas_directorio(directorio, formatos = None, crs_destino = None):
    """
    Carga todas las capas vectoriales de un directorio en QGIS
    
    Parámetros:
    - directorio: Ruta del directorio a escanear
    - formatos: Lista de extensiones a incluir (ej. ['.gpkg', '.shp'])
    - crs_destino: CRS objetivo para reproyectar (opcional)
    """
    if formatos is None:
        formatos = ['.gpkg', '.shp', '.geojson']
    
    capas_cargadas = []
    
    for root, dirs, files in os.walk(directorio):
        for file in files:
            if any(file.lower().endswith(ext) for ext in formatos):
                ruta_completa = os.path.join(root, file)
                nombre_capa = os.path.splitext(file)[0]
                
                # Cargar capa
                capa = QgsVectorLayer(ruta_completa, nombre_capa, 'ogr')
                
                if capa.isValid():
                    # Reprojectar si se especificó un CRS destino
                    if crs_destino and capa.crs() != crs_destino:
                        reproyectado = processing.run("native:reprojectlayer", {
                            'INPUT': capa,
                            'TARGET_CRS': crs_destino,
                            'OUTPUT': 'memory:'
                        })['OUTPUT']
                        reproyectado.setName(f"{nombre_capa}_reproyectado")
                        QgsProject.instance().addMapLayer(reproyectado)
                        capas_cargadas.append(reproyectado)
                    else:
                        QgsProject.instance().addMapLayer(capa)
                        capas_cargadas.append(capa)
                    
                    print(f"✓ {nombre_capa} cargada desde {ruta_completa}")
                else:
                    print(f"✗ Error al cargar {file}")
    
    # Ajustar vista al contenido (solo si hay capas cargadas)
    if capas_cargadas:
        # Calcular extensión combinada
        extension = QgsRectangle()
        extension.setMinimal()
        
        for capa in capas_cargadas:
            if capa.extent().isNull():
                extension.combineExtentWith(capa.extent())
        
        # Aplicar zoom si la extensión es válida
        if not extension.isNull() and extension.isValid():
            canvas = iface.mapCanvas()
            canvas.setExtent(extension)
            canvas.refresh()
    
    return len(capas_cargadas)

# Uso del método:
from qgis.core import QgsCoordinateReferenceSystem

# Especificar directorio
directorio = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Ecositemas/Ecosistemas_por_Consejo'

# Opcional: definir CRS destino (ej. EPSG:3116 para Colombia)
crs_destino = QgsCoordinateReferenceSystem('EPSG:3116')

# Cargar capas
total = cargar_capas_directorio(directorio, crs_destino = crs_destino)
print(f"\nTotal de capas cargadas: {total}")



def aplicar_estilo_comun_a_capas(capas, campo, colores_por_valor, borde_color='0,0,0', grosor_borde=0.2):
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
        
        # Crear y asignar renderizador
        renderer = QgsCategorizedSymbolRenderer(campo, categories)
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


# Opción 3: Todas las capas de polígonos que comienzan con "Ecosistemas"
todas_capas = [
    capa for capa in QgsProject.instance().mapLayers().values() 
    if capa.name().startswith('Ecosistemas') and capa.geometryType() == QgsWkbTypes.PolygonGeometry
]


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


# Aplicar a capas por nombre
aplicar_estilo_comun_a_capas(
    capas = todas_capas,
    campo = 'ECOS_GENER',  # Campo común en todas las capas
    colores_por_valor = colores_eco,
    borde_color='0,0,0',    # Borde negro
    grosor_borde=0.3        # 0.3 mm de grosor
)