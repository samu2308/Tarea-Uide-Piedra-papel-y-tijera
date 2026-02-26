# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 13:00:29 2026

@author: Samu
"""

def obtener_opciones():
    return ("piedra", "papel", "tijera")


def obtener_reglas():
    return {
        "piedra": "tijera",
        "papel": "piedra",
        "tijera": "papel"
    }