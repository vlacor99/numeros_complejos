import unittest
import Calculadora_Quantica
from math import *

class MyTestCase(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(Calculadora_Quantica.Suma_Resta((3,4),(4,16),1),(7,20))
    def test_resta(self):
        self.assertEqual(Calculadora_Quantica.Suma_Resta((3,4),(4,16),0),(-1,-12))
    def test_multiplicacion(self):
        self.assertEqual(Calculadora_Quantica.Multiplicacion((3,4),(4,16)),(-52,64))
    def test_division(self):
        self.assertEqual(Calculadora_Quantica.Division((3,4),(4,16)),(-0.19117647058823528, 0.23529411764705882))
    def test_modulo(self):
        self.assertEqual(Calculadora_Quantica.Modulo((3,4)),5)
    def test_conjugado(self):
        self.assertEqual(Calculadora_Quantica.Conjugado((3,4)),(3,-4))
    def test_complejos_polar(self):
        self.assertEqual(Calculadora_Quantica.Complejos_Polar((3,4)),(5,0.9272952180016122))
    def test_fase(self):
        self.assertEqual(Calculadora_Quantica.Fase((3,6)),1.1071487177940904)
    def test_sum_vec(self):
        self.assertEqual(Calculadora_Quantica.Sum_Res_Mat([[(1,2),(2,3),(3,4)]],[[(2,4),(4,6),(6,8)]],1),[[(3,6),(6,9),(9,12)]])
    def test_res_vec(self):
        self.assertEqual(Calculadora_Quantica.Sum_Res_Mat([[(1,2),(2,3),(3,4)]],[[(2,4),(4,6),(6,8)]],0),[[(-1,-2),(-2,-3),(-3,-4)]])
    def test_mul_esc_vecC(self):
        self.assertEqual(Calculadora_Quantica.Mult_Vect_Esc([(2,3),(4,5),(6,7)],5),[(10,15),(20,25),(30,35)])
    def test_mul_esc_matC(self):
        self.assertEqual(Calculadora_Quantica.Mult_Mat_Esc([[(2,3),(4,5),(6,7)],[(1,3),(2,5),(8,7)],[(12,3),(24,5),(32,7)]],5),([[(10,15),(20,25),(30,35)],[(5,15),(10,25),(40,35)],[(60,15),(120,25),(160,35)]]))
    def test_sum_mat(self):
        self.assertEqual(Calculadora_Quantica.Sum_Res_Mat([[(1,2),(2,3),(3,4)],[(1,2),(2,3),(3,4)],[(1,2),(2,3),(3,4)]],[[(2,4),(4,6),(6,8)],[(2,4),(4,6),(6,8)],[(2,4),(4,6),(6,8)]],1),[[(3,6),(6,9),(9,12)],[(3,6),(6,9),(9,12)],[(3,6),(6,9),(9,12)]])
    def test_res_mat(self):
        self.assertEqual(Calculadora_Quantica.Sum_Res_Mat([[(1,2),(2,3),(3,4)],[(1,2),(2,3),(3,4)],[(1,2),(2,3),(3,4)]],[[(2,4),(4,6),(6,8)],[(2,4),(4,6),(6,8)],[(2,4),(4,6),(6,8)]],0),[[(-1,-2),(-2,-3),(-3,-4)],[(-1,-2),(-2,-3),(-3,-4)],[(-1,-2),(-2,-3),(-3,-4)]])
    def test_mat_transpuesta(self):
        self.assertEqual(Calculadora_Quantica.Mat_Trans([[(1,2),(2,3),(3,4)],[(1,2),(2,3),(3,4)]]),[[(1, 2), (1, 2)], [(2, 3), (2, 3)], [(3, 4), (3, 4)]])
    def test_mat_conjugada(self):
        self.assertEqual(Calculadora_Quantica.Mat_Conjugada([[(1,2),(2,3),(3,4)],[(1,2),(2,3),(3,4)]]),[[(1, -2), (2, -3), (3, -4)], [(1, -2), (2, -3), (3, -4)]])
    def test_mat_adjunta(self):
        self.assertEqual(Calculadora_Quantica.Mat_Adjunta([[(1,2),(2,3),(3,4)],[(1,2),(2,3),(3,4)]]),[[(1, -2), (1, -2)], [(2, -3), (2, -3)], [(3, -4), (3, -4)]])
    def test_accion(self):
        self.assertEqual(Calculadora_Quantica.Accion([[(1,2),(2,3),(3,4)],[(1,2),(2,3),(3,4)]],[(2,3),(4,5),(6,7)]),[[(-21, 74)], [(-21, 74)]])
    def test_norma_mat(self):
        self.assertEqual(Calculadora_Quantica.Norma_Mat([[(1,2),(2,3),(3,4)],[(1,2),(2,3),(3,4)]]),5.291502622129181)
    def distancia_matrices(self):
        self.assertEqual(Calculadora_Quantica.Dist_Matriz([[(1,2),(2,3),(3,4)],[(1,2),(2,3),(3,4)]],[[(1,2),(2,3),(3,4)],[(1,2),(2,3),(3,4)]]),0)
if __name__== '__main__':
    unittest.main()
