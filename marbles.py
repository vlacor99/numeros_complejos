from math import *
import unittest

def Suma_Resta(NumA,NumB,Op):
    """
PRE = Nos entran dos tuplas la cuales cada una es un numero imaginario NumA y NumB dentro de ellas la posicion
      [0] de cada una nos da la parte real y la parte [1] es la parte imaginaria, Ademas nos entra un Op
      el cual si es "1" hacemos suma entre complejos y si es "0" hacemos la resta entre complejos.
POS = Devolvemos una tupla en la cual la posicion [0] nos da la parte real y la parte [1] es la parte imaginaria
    """
    if Op==1:
        SumParteR = NumA[0]+NumB[0]
        SumParteI = NumA[1]+NumB[1]
    else:
        SumParteR = NumA[0]-NumB[0]
        SumParteI = NumA[1]-NumB[1]
    Respuesta = (SumParteR , SumParteI)
    return Respuesta
def Multiplicacion(NumA,NumB):
    """
PRE = Nos entran dos tuplas la cuales cada una es un numero imaginario NumA y NumB dentro de ellas la posicion
      [0] de cada una nos da la parte real y la parte [1] es la parte imaginaria, hallamos ParteA y ParteD para
      al final sumarlos y hallar la parte real despues hallamos ParteB y ParteC las cuales sumamos para hallar
      la parte imaginaria.
POS = Devolvemos una tupla en la cual la posicion [0] nos da la parte real y la parte [1] es la parte imaginaria
    """
    ParteA=NumA[0]*NumB[0]
    ParteB=NumA[0]*NumB[1]
    ParteC=NumA[1]*NumB[0]
    ParteD=(NumA[1]*NumB[1])*(-1)
    SumParteR = ParteA+ParteD
    SumParteI = ParteB+ParteC
    Respuesta = (SumParteR , SumParteI)
    return Respuesta

def Marbels(matrizAdj, estadoInicial, clicks):
    '''Se simula el experimento de  las canicas despues de varios clicks UTILIZANDO suma y resta de numeros imaginarios'''
    while clicks > 0:
        clicks -= 1
        aux = []
        for i in range(len(matrizAdj)):
            sume = (0,0)
            for j in range(len(estadoInicial)):
               sume = Suma_Resta(sume,Multiplicacion(estadoInicial[j],matrizAdj[i][j]),1)
            aux.append(sume)
        estadoInicial  = aux
    return aux

class MyTestCase(unittest.TestCase):
    def test_marbles(self):
        result = Marbels([[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],[(0,0),(1,0),(0,0),(0,0),(0,0),(1,0)],[(0,0),(0,0),(0,0),(1,0),(0,0),(0,0)],[(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)],[(1,0),(0,0),(0,0),(0,0),(1,0),(0,0)]],[(6,0),(2,0),(1,0),(5,0),(3,0),(10,0)],1)
        self.assertEqual(result,[(0, 0), (0, 0), (12, 0), (5, 0), (1, 0), (9, 0)])
if __name__== '__main__':
    unittest.main()
