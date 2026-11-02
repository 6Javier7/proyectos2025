#whitebox install

import os
from qgis.core import QgsSettings, QgsApplication
from processing.core.Processing import Processing

# Ruta EXACTA a tu ejecutable (la que ya funciona)
wbt_path = "/Applications/WhiteboxTools_darwin_m_series/WBT/whitebox_tools"

print("="*60)
print("🔧 CONFIGURACIÓN FINAL (MÉTODO CORREGIDO)")
print("="*60)

# PASO 1: Verificar que el archivo existe
if not os.path.exists(wbt_path):
    print(f"❌ Error: No se encuentra el archivo en {wbt_path}")
else:
    print(f"✅ Ejecutable verificado: {wbt_path}")

    # PASO 2: Guardar la ruta en la configuración de QGIS
    print("\n⚙️ Guardando ruta en configuración de QGIS...")

    # Usar QgsSettings (funciona en todas las versiones)
    settings = QgsSettings()
    settings.setValue("Processing/Configuration/WBT_EXECUTABLE_PATH", wbt_path)
    print("✅ Ruta guardada en configuración.")

    # PASO 3: Forzar la recarga de proveedores
    print("\n🔄 Recargando proveedores de procesamiento...")
    Processing.initialize()
    print("✅ Proveedores recargados.")

    # PASO 4: Verificar usando el método correcto (processingRegistry)
    print("\n📊 Verificando proveedores disponibles...")
    
    # MÉTODO CORRECTO: Usar processingRegistry
    registry = QgsApplication.processingRegistry()
    
    # Listar todos los proveedores
    providers = registry.providers()
    print(f"   Total proveedores: {len(providers)}")
    
    # Buscar proveedores que contengan "whitebox"
    wbt_providers = [p for p in providers if "whitebox" in p.name().lower() or "whitebox" in p.id().lower()]
    
    if wbt_providers:
        print(f"✅ Proveedor Whitebox encontrado:")
        for p in wbt_providers:
            print(f"   • Nombre: {p.name()}")
            print(f"   • ID: {p.id()}")
            
            # Listar algunos algoritmos
            algs = p.algorithms()
            print(f"   • Algoritmos cargados: {len(algs)}")
            if len(algs) > 0:
                print(f"\n📋 Primeros 5 algoritmos:")
                for alg in algs[:5]:
                    print(f"   • {alg.name()}")
    else:
        print("❌ No se encontró proveedor Whitebox")
        print("\n   Proveedores disponibles:")
        for p in providers[:10]:  # Mostrar primeros 10
            print(f"   • {p.name()} (ID: {p.id()})")

    # PASO 5: Intentar activar el proveedor manualmente si no aparece
    if not wbt_providers:
        print("\n🔄 Intentando activación manual del proveedor...")
        try:
            # Forzar la carga del plugin WhiteboxTools
            from wbt_for_qgis.wbtprovider import WbtProvider
            whitebox_provider = WbtProvider()
            registry.addProvider(whitebox_provider)
            print("✅ Proveedor Whitebox añadido manualmente")
        except ImportError:
            print("⚠️ No se pudo cargar el módulo wbt_for_qgis")
            print("   El plugin WhiteboxTools for QGIS puede no estar instalado")

print("\n" + "="*60)
print("✅ CONFIGURACIÓN COMPLETADA")
print("="*60)
print("\n🔍 VERIFICACIÓN MANUAL:")
print("1. Abre la Caja de Herramientas de Procesamiento (Ctrl+Alt+T)")
print("2. En la barra de búsqueda, escribe 'whitebox'")
print("3. Si ves herramientas como 'LineSimplification', ¡todo está listo!")
print("4. Si no ves herramientas, reinicia QGIS completamente")
print("5. La ruta configurada es:", wbt_path)