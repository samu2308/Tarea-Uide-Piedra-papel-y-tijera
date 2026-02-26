# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 13:02:52 2026

@author: Samu
"""

import random

def elegir_computadora(opciones):
    return random.choice(opciones)


def elegir_jugador(opciones):
    jugador = input("Elige piedra, papel o tijera: ").lower()
    if jugador in opciones:
        return jugador
    else:
        return None