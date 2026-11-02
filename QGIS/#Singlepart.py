#Singlepart

import time
from qgis import processing
from qgis.core import QgsProject
vertices = 4_213_873

# --- CONFIGURACIÓN ---
capa = QgsProject.instance().mapLayersByName('recuperacion')[0]  # O usa el nombre específico si prefieres

tolerancia = 0.005  # Ajusta según necesites

print("="*60)
print("🛠️  PROCESAMIENTO CON HERRAMIENTAS NATIVAS")
print("="*60)

# ==================================================
# PASO 1: Verificar que existe la capa
# ==================================================
if not capa:
    print("❌ No hay capa activa seleccionada")
    exit()

print(f"\n📋 Capa original: {capa.name()}")
print(f"   Features: {capa.featureCount()}")
print(f"   CRS: {capa.crs().authid()}")

# ==================================================
# PASO 2: SIMPLIFICAR GEOMETRÍAS (NATIVO)
# ==================================================
print(f"\n2️⃣  Simplificando geometrías con native:simplifygeometries...")
t1 = time.time()

simplificadas = processing.run("native:simplifygeometries", {
    'INPUT': capa,
    'METHOD': 0,  # 0 = Douglas-Peucker (el mismo que Whitebox)
    'TOLERANCE': tolerancia,
    'OUTPUT': 'memory:'
})['OUTPUT']

# Calcular reducción de vértices
v_originales = vertices  # De tu diagnóstico (ajusta si quieres calcularlo dinámicamente)
v_nuevos = 0
for feat in simplificadas.getFeatures():
    geom = feat.geometry()
    if geom:
        v_nuevos += geom.constGet().nCoordinates()

reduccion = (1 - v_nuevos/v_originales) * 100
print(f"   ✅ Vértices: {v_originales:,} → {v_nuevos:,}")
print(f"   📉 Reducción: {reduccion:.1f}%")
print(f"   ⏱️  Tiempo: {time.time()-t1:.1f}s")

# Añadir la capa simplificada al proyecto (opcional)
QgsProject.instance().addMapLayer(simplificadas)
capa_para_singlepart = simplificadas

# ==================================================
# RESUMEN FINAL
# ==================================================
print("\n" + "="*60)
print("✅ PROCESO COMPLETADO")
print("="*60)
print("\n📌 NOTAS:")
print(f"• Capa simplificada: {simplificadas.name()} ({simplificadas.featureCount()} features)")
print(f"• Tolerancia usada: {tolerancia}")
print("• Ya puedes usar estas capas para clip, buffer u otros análisis")
print("\n💡 Si necesitas calcular los vértices exactos antes de simplificar:")
print("   v_reales = 0")
print("   for feat in capa.getFeatures():")
print("       geom = feat.geometry()")
print("       if geom: v_reales += geom.constGet().nCoordinates()")
print("   print(f'Vértices reales: {v_reales:,}')")