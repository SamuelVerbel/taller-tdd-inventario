import unittest
from procesador import es_palindromo

class TestPalindromo(unittest.TestCase):
    def test_es_palindromo_radar(self):
        self.assertTrue(es_palindromo("radar"))

if __name__ == "__main__":
    unittest.main()