# ============================================
# 3. LIMPIAR GEOMETRÍAS CON BUFFER 0
# ============================================

capa = QgsProject.instance().mapLayersByName('Corregidos Recuperacion2 — Corregidos Recuperacion_procesado')[0]


import time

print("⏱️ Midiendo tiempos de procesamiento...")

# Medir tiempo de buffer
start = time.time()


print("\n" + "="*50)
print("🧹 LIMPIANDO GEOMETRÍAS")
print("="*50)

# Identificar features inválidas primero
invalidas = []
for feat in capa.getFeatures():
    if not feat.geometry().isGeosValid():
        invalidas.append(feat.id())

if invalidas:
    # Seleccionar solo las inválidas
    capa.selectByIds(invalidas)
    
params_buffer = {
    'INPUT': capa,
    'DISTANCE': 0,
    'SEGMENTS': 5,
    'END_CAP_STYLE': 0,
    'JOIN_STYLE': 0,
    'MITER_LIMIT': 2,
    'DISSOLVE': False,
    'OUTPUT': 'memory:Corregidos Recuperacion2'
}

capa = processing.run("native:buffer", params_buffer)['OUTPUT']
print(f"✅ Geometrías limpiadas con buffer 0")
#print(f"- Features originales: {capa.featureCount()}")
#print(f"- Features limpias: {capa_limpio.featureCount()}")

#Añadir al proyecto
QgsProject.instance().addMapLayer(capa)
