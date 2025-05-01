#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 13:19:20 2025

@author: javiermontanochiriboga
"""

# Configuración de colores por categoría
colores_prioridad = {
    'omisiones,urgentes, naturales y oportunas': QColor(255, 0, 0),       # Rojo
    'omisiones,urgentes,naturales y sin oportunidad': QColor(255, 50, 0), # Naranja-rojizo
    'omisiones, urgentes y seminaturales': QColor(255, 100, 0),           # Naranja
    'omisiones sin urgencia': QColor(255, 150, 0),                        # Naranja claro
    'alta insuficiencia y urgente': QColor(255, 200, 0),                  # Amarillo-naranja
    'alta insuficiencia sin urgencia': QColor(255, 225, 0),               # Amarillo claro
    'baja insuficiencia y urgente': QColor(255, 250, 0),                  # Amarillo-naranja claro
    'baja insuficiencia y sin urgencia': QColor(255, 255, 0)              # Amarillo puro
}

def aplicar_estilo_prioridad(capa, campo, colores_dict):
    """Aplica estilo categorizado a la capa de prioridad"""
    if not capa.isValid():
        print("Error: Capa no válida")
        return False
    
    if campo not in [field.name() for field in capa.fields()]:
        print(f"Error: Campo '{campo}' no encontrado")
        return False
    
    # Crear categorías
    categories = []
    for valor, color in colores_dict.items():
        # Crear símbolo (ajustar según tipo de geometría)
        if capa.geometryType() == QgsWkbTypes.PolygonGeometry:
            symbol = QgsFillSymbol.createSimple({
                'color': color.name(),
                'color_border': '0,0,0',  # Borde negro
                'width_border': '0.2'      # Grosor de borde
            })
        else:
            symbol = QgsSymbol.defaultSymbol(capa.geometryType())
            symbol.setColor(color)
        
        # Crear categoría
        category = QgsRendererCategory(valor, symbol, str(valor))
        categories.append(category)
    
    # Aplicar renderizador
    renderer = QgsCategorizedSymbolRenderer(campo, categories)
    capa.setRenderer(renderer)
    capa.triggerRepaint()
    
    # Actualizar la vista
    iface.layerTreeView().refreshLayerSymbology(capa.id())
    iface.mapCanvas().refresh()
    
    print(f"Estilo aplicado a la capa: {capa.name()}")
    return True

# Cargar la capa de prioridad
priori_path = '/Volumes/Disco J/Mapas/Ecosistemas y comunidades/Prioridad_Conpes/PCN_CONPES.shp'
#layerpri = QgsVectorLayer(priori_path, 'Prioridades PDET', "ogr")
layerpri = iface.addVectorLayer(priori_path, 'Prioridades PDET', "ogr")

if not layerpri.isValid():
    raise Exception("No se pudo cargar la capa de prioridad")

# Aplicar el estilo (asumiendo que el campo se llama 'categoria')
campo_categorias = 'PRIORIDAD'  # Cambiar por el nombre real del campo en tus datos
if not aplicar_estilo_prioridad(layerpri, campo_categorias, colores_prioridad):
    print("No se pudo aplicar el estilo")

# Añadir al proyecto si no está ya
if not QgsProject.instance().mapLayersByName(layerpri.name()):
    QgsProject.instance().addMapLayer(layerpri)