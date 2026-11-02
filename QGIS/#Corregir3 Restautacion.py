#Corregir3

# ============================================
# SCRIPT CORREGIDO - Procesamiento de capas
# ============================================

# CONFIGURACIÓN
capa_path = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/Restauracion/Corregidos Restauracion.gpkg'
output_base = '/Volumes/Disco A/Javier/Cartografia/Mapas/Ecosistemas y comunidades/Restauracion/Corregidos Restauracion2.gpkg'

# 1. CARGAR CAPA ORIGINAL
print("\n📂 Cargando capa original...")
capa_original = QgsVectorLayer(capa_path, 'capa_original', "ogr")


# 2. PRIMERO REPROYECTAR (es mejor hacerlo al inicio)
print("\n🔄 1/2: Reproyectando a WGS84 (EPSG:4326)...")
output_grados = output_base.replace('.gpkg', '_1.gpkg')

grados = processing.run("native:reprojectlayer", {
    'INPUT': capa_original,
    'TARGET_CRS': 'EPSG:4326',
    'OUTPUT': output_grados
})['OUTPUT']

print(f"✅ Reproyección completada: {output_grados}")

# 3. LUEGO SIMPLIFICAR (ya en grados)
print("\n🔄 2/2: Simplificando geometrías...")

# La tolerancia en grados es diferente que en metros
# 20 grados es ENORME (unos 2200 km). Probablemente quieras algo mucho menor.
# Para simplificar suavemente en grados: 0.001 o 0.0001
tolerancia_grados = 0.001  # Ajusta según necesites

simplificado = processing.run("native:simplifygeometries", {
    'INPUT': grados,
    'METHOD': 0,  # 0 = Distancia (Ramirez-Douglas-Peucker)
    'TOLERANCE': tolerancia_grados,
    'OUTPUT': output_base
})['OUTPUT']

print(f"✅ Simplificación completada: {output_base}")

# 4. CARGAR Y VERIFICAR RESULTADO FINAL
print("\n📊 Cargando capa final...")
capa_final = QgsVectorLayer(output_base, 'capa_final', "ogr")

if capa_final.isValid():
    print(f"✅ PROCESO COMPLETADO EXITOSAMENTE")
    print(f"📌 Features finales: {capa_final.featureCount()}")
    print(f"📌 CRS final: {capa_final.crs().authid()}")
    
    # Opcional: añadir al proyecto
    QgsProject.instance().addMapLayer(capa_final)
    print("✅ Capa añadida al proyecto")
    
    # Mostrar diferencias
    print(f"\n📊 Resumen:")
    print(f"  - Original: {capa_original.featureCount()} features")
    print(f"  - Final:    {capa_final.featureCount()} features")
    print(f"  - CRS:      {capa_final.crs().authid()}")
else:
    print("❌ Error: No se pudo cargar la capa final")


