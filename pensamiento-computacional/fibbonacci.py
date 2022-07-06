def fibonacci(n):
        print(n)
        if n == 0 or n == 1:
            return 1

        return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    numero = int(input('Ingresa un numero: '))

    print(fibonacci(numero))


if __name__ == '__main__':
    main()