#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 20:31:55 2025

@author: javiermontanochiriboga
"""

import csv
import os
from datetime import datetime

def changes():
    num_changes = int(input('¿Cuántos cambios encontraste hoy? '))
    # Revisar desde donde empezara a el nuevo id.
    file_exists = os.path.isfile('changelog.csv')
    if file_exists:
        with open('changelog.csv', 'r', encoding='utf-8') as arch:
            interx = csv.DictReader(arch)
            ids_exis = [int(fil['ID']) for fil in interx if fil['ID'].isdigit()]
            if ids_exis:
                sig_id = max(ids_exis) + 1
            else:
                sig_id = 1
    
    with open('changelog.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # Escribe headers si el archivo está vacío
        if csvfile.tell() == 0:
            writer.writerow(["ID", "Fecha de envio", "Solicitado por", "Nombre", "Descripción", "Impacto", "Estado", "Tipo"])
        
        for count in range(sig_id, num_changes + sig_id):
            print(f'\n--- Cambio #{count} ---')
            writer.writerow([
                count,
                datetime.now().strftime('%Y-%m-%d'),
                input('Solicitado por: '),
                input('Nombre del cambio: '),
                input('Descripción: '),
                input('Impacto en costo/tiempo de 1 a 5: '),
                input('Estado (P(Pendiente)/A(Aprovado)/R(Rechazado)): ').capitalize(),
                input('Tipo (T(Tendencia)/S(Solicitud)): ').capitalize()
            ])
    
    print(f'\n✅ Datos guardados en changelog.csv ')

changes()