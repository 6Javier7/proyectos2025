#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 22:00:45 2026

@author: javier
"""


#!/usr/bin/env python3
import string

# Alfabeto español
mayus = string.ascii_uppercase[:13] + 'Ñ' + string.ascii_uppercase[13:]
minus = string.ascii_lowercase[:13] + 'ñ' + string.ascii_lowercase[13:]

# Cifrado Atbash
def atbash(txt):
    tabla = str.maketrans(mayus + minus, mayus[::-1] + minus[::-1])
    return txt.translate(tabla)

# Cifrado A1Z27 (MEJORADO - sin guiones extras)
def a1z27(txt):
    resultado = []
    
    for caracter in txt:
        if caracter in mayus:
            numero = f"{mayus.index(caracter)+1:02d}"
            resultado.append(numero)
        elif caracter in minus:
            numero = f"{minus.index(caracter)+1:02d}"
            resultado.append(numero)
        else:
            # Mantener espacios y signos tal cual
            resultado.append(caracter)
    
    # Unir números con guiones, mantener otros caracteres separados
    final = []
    i = 0
    
    while i < len(resultado):
        if resultado[i].isdigit():  # Es un número (01, 02, etc.)
            # Encontrar todos los números consecutivos
            numeros_grupo = [resultado[i]]
            i += 1
            while i < len(resultado) and resultado[i].isdigit():
                numeros_grupo.append(resultado[i])
                i += 1
            final.append("-".join(numeros_grupo))
        else:
            # No es número (espacio, signo, etc.)
            final.append(resultado[i])
            i += 1
    
    return " ".join(final)  # Usar espacio para separar grupos

# Programa principal
print("🔐 CIFRADOR (Atbash + A1Z27 con -)")
print("=" * 40)

while True:
    msg = input("\nMensaje: ").strip()
    if not msg or msg.lower() == "salir":
        break
    
    print(f"\nOriginal: {msg}")
    print(f"Atbash:   {atbash(msg)}")
    print(f"A1Z27:    {a1z27(msg)}")