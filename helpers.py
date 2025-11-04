import re
import os
import platform


def limpiar_pantalla():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')


def leer_texto(longitud_min=0, longitud_max=100, mensaje=None):
    print(mensaje) if mensaje else None
    while True:
        texto = input("> ")
        if len(texto) >= longitud_min and len(texto) <= longitud_max:
            return texto


def dni_valido(dni, lista):
    # Acepta 8 dígitos, con o sin puntos como separadores
    patron = r'^\d{1,2}\.?\d{3}\.?\d{3}$'

    if not re.match(patron, dni):
        print("DNI incorrecto. Debe tener el formato 42.910.032 o 42910032.")
        return False

    # Eliminar los puntos para comparar DNIs de forma uniforme
    dni_limpio = dni.replace('.', '')

    for cliente in lista:
        if cliente.dni.replace('.', '') == dni_limpio:
            print("DNI utilizado por otro cliente.")
            return False

    return True

