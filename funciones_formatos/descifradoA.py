#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 00:27:07 2026

@author: javier
"""

#!/usr/bin/env python3
import string
import re

# Configurar alfabeto
mayus = string.ascii_uppercase[:13] + 'Ñ' + string.ascii_uppercase[13:]
minus = string.ascii_lowercase[:13] + 'ñ' + string.ascii_lowercase[13:]

def descifrar_a1z27(mensaje):
    """
    Descifra mensajes en código A1Z27.
    Preserva ESPACIOS y SIGNOS de puntuación.
    """
    def convertir_numero(num_match):
        num_str = num_match.group()
        num = int(num_str)
        
        if 1 <= num <= len(mayus):
            if num_str.islower():
                return minus[num-1]
            else:
                return mayus[num-1]
        return num_str
    
    # Paso 1: Convertir todos los números de 2 dígitos a letras
    mensaje = re.sub(r'\b\d{2}\b', convertir_numero, mensaje)
    
    # Paso 2: Eliminar SOLO los guiones que están entre números
    # Buscar patrones como "letra-guión-letra" y mantener el guión
    # Pero eliminar guiones restantes
    resultado = []
    i = 0
    
    while i < len(mensaje):
        # Si es un guión
        if mensaje[i] == '-':
            # Verificar contexto
            if i > 0 and i + 1 < len(mensaje):
                # Si está entre dos letras, mantenerlo (ej: "bi-dimensional")
                if mensaje[i-1].isalpha() and mensaje[i+1].isalpha():
                    resultado.append('-')
                # Si no, eliminarlo (era separador de números)
                i += 1
                continue
            else:
                # Guión al inicio o final, eliminarlo
                i += 1
                continue
        
        # Cualquier otro carácter
        resultado.append(mensaje[i])
        i += 1
    
    return ''.join(resultado)

# Ejemplos de uso
#no se puede colocar solo 3 debe colocar 03
if __name__ == "__main__":
    
    print("🔓 DESCIFRADOR A1Z27 (CON ESPACIOS Y SIGNOS)")
    print("=" * 50)
    
    
    # Interfaz interactiva
    print("\n" + "=" * 50)
    
    while True:
        msg = input("\n📩 Mensaje a descifrar (o Enter para salir): ").strip()
        if not msg:
            break
        
        print(f"✅ Resultado: '{descifrar_a1z27(msg)}'")