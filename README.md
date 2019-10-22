# CALCULADORA DE NUMEROS Y MATRICES COMPLEJAS :
# TEST MARBLES :
#   DESCRIPCION :

Calculadora De Numeros y Matrices complejas hecho por Vladimir Correa Arroyave en Lenguaje Python.
Ademas tenemos Un Gran Simulador de Marbles(Piquis) en el cual depende de los click que se le den este va a ir simulando el movimiento de cierto numero de Marbles

# TEST MARBLES
![GG](https://user-images.githubusercontent.com/54039061/67326166-c57f9a00-f4db-11e9-96d3-357c62c300b5.PNG)

# EJEMPLO NUMEROS REALES
# ENTRADA
([[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],[(1/2,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],[(1/2,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],[(0,0),(1/3,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],[(0,0),(1/3,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],[(0,0),(1/3,0),(1/3,0),(0,0),(0,0),(0,0),(0,0),(0,0)],[(0,0),(0,0),(1/3,0),(0,0),(0,0),(0,0),(0,0),(0,0)]],[(1,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],2)

# SALIDA
[(0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.16666666666666666, 0.0), (0.16666666666666666, 0.0), (0.3333333333333333, 0.0), (0.16666666666666666, 0.0)]

# SEGUIR LOS SIGUIENTES PASOS

#   ¿QUE CALCULOS SE HACEN?

# EN NUMEROS COMPLEJOS :

1) Suma : suma dos numeros complejos
2) Producto : el producto de dos numeros complejos
3) Resta : resta dos numeros complejos
4) División division de dos numeros complejos
5) Módulo : saca el modulo de un numero complejo
6) Conjugado : coloca la parte imaginaria de un numero complejo negativa
7) Conversión entre representaciones polar y cartesiano : pasa un numero de polar a cartesiano
8) Retornar la fase de un número complejo 

# EN MATRICES COMPLEJAS :

1) Adición de vectores complejos 
2) Inversa de vectores complejos 
3) Multiplicación escalar de vectores complejos 
4) Adición de matrices complejos 
5) Inversa de matrices complejos 
6) Multiplicación escalar de matrices complejas 
7) Matriz transpuesta 
8) Matriz conjugada 
9) Matriz adjunta 
10) Función para calcular la "acción" de una matriz sobre un vector 
11) Norma de matrices 
12) Distancia entrematrices 
13) Revisar si es unitaria 
14) Revisar si es Hermitian 
15) Producto tensor .


# ¿Como Instalar?
0) Esta hecho en lenguaje python 3.7.4 , este codigo esta disponible para versiones 3.7.x , para poder utilizarlo se tiene que descargar
la version mas reciente la cual esta disponible en https://www.python.org/ .
1) Buscar en tu navegador preferido
![Captu](https://user-images.githubusercontent.com/54039061/64633306-947e5680-d3c0-11e9-8e63-762808fffc48.PNG)
2) Buscar la version que se adapte a tu sistema operativo
![Untitled](https://user-images.githubusercontent.com/54039061/64633756-706f4500-d3c1-11e9-8375-6b16f17ade22.png)
3)Descargar
4) descargar todos los codigos en una misma carpeta
![arc1carp](https://user-images.githubusercontent.com/54039061/64201722-f1c05800-ce54-11e9-8707-976f049aa357.png)
5) click en tecla windows
![123](https://user-images.githubusercontent.com/54039061/64634003-e5427f00-d3c1-11e9-8117-eea94ad87551.png)
6) buscar idle
![img2](https://user-images.githubusercontent.com/54039061/64200892-0865af80-ce53-11e9-8b5c-fddea35ed343.png)

# ¿ COMO UTILIZAR EL CODIGO ?
# EJEMPLO EN CODIGO :

```Python
		
//from sys import stdin
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
```
# PARA UTILIZAR EL CODIGO EN SUMA
1) Quiero Sumar
2) NumA = 3+5i
3) NumB = 4-7i
4) Suma_Resta((3,5),(4,-7),1)
# PARA UTILIZAR EL CODIGO EN RESTA
1) Quiero Restar
2) NumA = 3+5i
3) NumB = 4-7i
4) Suma_Resta((3,5),(4,-7),0)
# EJEMPLO EN IMAGEN
![12345](https://user-images.githubusercontent.com/54039061/64634611-3e5ee280-d3c3-11e9-9141-e9da69e85b9e.PNG)

# PRUEBAS EN UNITTEST

Se utilizan por medio de una libretria llamada unittest la cual verifica si los casos de prueba son congruentes
de caso contrario a que no funcionen este mandara un rojito el cual sera un error en el programa.
![img5](https://user-images.githubusercontent.com/54039061/64201600-ae65e980-ce54-11e9-89b8-e86ffe8ee638.png)

# CODIGO MARBLES

Este codigo va a simular el orden de un numero x de canicas despues de un numero n de clickscon coeficiente booleano .

# HECHO POR :
# VLADIMIR CORREA ARROYAVE
