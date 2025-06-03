#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 17:04:57 2025

@author: javiermontanochiriboga
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 11:04:05 2025

@author: javiermontanochiriboga
"""

from qgis.core import (
    QgsCategorizedSymbolRenderer,
    QgsRendererCategory,
    QgsFillSymbol,
    QgsSymbol,
    QgsVectorLayer
)
from qgis.PyQt.QtGui import QColor

from qgis.core import QgsProject  # Importación necesaria

# Obtener la instancia del proyecto actual
project = QgsProject.instance()

def eliminar_capas_por_nombre(patron='Coberturas'):
    """
    Elimina capas que contengan un texto específico en su nombre
    
    Args:
        patron (str): Texto a buscar en los nombres de capa (no sensible a mayúsculas)
    """
    # Lista para almacenar los IDs de capas a eliminar
    capas_a_eliminar = []
    
    # Buscar capas que coincidan con el patrón
    for layer_id, layer in project.mapLayers().items():
        if patron.lower() in layer.name().lower():
            capas_a_eliminar.append(layer_id)
    
    # Eliminar las capas encontradas
    for layer_id in capas_a_eliminar:
        project.removeMapLayer(layer_id)
    
    # Mostrar resumen
    print(f"Se eliminaron {len(capas_a_eliminar)} capas que contenían '{patron}' en su nombre")
    print(f"Capas restantes en el proyecto: {len(project.mapLayers())}")

# Ejecutar la función
eliminar_capas_por_nombre('Coberturas')


def cargar_capas_directorio(directorio, formatos = None, crs_destino = None, campo_clasificacion='nivel_3'):
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
        capas_cargadas = []
    
    for root, dirs, files in os.walk(directorio):
        for file in files:
            if any(file.lower().endswith(ext) for ext in formatos):
                ruta_completa = os.path.join(root, file)
                nombre_capa = os.path.splitext(file)[0]
                
                # Cargar capa
                capa = QgsVectorLayer(ruta_completa, nombre_capa, 'ogr')
                
                if not capa.isValid():
                    print(f"✗ Error al cargar {file}")
                    continue
                
                # Verificar si el campo de clasificación existe
                if campo_clasificacion not in [field.name() for field in capa.fields()]:
                    print(f"✗ Campo '{campo_clasificacion}' no encontrado en {nombre_capa}")
                    continue
                
                # Solo aplicar estilo a capas de polígonos
                if capa.geometryType() == QgsWkbTypes.PolygonGeometry:
                    # Crear categorías para el renderizador
                    categories = []
                    for valor, color_rgb in colores_cov.items():
                        # Crear símbolo de relleno
                        symbol = QgsFillSymbol.createSimple({
                            'color': f'{color_rgb[0]},{color_rgb[1]},{color_rgb[2]}',
                            'color_border': '0,0,0',  # Borde negro
                            'width_border': '0.3'      # Grosor de borde
                        })
                        # Crear categoría
                        category = QgsRendererCategory(valor, symbol, str(valor))
                        categories.append(category)
                    
                    # Crear y asignar renderizador
                    renderer = QgsCategorizedSymbolRenderer(campo_clasificacion, categories)
                    capa.setRenderer(renderer)
                    capa.triggerRepaint()
                    
                    # Guardar estilo como predeterminado para esta capa
                    capa.saveDefaultStyle()
                
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
directorio = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Coberturas Vegetales/Coberturas_por_Municipio'

# Opcional: definir CRS destino (ej. EPSG:3116/9377 para Colombia)
crs_destino = QgsCoordinateReferenceSystem('EPSG:9377')

# Cargar capas
total = cargar_capas_directorio(directorio, crs_destino = crs_destino)
print(f"\nTotal de capas cargadas: {total}")



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


# Opción 3: Todas las capas de polígonos que comienzan con "Coberturas"
todas_capas = [
    capa for capa in QgsProject.instance().mapLayers().values() 
    if capa.name().startswith('Coberturas') and capa.geometryType() == QgsWkbTypes.PolygonGeometry
]


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


# Aplicar a capas por nombre
aplicar_estilo_comun_a_capas(
    capas = todas_capas,
    campo = 'nivel_3',  # Campo común en todas las capas
    colores_por_valor = colores_cov,
    borde_color='0,0,0',    # Borde negro
    grosor_borde=0.3        # 0.3 mm de grosor
)


# Opción 1: Guardar estilo predeterminado para TODAS las capas del proyecto
for capa in QgsProject.instance().mapLayers().values():
    capa.saveDefaultStyle()  # Guarda el estilo actual como predeterminado PARA ESA CAPA
    print(f"Estilo guardado como predeterminado para: {capa.name()}")

