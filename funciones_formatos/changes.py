#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 20:31:55 2025

@author: javiermontanochiriboga
"""

import csv
from datetime import datetime

def changes():
    num_changes = int(input('¿Cuántos cambios encontraste hoy? '))
    
    with open('changelog.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # Escribe headers si el archivo está vacío
        if csvfile.tell() == 0:
            writer.writerow(["ID", "Fecha de envio", "Solicitado por", "Nombre", "Descripción", "Impacto", "Estado", "Tipo"])
        
        for count in range(1, num_changes + 1):
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