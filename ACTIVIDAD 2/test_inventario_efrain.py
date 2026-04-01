import unittest
# Esto fallará porque 'inventario.py' no existe aún
from inventario import Inventario 

class TestInventarioEfrain(unittest.TestCase):
    def test_agregar_y_obtener(self):
        inv = Inventario()
        inv.agregar_producto("Manzana", 10)
        self.assertEqual(inv.obtener_inventario()["Manzana"], 10)

if __name__ == '__main__':
    unittest.main()