#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 20:35:57 2025

@author: javiermontanochiriboga
"""

import csv
from datetime import datetime

def stakeholdereg():
    num_riskreg = int(input('¿Cuántas personas involucradas encontraste encontraste hoy? '))
    
    with open('stakeholdeReg.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # Escribe headers si el archivo está vacío
        if csvfile.tell() == 0:
            writer.writerow(["ID", "Fecha de hallazgo", "Nombre", "Cargo", "Rol", "Tipo", "Interes", "Poder", "Tipo"])
        
        for count in range(1, num_riskreg + 1):
            print(f'\n--- Involucrade #{count} ---')
            writer.writerow([
                count,
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