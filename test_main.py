# test_main.py
import unittest
import main  # Importamos el script main.py

class TestMain(unittest.TestCase):
    def test_sumar(self):
        resultado = main.sumar(3, 5)
        self.assertEqual(resultado, 8)  # Verificamos que el resultado sea 8

if __name__ == '__main__':
    unittest.main()
