# test_suma.py
import unittest
from suma import suma_lista # El módulo aún no existe

class TestSumaLista(unittest.TestCase):
    def test_suma_lista_normal(self):
        self.assertEqual(suma_lista([1, 2, 3]), 6)

    def test_suma_lista_vacia(self):
        self.assertEqual(suma_lista([]), 0)

if __name__ == '__main__':
    unittest.main()