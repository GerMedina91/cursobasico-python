def nombre_completo(nombre, apellido, inverso=False):
    """ Concatena el nombre y apellido de una persona

    str nombre Nombre de la persona

    str apellido Apellido de la persona

    bool inverso Orden en el que se va a concatenar
    """
    if inverso:
        return f'{apellido} {nombre}'
    else:
        return f'{nombre} {apellido}'


def main():
    print('Ingrese nombre y apellido: ')
    nombre = input('Nombre: ')
    apellido = input('Apellido: ')
    
    print(nombre_completo(nombre, apellido))
    print(nombre_completo(nombre, apellido, True))
    print(nombre_completo(apellido=apellido, nombre=nombre))


if __name__ == '__main__':
    main()