import sys


sys.path.append('../')
from aproximacion import main as aprox
from busqueda_binaria import main as binar
from functiones import main as func
from palindromo import run as pal


def main():
    eleccion = int(input("""
    Bienvenido al programa de eleccion. Ingrese el programa que quiere ejecutar:
    1 - Aproximacion
    2 - Busqueda binaria
    3 - funciones
    4 - Palindromo
    """))

    while True:
        if eleccion == 1:
            aprox()
            break
        elif eleccion == 2:
            binar()
            break
        elif eleccion == 3:
            func()
            break
        elif eleccion == 4:
            pal()
            break
        else:
            eleccion = input('Valor incorrecto, ingrese nuevamente: ')


    print('Gracias por usar el programa')
    exit()


if __name__ == '__main__':
    main()