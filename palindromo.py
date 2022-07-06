def palindromo(palabra):
    palabra = str(palabra).lower().replace(' ', '').strip()
    palabra_r = palabra[::-1]
    if (palabra == palabra_r):
        return True
    else:
        return False


def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')


if __name__ == '__main__':
    run()

