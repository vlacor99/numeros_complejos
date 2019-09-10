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

def Mult_Mat(MatA,MatB):
    """
PRE =Nos entran dos matrices de la forma [[(ParteR,ParteI)*N]*M] las cuales vamos a
     multiplicar ¿como? , cogemos cada una de las filas de MatA y multiplicamos una a
     con las columnas de MatB
POS =Retornamos una matriz de la forma [[(ParteR,ParteI)*longuitud(MatB)]*longuitud(MatA[0])]
    """
    filasB = len(MatB)
    columnasA = len(MatA[0])
    if filasB == columnasA:
        filas = len(MatA)
        columnas = len(MatB[0])
        matriz = [[(0, 0)] * columnas for x in range(filas)]
        for i in range(0, filas):
            for j in range(0, columnas):
                for k in range(0, len(MatB)):
                    m = Multiplicacion(MatA[i][k], MatB[k][j])
                    n = matriz[i][j]
                    matriz[i][j] = (m[0]+n[0], m[1]+n[1])
        return matriz
    else:
        raise 'La multiplicación de matrices no está definida para estas matrices'
def Accion(MatA,VecA):
    """
PRE= Entra una matriz MatA de la forma [[(ParteR,ParteI)*N]*M] y un vector VecA
     de la forma [[(ParteR,ParteI)*N]*1]
POS= Se retorna la multiplicacion entre la Matriz y la transpuesta de el VecA
    """
    return Mult_Mat(MatA,(Mat_Trans([VecA])))
    
def Mult_Mat_Esc(mat,esc):
    """
PRE = Nos entra una matriz de la forma [[(ParteR,ParteI)*N]*M] la cual vamos a
      multiplicar por un escalar R de la forma Numero Real
POS = Retornamos una Matriz de la forma [[(R*ParteR,ParteI)*N]*M] 
    """
    MatT = []
    for i in range(len(mat)):
        MatT.append(Mult_Vect_Esc(mat[i],esc))
    return MatT

def Mult_Vect_Esc(vec,esc):
    """
PRE = Nos entra un Vector de la forma [[(ParteR,ParteI)*N]*1] el cual vamos a
      multiplicar por un escalar R de la forma Numero Real
POS = Retornamos un Vector de la forma [[(R*ParteR,ParteI)*N]*1] 
    """
    VecT = []
    for i in range(len(vec)):
        VecT.append(Multiplicacion(vec[i],(esc,0)))
    return VecT

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

def Mat_Trans(matriz):
    """
PRE = Nos entra una matriz de la forma [[(ParteR,ParteI)*i]*j] la cual le vamos
      a aplicar la formula de matriz transpuesta (a[i][j])**t=(a[j][i])        
POS = Retornamos una matriz de la forma [[(ParteR,ParteI)*j]*i]=(a[j][i])
    """
    MatF = []
    for i in range(len(matriz[0])):
        fila = []
        for j in range(len(matriz)):
            fila.append(matriz[j][i])
        MatF.append(fila)
    return MatF

def Mat_Conjugada(matriz):
    """
PRE = Entra una matriz de la forma [[(ParteR,ParteI)*i]*j] a la cual le vamos a
      aplicar la conjugada a cada una de sus posiciones
POS = Retornamos una matriz de la forma [[(ParteR,-1*ParteI)*i]*j]
    """
    MatF = []
    for i in range(len(matriz)):
        fila = []
        for j in range(len(matriz[0])):
            rta = Conjugado(matriz[i][j])
            fila.append(rta)
        MatF.append(fila)
    return MatF

def Mat_Adjunta(matriz):
    """
PRE= Entra una matriz a la cual le vamos a hallar la adjunta
POS= Retornamos segun la definicion de adjunta , es la transpuesta de la conjugada
    """
    return Mat_Trans(Mat_Conjugada(matriz))

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
    return (unicNum[0],(-unicNum[1]))

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
            
def Vec_Normal(Mat):
    """
PRE= Nos entra una matriz de la forma [[(ParteR,ParteI)*i]*j] a la cual le vamos
     a hallar el vector normal
POS= Retornamos un Vector Normal
    """
    realres = 0
    imares = 0
    for i in range(len(Mat)):
        realres += math.pow(Mat[i][0],2)
        imares += math.pow(Mat[i][1],2)
    return ((math.sqrt(realres)),(math.sqrt(imares)))

def Unitaria(Mat):
    MatT = [[0 for x in range(len(Mat[0]))]for y in range(len(Mat))]
    if len(Mat)!=len(Mat[0]):
        return False
    for i in range(len(Mat[0])):
        MatT[i][i]=1
    MatF = Mult_Mat(Mat,Mat)
    return (MatT==MatF)
            
def Hermitanea(Mat):
    """
PRE= Entra una Matriz Mat de la forma [[(ParteR,ParteI)*i]*j]
POS= Verificamos que sea hermitanea conjugando la transpueesta de la prueba
    """
    prueba=[]
    for x in range(len(Mat)):
        tempo=[]
        for y in range(len(Mat[x])):
            tempo.append(Mat[x][y])
        prueba.append(tempo)
    fin=Mat_Conjugada(Mat_Trans(prueba))
    return(fin==Mat)

def Prod_tensor(MatA,MatB):
    """
PRE= Entran dos matrices VecA y VecB las cuales no importa el tamaño de cada una
POS= Hallamos el pructo tensor y lo retornamos
    """
    lonA = len(MatA)
    colA = len(MatA[0])
    lonB = len(MatB)
    colB = len(MatB[0])
    VecT=[[(0,0) for x in range(colA*colB)]for x in range(lonA*lonB)]
    for i in range(len(VecT)):
        for j in range(len(VecT[0])):
            VecT[i][j] = (Multiplicacion(MatA[i//lonB][j//lonA],MatB[i%lonB][j%lonA]))
    return VecT
def Prod_Int(VecA,VecB):
    """
PRE=Entran dos vectores VecA ,VecB los cuales les vamos a hallar el producto interno
POS= retornamos (la suma de las partes reales , la suma de las partes imaginarias)
    """
    res1 = []
    res2 = []
    for i in range(len(VecA)):
        for j in range(len(VecA[0])):
            realproduct = (VecA[i][j][0]*VecB[i][j][0])
            complexproduct = (VecA[i][j][1]*VecB[i][j][1])
            res1.append(realproduct)
            res2.append(complexproduct)
    return (sum(res1),sum(res2))
def Norma_Mat(MatA):
    return sqrt(Prod_Int(MatA,MatA)[0])
def Dist_Matriz(MatA,MatB):
    a=Sum_Res_Mat(MatA,MatB,0)
##    q=Sum_Res_Mat(MatA,a,1)
##    print(q)
    return Norma_Mat(a)

