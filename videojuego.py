import secrets


def run():
    num_com = secrets.randbelow(100)
    num_pj = int(input('Ingrese un numero del 1 al 100: '))
    vidas = 4
    while num_com != num_pj and vidas > 0:
        if num_pj < num_com: 
            print('Busca un numero mas grande')   
        else:
            print('Busca un numero mas chico')
        vidas -= 1
        num_pj = int(input('Elije otro numero: '))
    
    if vidas > 0:
        print('¡Ganaste!')
    else:
        print('Se acabaron las vidas pichon...')


if __name__ == '__main__':
    run()