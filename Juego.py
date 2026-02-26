# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 13:03:58 2026

@author: Samu
"""
from datos import obtener_opciones, obtener_reglas
from entradas import elegir_computadora, elegir_jugador
from logica import determinar_resultado


def jugar_otra_vez():
    respuesta = input("¿Jugar otra vez? (si/no): ").lower()
    return respuesta == "si"


def ejecutar_juego():
    opciones = obtener_opciones()
    reglas = obtener_reglas()

    while True:
        computadora = elegir_computadora(opciones)
        jugador = elegir_jugador(opciones)

        if jugador is None:
            print("Opción inválida. Intenta nuevamente.")
            continue

        print(f"Jugador: {jugador}")
        print(f"Computadora: {computadora}")
        print(determinar_resultado(jugador, computadora, reglas))

        if not jugar_otra_vez():
            print("Gracias por jugar ")
            break


ejecutar_juego()
