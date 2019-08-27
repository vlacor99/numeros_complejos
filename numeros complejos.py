from sys import stdin
from math import *

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

def Sum_Res_Mat(MatA,MatB,Op):
    """
PRE = Nos entran dos matrices cada una con tuplas las cuales cada una es un numero imaginario NumA y NumB dentro
      de ellas la posicion [0] de cada una nos da la parte real y la parte [1] es la parte imaginaria, Ademas
      nos entra un Op el cual si es "1" hacemos suma entre complejos y si es "0" hacemos la resta entre complejos.
POS = Devolvemos una matriz con tuplas las cuales en la posicion [0] nos da la parte real y la parte [1]
      es la parte imaginaria.
    """
    MatT = [[0 for x in range(len(MatA[0]))]for x in range(len(MatA))]
    if len(MatA[0])!=len(MatB[0]) or len(MatA)!=len(MatB):
        print("La {} entre estos vectores no esta definida".format("suma" if Op==1 else "resta"))
    for x in range(len(MatA)):
        for y in range(len(MatA[0])):
            if Op==1:
                MatT[x][y]=Suma_Resta(MatA[x][y],MatB[x][y],1)
            else:
                MatT[x][y]=Suma_Resta(MatA[x][y],MatB[x][y],0)
    return MatT

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

def Division(NumA,NumB):
    """
PRE = Nos entran dos tuplas la cuales cada una es un numero imaginario NumA y NumB dentro de ellas la posicion
      [0] de cada una nos da la parte real y la parte [1] es la parte imaginaria, hallamos ParteArriba y
      ParteAbajo para hallar la ParteR y la ParteI.
POS = Devolvemos una tupla en la cual la posicion [0] nos da la parte real y la parte [1] es la parte imaginaria
    """
    ParteArriba = Multiplicacion(NumA,NumB)
    ParteAbajo = (NumB[0]**2)+(NumB[1]**2)
    ParteR = ParteArriba[0]/ParteAbajo
    ParteI = ParteArriba[1]/ParteAbajo
    Respuesta = (ParteR,ParteI)
    return Respuesta

def Modulo(unicNum):
    """
PRE = entra un unicNum  el cual es un numero complejo para hallar el modulo se define como a la
      distancia del origen de coordenadas al afijo de dicho número.
POS = se devuelve el modulo del numero complejo.
    """
    return ((unicNum[0]**2)+(unicNum[1]**2))**0.5

def Conjugado(unicNum):
    """
PRE = entra un unico numero el cual es un complejo para este vamos a hallar el opuesto de
      un número es simétrico respecto del origen
POS = devolvemos la ParteR igual que como entra y la ParteI negativa
    """
    return (unicNum[0],(unicNum[1])*(-1))

def Complejos_Polar(unicNum):
    """
PRE = entra un numeron complejo el cual vamos a pasar de complejo a polar
POS = devolvemos el numero con sus coordenadas polares
    """
    mod=Modulo(unicNum)
    argumento = atan(unicNum[1]/(unicNum[0]))
    Respuesta = (mod,argumento)
    return Respuesta

def Fase(unicNum):
    """
PRE = entra un numeron complejo el cual vamos sacarle su fase
POS = devolvemos la arco tangente de su ParteI sobre su ParteR
    """
    respuesta = atan(unicNum[1]/unicNum[0])
    return respuesta
            
