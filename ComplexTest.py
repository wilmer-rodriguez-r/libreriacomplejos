import unittest
import math
import LibraryComplex as lcp

class testfunciones(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(lcp.sum_complex((4, 5), (5, 4)), (9, 9))
        self.assertEqual(lcp.sum_complex((-4, -100), (1, 4)), (-3, -96))

    def test_res(self):
        self.assertEqual(lcp.res_complex((4, 5), (5, 4)), (-1, 1))
        self.assertEqual(lcp.res_complex((-4, -100), (1, 4)), (-5, -104))

    def test_mult(self):
        self.assertEqual(lcp.mult_complex((4, 5), (5, 4)), (0, 41))
        self.assertEqual(lcp.mult_complex((-4, -100), (1, 4)), (396, -116))

    def test_div(self):
        self.assertEqual(lcp.div_complex((3, 4), (4, 3)), (0.96, 0.28))
        self.assertEqual(lcp.div_complex((-4, -10), (1, 4)), (44/116, 6/116))

    def test_modulo(self):
        self.assertEqual(lcp.modulo_complex((3, -4)), 5)
        self.assertEqual(lcp.modulo_complex((0, -10)), 10)

    def test_conjugado(self):
        self.assertEqual(lcp.conjugado_complex((3, -4)), (3, 4))
        self.assertEqual(lcp.conjugado_complex((-4, -100)), (-4, 100))

    def test_cartesianas(self):
        self.assertEqual(lcp.convercar_complex((3, -4)), (5, math.tan(-4/3)))
        self.assertEqual(lcp.convercar_complex((-4, -100)), (10016**(1/2), math.tan(100/4)))

    def test_polares(self):
        self.assertEqual(lcp.converpo_complex((3, math.pi/2)), (0, 3))
        self.assertEqual(lcp.converpo_complex((4, math.pi/3)), (2, 3.6))

    def test_fase(self):
        self.assertEqual(lcp.fase_complex((1, 1)), 45)
        self.assertEqual(lcp.fase_complex((2, 1)), 27)

if __name__ == '__main__':
    unittest.main()