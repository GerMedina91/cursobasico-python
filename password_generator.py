import random
import string


def generate_password():
    PASSWORD_LENGHT = 20
    password = ''
    lista_de_caracteres = list(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    for i in range(PASSWORD_LENGHT):
        a = random.randint(0, len(lista_de_caracteres)-1)
        password += lista_de_caracteres[a]
    return password

    

def run():
    password = generate_password()
    print(password)

if __name__ == '__main__':
    run()