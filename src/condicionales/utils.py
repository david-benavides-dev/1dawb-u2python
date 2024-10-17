from os import system, name

# Funcion para limpiar la consola
def clear():
    if name == 'nt':
        _ = system('cls')

# Funciones que solicita entero al usuario.
def pedir_num(msg) -> int:
    """
    
    """
    numero = None
    while numero == None:
        numero = input(msg)
        if validar_num(numero):
            return int(numero)
        else:
            print("**ERROR** Debes introducir un número")
            numero = None

# Función para validar si un número es entero.
def validar_num(numero: str) -> bool:
    """
    
    """
    try:
        int(numero)
        return True
    except ValueError:
        return False

# Función que solicita float al usuario.
def pedir_float(msg) -> float:
    """
    
    """
    numero = None
    while numero == None:
        numero = input(msg)
        if validar_float(numero):
            return float(numero)
        else:
            print("**ERROR** Debes introducir un número flotante.")
            numero = None

# Función para validar si un número es flotante.
def validar_float(numero: str) -> bool:
    """
    
    """
    try:
        float(numero)
        return True
    except ValueError:
        return False
    
# Función para "pausar" la ejecución de un programa hasta que el usuario pulse ENTER.
def pause():
    input("Pulsa ENTER para continuar...")