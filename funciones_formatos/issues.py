#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 20:33:19 2025

@author: javiermontanochiriboga
@coauthor: andreymch
"""

import csv
import os
from datetime import datetime

def issues():
    num_issues = int(input('¿Cuántos issuues encontraste hoy? '))
    # Revisar desde donde empezara a el nuevo id.
    file_exists = os.path.isfile('issuelog.csv')
    if file_exists:
        with open('issuelog.csv', 'r', encoding='utf-8') as arch:
            interx = csv.DictReader(arch)
            ids_exis = [int(fil['ID']) for fil in interx if fil['ID'].isdigit()]
            if ids_exis:
                sig_id = max(ids_exis) + 1
    else:
        sig_id = 1
    
    with open('issuelog.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # Escribe headers si el archivo está vacío
        if csvfile.tell() == 0:
            writer.writerow(["ID", "Fecha de envio", "Prioridad", "Asignada", "Descripción", "Impacto", "Estado"])
        
        for count in range(sig_id, num_issues + sig_id):
            print(f'\n--- Issue #{count} ---')
            writer.writerow([
                count,
                datetime.now().strftime('%Y-%m-%d'),
                input('Prioridad (A(Alta), M(Media), B(Baja): '),
                input('Asignada a: '),
                input('Descripción: '),
                input('Impacto costo/tiempo de 1 a 5: '),
                input('Estado (P(Pendiente)/A(Aprovado)/R(Rechazado)): ').capitalize()

            ])
    
    print(f'\n✅ Datos guardados en issuelog.csv ')

issues()