def main():
    objetivo = int(input('Ingrese un numero: '))
    epsilon = 0.01
    paso = epsilon**2
    resultado = 0.0

    while abs(resultado**2 - objetivo) >= epsilon and resultado <= objetivo:
        resultado += paso

    if abs(resultado**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada de {objetivo}')
    else:
        print(f'La raiz cuadrada de {objetivo} es {resultado}')


if __name__ == '__main__':
    main()