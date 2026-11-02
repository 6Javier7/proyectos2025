#!/bin/bash

# Configuración
CSS_VIEJO="css/tjreport.css"
CSS_NUEVO="Modernizado/modern-theme.css"
EXTENSION_BAK=".bak"

echo "🔍 Buscando archivos HTML..."

for archivo in *.html; do
  if [ -f "$archivo" ]; then
    echo "📝 Procesando: $archivo"
    sed -i "${EXTENSION_BAK}" "s|${CSS_VIEJO}|${CSS_NUEVO}|g" "$archivo"
  fi
done

echo ""
echo "✅ Completado!"
echo "🗑️  Para eliminar backups: rm *${EXTENSION_BAK}"