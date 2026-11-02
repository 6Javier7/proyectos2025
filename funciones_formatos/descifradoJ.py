#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 00:27:07 2026

@author: javier
"""

#!/usr/bin/env python3
import string

# Configurar alfabeto español (27 letras)
mayus = string.ascii_uppercase[:13] + 'Ñ' + string.ascii_uppercase[13:]
minus = string.ascii_lowercase[:13] + 'ñ' + string.ascii_lowercase[13:]

# Tabla de descifrado Atbash: del alfabeto invertido al normal
# (Atbash es simétrico, así que esta tabla también sirve para cifrar)
_TABLA_ATBASH_INV = str.maketrans(mayus[::-1] + minus[::-1], mayus + minus)


def descifrar_atbash(mensaje):
    """
    Descifra mensajes cifrados con Atbash (alfabeto español).

    Atbash es una sustitución simétrica: A↔Z, B↔Y, C↔X, ..., Ñ↔Ñ.
    Aplicarlo dos veces devuelve el texto original.

    - Las letras (mayúsculas y minúsculas) se invierten.
    - Los ESPACIOS, SIGNOS y DÍGITOS se mantienen tal cual.
    - Los acentos (á, é, í, ó, ú) no están en el alfabeto base, así que
      pasan intactos. Si el cifrado los transformó previamente, aquí no
      se recuperan; para eso habría que ampliar el alfabeto.
    """
    return mensaje.translate(_TABLA_ATBASH_INV)


# Ejemplos de uso
if __name__ == "__main__":

    print("🔓 DESCIFRADOR ATBASH (CON ESPACIOS Y SIGNOS)")
    print("=" * 50)

    # Demostración rápida de que funciona
    print("\n🧪 Prueba interna:")
    original = "Hola, ¿cómo estás? 2026"
    cifrado = descifrar_atbash(original)       # Atbash es simétrico
    recuperado = descifrar_atbash(cifrado)
    print(f"  Original : {original}")
    print(f"  Cifrado  : {cifrado}")
    print(f"  Recup.   : {recuperado}")
    assert recuperado == original, "❌ Algo falla en el descifrado"
    print("  ✅ Round-trip correcto")

    # Interfaz interactiva
    print("\n" + "=" * 50)

    while True:
        msg = input("\n📩 Mensaje a descifrar (o Enter para salir): ").strip()
        if not msg:
            break

        print(f"✅ Resultado: '{descifrar_atbash(msg)}'")