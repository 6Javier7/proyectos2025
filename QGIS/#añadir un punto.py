#añadir un punto

# Importar las clases necesarias
from qgis.core import (QgsPointXY, QgsCoordinateReferenceSystem, 
                      QgsCoordinateTransform, QgsProject)
from qgis.utils import iface


# --- PASO 1: Definir las coordenadas de entrada (WGS84) ---
# IMPORTANTE: QGIS espera primero Longitud (X) y luego Latitud (Y)
wgs84_longitud = -77.06863904540673
wgs84_latitud = 3.707302734669554

# Crear el punto en WGS84
punto_wgs84 = QgsPointXY(wgs84_longitud, wgs84_latitud)
print(f"Punto original (WGS84): {punto_wgs84.asWkt()}")

# --- PASO 2: Definir los sistemas de coordenadas (CRS) ---
# Sistema de origen: WGS84 (EPSG:4326)
crs_origen = QgsCoordinateReferenceSystem("EPSG:4326")
if not crs_origen.isValid():
    print("¡Error: CRS de origen no válido!")

# Sistema de destino 1: MAGNA-SIRGAS / Colombia Oeste (EPSG:3115)
# Las coordenadas que proporcionaste "magna-sirgas-oeste: 964840.94, 866862.95" corresponden a este sistema
crs_magna_oeste = QgsCoordinateReferenceSystem("EPSG:3115")
if not crs_magna_oeste.isValid():
    print("¡Error: CRS EPSG:3115 no válido!")

# Sistema de destino 2: MAGNA-SIRGAS / Origen Único Nacional (EPSG:9377)
# Las coordenadas "origen unico nacional: 4511636.83, 1933948.78" corresponden a este sistema
crs_origen_nacional = QgsCoordinateReferenceSystem("EPSG:9377")
if not crs_origen_nacional.isValid():
    print("¡Error: CRS EPSG:9377 no válido!")

# --- PASO 3: Crear las transformaciones ---
# Es importante usar QgsProject.instance() para respetar la configuración del proyecto [citation:6]
transform_oeste = QgsCoordinateTransform(crs_origen, crs_magna_oeste, QgsProject.instance())
transform_nacional = QgsCoordinateTransform(crs_origen, crs_origen_nacional, QgsProject.instance())

# --- PASO 4: Realizar las transformaciones ---
try:
    # Transformar a MAGNA-SIRGAS Oeste (EPSG:3115)
    punto_magna_oeste = transform_oeste.transform(punto_wgs84)
    print(f"\nTransformado a MAGNA-SIRGAS Oeste (EPSG:3115):")
    print(f"  X (Este): {punto_magna_oeste.x():.6f}")
    print(f"  Y (Norte): {punto_magna_oeste.y():.6f}")
    print(f"  (Tus coordenadas: 964840.9443027232, 866862.952355389)")

    # Transformar a Origen Único Nacional (EPSG:9377)
    punto_origen_nacional = transform_nacional.transform(punto_wgs84)
    print(f"\nTransformado a Origen Único Nacional (EPSG:9377):")
    print(f"  X (Este): {punto_origen_nacional.x():.6f}")
    print(f"  Y (Norte): {punto_origen_nacional.y():.6f}")
    print(f"  (Tus coordenadas: 4511636.833139184, 1933948.7876036286)")

except Exception as e:
    print(f"Error durante la transformación: {e}")

# --- PASO 5: (Opcional) Agregar el punto al mapa para verificación visual ---
# Crear una capa temporal con el punto transformado
capa_temporal = QgsVectorLayer("Point?crs=EPSG:9377", "Punto_Verificacion", "memory")
proveedor = capa_temporal.dataProvider()
feature = QgsFeature()
feature.setGeometry(QgsGeometry.fromPointXY(punto_origen_nacional))
proveedor.addFeatures([feature])
capa_temporal.updateExtents()

# Agregar la capa al proyecto
QgsProject.instance().addMapLayer(capa_temporal)
print("\n¡Punto agregado al mapa para verificación visual!")

# Opcional: Acercar la vista al punto
iface.mapCanvas().setExtent(capa_temporal.extent())
iface.mapCanvas().refresh()