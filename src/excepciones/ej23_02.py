# Ejercicio 2.3.2
# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.


def pedir_num_positivo(msg) -> int:
    numero = None
    while numero == None:
        numero = input(msg)
        if validar_num_positivo(numero):
            return int(numero)
        else:
            print("**ERROR** Debes introducir un número entero positivo")
            numero = None


def validar_num_positivo(numero: str) -> bool:
    try:
        int(numero)
        return int(numero) > 0
    except ValueError:
        return False


def mostrar_impares(numero: int) -> str:
    serie_numeros = ""

    for i in range(1, numero):
        if i % 2 == 1:
            serie_numeros += f"{i}, "

    return serie_numeros[:-2]


def main():
    numero = pedir_num_positivo("Introduce un número entero positivo: ")
    print(mostrar_impares(numero))


if __name__ == "__main__":
    main()