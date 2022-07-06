import unittest

def suma(num_1, num_2):
    return num_1 + num_2

class CajaNegraTest(unittest.TestCase):

    def test_suma_positivos(self):
        num_1 = 5
        num_2 = 10

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, 15)

    def test_suma_negativos(self):
        num_1 = -5
        num_2 = -10

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, -14)

if __name__ == '__main__':
    unittest.main()