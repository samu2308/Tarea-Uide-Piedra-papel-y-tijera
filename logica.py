# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 13:03:24 2026

@author: Samu
"""
def determinar_resultado(jugador, computadora, reglas):
    if jugador == computadora:
        return "Empate"
    elif reglas[jugador] == computadora:
        return "Ganaste, bien manito"
    else:
        return "Perdiste, cha mangos"