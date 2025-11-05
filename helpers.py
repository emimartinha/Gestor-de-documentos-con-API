# Importaciones necesarias para las funciones de utilidad
import re
import os
import platform


def limpiar_pantalla():
    """Limpia la pantalla de la terminal según el sistema operativo.
    Utiliza 'cls' para Windows y 'clear' para Unix/Linux."""
    os.system('cls') if platform.system() == "Windows" else os.system('clear')


def leer_texto(longitud_min=0, longitud_max=100, mensaje=None):
    """Lee y valida entrada de texto del usuario.
    
    Args:
        longitud_min (int): Longitud mínima permitida para el texto
        longitud_max (int): Longitud máxima permitida para el texto
        mensaje (str): Mensaje opcional para mostrar antes de la entrada
        
    Returns:
        str: Texto validado ingresado por el usuario
    """
    print(mensaje) if mensaje else None
    while True:
        texto = input("> ")
        if len(texto) >= longitud_min and len(texto) <= longitud_max:
            return texto


def dni_valido(dni, lista):
    """Valida el formato del DNI y verifica que no esté duplicado.
    
    Args:
        dni (str): DNI a validar en formato XX.XXX.XXX o XXXXXXXX
        lista (list): Lista de clientes para verificar duplicados
        
    Returns:
        bool: True si el DNI es válido y no está duplicado, False en caso contrario
    """
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
