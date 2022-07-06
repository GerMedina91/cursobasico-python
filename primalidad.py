import math


def es_primo(num):
    # Teorema de WIlson
    return math.factorial(num - 1) % num == (-1) % num


def run():
    numero = int(input("Ingresa un numero: "))
    if es_primo(numero):
        print("Es primo")
    else:
        print("No es primo")

if __name__ == '__main__':
    run()