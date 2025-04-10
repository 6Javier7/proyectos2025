#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 20:35:57 2025

@author: javiermontanochiriboga
"""

import csv
import os
from datetime import datetime

def stakeholdereg():
    num_riskreg = int(input('¿Cuántas personas involucradas encontraste encontraste hoy? '))
    # Revisar desde donde empezara a el nuevo id.
    file_exists = os.path.isfile('stakeholdeReg.csv')
    if file_exists:
        with open('stakeholdeReg.csv', 'r', encoding='utf-8') as arch:
            interx = csv.DictReader(arch)
            ids_exis = [int(fil['ID']) for fil in interx if fil['ID'].isdigit()]
            if ids_exis:
                sig_id = max(ids_exis) + 1
            else:
                sig_id = 1

    with open('stakeholdeReg.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # Escribe headers si el archivo está vacío
        if csvfile.tell() == 0:
            writer.writerow(["ID", "Fecha de hallazgo", "Nombre", "Cargo", "Rol", "Tipo", "Interes", "Poder", "Tipo"])

        for counts in range(sig_id, num_riskreg + sig_id):
            print(f'\n--- Involucrade #{counts} ---')
            writer.writerow([
                counts,
                datetime.now().strftime('%Y-%m-%d'),
                input('Nombre de involucrade: '),
                input('Cargo: '),
                input('Rol en el proyecto: '),
                input('Tipo I(Inconciente), R(Resistente), N(Neutral), S(Sopoerte), L(Liderazgo): '),
                input('Interes A(Alto), M(Medio), B(Bajo): '),
                input('Poder: Es la capacidad que tienen para influir en el resultado A(Alto), M(Medio), B(Bajo): '),
                input('Legitimidad: El nivel de autoridad que tiene A(Alto), M(Medio), B(Bajo): '),
                input('Urgencia: Es la necesidad que tiene de actuar de manera inmediata A(Alto), M(Medio), B(Bajo): '),
                
            ])
    
    print(f'\n✅ Datos guardados en stakeholdeReg.csv ')

stakeholdereg()