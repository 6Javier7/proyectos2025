#Whitebox
# Importar las librerías necesarias (¡lo más importante!)
import time
from qgis import processing
import os
import subprocess

#📋 Buscando algoritmos de simplificación...
#
#Total encontrados: 0
#
#📋 Primeros 20 algoritmos disponibles:
#   1. wbt:AbsoluteValue
#   2. wbt:AccumulationCurvature
#   3. wbt:AdaptiveFilter
#   4. wbt:Add
#   5. wbt:AddPointCoordinatesToTable
#   6. wbt:AggregateRaster
#   7. wbt:And
#   8. wbt:Anova
#   9. wbt:ArcCos
#   10. wbt:ArcSin
#   11. wbt:ArcTan
#   12. wbt:Arcosh
#   13. wbt:Arsinh
#   14. wbt:Artanh
#   15. wbt:AsciiToLas
#   16. wbt:Aspect
#   17. wbt:AssessRoute
#   18. wbt:Atan2
#   19. wbt:AttributeCorrelation
#   20. wbt:AttributeCorrelationNeighbourhoodAnalysis

from qgis.core import QgsApplication

# Obtener el proveedor Whitebox
registry = QgsApplication.processingRegistry()
wbt_provider = registry.providerById("wbt")

if wbt_provider:
    print(f"✅ Proveedor Whitebox encontrado: {wbt_provider.name()}")
    print(f"📊 Total de algoritmos: {len(wbt_provider.algorithms())}")
    print("\n" + "="*80)
    print("📋 LISTA COMPLETA DE ALGORITMOS WHITEBOX:")
    print("="*80)
    
    # Mostrar TODOS los algoritmos numerados
    for i, alg in enumerate(wbt_provider.algorithms(), 1):
        print(f"{i:4d}. {alg.id()}")
        
        # Opcional: mostrar también el nombre descriptivo
        # print(f"{i:4d}. {alg.id()} - {alg.name()}")
        
        # Pequeña pausa cada 50 líneas para no saturar la consola
        if i % 50 == 0:
            input(f"\n📌 Mostrados {i} algoritmos. Presiona Enter para continuar...")
    
    print(f"\n✅ Total mostrados: {len(wbt_provider.algorithms())} algoritmos")
else:
    print("❌ No se encontró el proveedor Whitebox")



import time
from qgis import processing
from qgis.core import QgsProject

try:
    capa = reclayer

except NameError:
    capa = iface.activeLayer()
    print("ℹ️ Usando la capa activa seleccionada.")

tolerancia = 0.001
print("="*60)
print("🚀 PROCESANDO CAPA CON WHITEBOX")
print("="*60)

# ==================================================
# PASO 1: Buscar si existe un algoritmo de simplificación
# ==================================================
print("\n1️⃣  Buscando algoritmo de simplificación...")
from qgis.core import QgsApplication
registry = QgsApplication.processingRegistry()
wbt_provider = registry.providerById("wbt")

algs_simplify = []
if wbt_provider:
    for alg in wbt_provider.algorithms():
        if "simplif" in alg.name().lower():
            algs_simplify.append(alg.id())
            print(f"   🔹 {alg.id()} - {alg.name()}")

if algs_simplify:
    print(f"   ✅ Algoritmos de simplificación encontrados: {algs_simplify}")
    # Usar el primero encontrado
    alg_simplify = algs_simplify[0]
else:
    print("   ⚠️ No se encontró algoritmo específico de simplificación.")
    print("   Se omitirá el paso de simplificación por ahora.")
    alg_simplify = None

# ==================================================
# PASO 2: Simplificar (si hay algoritmo)
# ==================================================
if alg_simplify:
    print(f"\n2️⃣  Simplificando geometrías con {alg_simplify}...")
    t1 = time.time()
    
    simplificadas = processing.run(alg_simplify, {
        'INPUT': capa,
        'TOLERANCE': tolerancia,
        'METHOD': 0,
        'OUTPUT': 'memory:'
    })['OUTPUT']
    
    v_originales = 4_213_873
    v_nuevos = 0
    for feat in simplificadas.getFeatures():
        geom = feat.geometry()
        if geom:
            v_nuevos += geom.constGet().nCoordinates()
    
    reduccion = (1 - v_nuevos/v_originales) * 100
    print(f"   ✅ Vértices: {v_originales:,} → {v_nuevos:,}")
    print(f"   📉 Reducción: {reduccion:.1f}%")
    print(f"   ⏱️  Tiempo: {time.time()-t1:.1f}s")
    
    QgsProject.instance().addMapLayer(simplificadas)
    capa_para_singlepart = simplificadas
else:
    capa_para_singlepart = capa
    print("\n⏩ Omitiendo simplificación, solo se convertirá a singlepart.")

# ==================================================
# PASO 3: Convertir a Singlepart (¡CON NOMBRE VERIFICADO!)
# ==================================================
print("\n3️⃣  Convirtiendo a Singlepart con wbt:MultiPartToSinglePart...")
t2 = time.time()

try:
    singlepart = processing.run("wbt:MultiPartToSinglePart", {
        'INPUT': capa_para_singlepart,
        'EXCLUDE_HOLES': True,
        'OUTPUT': 'memory:'
    })['OUTPUT']
    
    print(f"   ✅ Features originales: {capa_para_singlepart.featureCount()}")
    print(f"   ✅ Features después: {singlepart.featureCount()}")
    print(f"   ⏱️  Tiempo: {time.time()-t2:.1f}s")
    
    # Añadir la capa final
    QgsProject.instance().addMapLayer(singlepart)
    
except Exception as e:
    print(f"   ❌ Error: {e}")

print("\n" + "="*60)
print("✅ PROCESO COMPLETADO")
print("="*60)
print("\n📌 NOTAS:")
print("• La capa final (singlepart) se ha añadido al proyecto.")
print("• Si la simplificación no se realizó, puedes investigar:")
print("  - Los algoritmos disponibles están en la lista que obtuviste.")
print("  - Busca en la documentación de WhiteboxTools el nombre exacto.")