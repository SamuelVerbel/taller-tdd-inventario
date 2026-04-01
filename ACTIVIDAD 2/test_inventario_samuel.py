import unittest
from inventario import Inventario

class TestInventarioSamuel(unittest.TestCase):
    def test_actualizar_y_buscar(self):
        inv = Inventario()
        inv.agregar_producto("Monitor", 5)
        # Esto fallará porque el método actualizar_stock no existe
        inv.actualizar_stock("Monitor", 10) 
        self.assertEqual(inv.buscar_producto("Monitor"), 10)

if __name__ == '__main__':
    unittest.main()