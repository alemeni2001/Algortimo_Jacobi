# Importamos libreria numpy
import numpy as np
import os

def limpiarConsola():
    #limpiar consola en Linux
    if (os.name == "posix"):
        os.system("clear")
    elif (os.name == "nt"):
        #limpar consola en winows
        os.system("cls")

def presentacion():
    print("\n\n")
    print("------------------------------------------------------------------------------")
    print ("Metodo Jacobi que resuelve ecuaciones lineales con una matriz de N X N")
    print("------------------------------------------------------------------------------")
    print ("Integrantes: Alejo Menini, Juan Caceffo, Sol Lopez, Pablo Foglia")
    print("------------------------------------------------------------------------------")
    print("\n\n")


def datosJacobi():
    # Pedir al usuario la dimensión del sistema de ecuaciones
    n = int(input("Ingrese la dimensión del sistema de ecuaciones: "))

    # Pedir al usuario los elementos de la matriz A
    print("Ingrese la matriz A:")
    A = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            A[i, j] = float(input(f"Ingrese el elemento A[{i}][{j}]: "))

    # Pedir al usuario los elementos del vector B
    print("Ingrese la matirz B:")
    B = np.zeros(n)
    for i in range(n):
        B[i] = float(input(f"Ingrese el elemento b[{i}]: "))

    #valores iniciales para el metodo
    x0 = np.zeros_like(B)


    # Pedir al usuario la cantidad de decimales correctos
    #rango de exactitud de decimales posible
    RANGO_TOLERABLE = range(1,11)
    exactitud = int(input(f"ingrese la cantidad de deicmales correctos que desea dentro del rango ({RANGO_TOLERABLE.start}..{RANGO_TOLERABLE.stop-1}): "))
    #verificar que la exactitud ingresada por el usuario sea correcta 
    while (not(exactitud in RANGO_TOLERABLE)):    
        exactitud = int(input(f"ingrese la cantidad de deicmales correctos que desea en el dentro del rango ({RANGO_TOLERABLE.start}..{RANGO_TOLERABLE.stop-1}): "))
    #scamos el valor de paradad dada la exactitud
    tolerancia = "0."
    #agregamos tantos 0 como exactitud indicada
    for i in range(exactitud): tolerancia += "0"
    #agregamos un uno para indicar que es una fraccion
    tolerancia += "1"
    #convertimos a flotante para poder operara
    tolerancia = float(tolerancia)

    return (A,B,x0,tolerancia,exactitud)
    

# A = matriz, B = vector independiente x0 = vector inicial para el metodo de Jacobi
# tol = tolerancia para determinar convergencia de metodo
#exactitud = cantidad de decimales correctos
# max_iter = Número máximo de iteraciones permitidas 
def jacobi(A, B, x0, tol, exactitud,max_iter=100):
    # Se determina el tamaño del vector para que este sea recorrido en el ciclo for
    n = len(B)
    # Se copia el vector para asi poder mantener el vector inicial sin modificar en el proceso iterativo
    x = x0.copy()
    x_copy = np.zeros_like(x)

    for m in range(max_iter):
        for i in range(n):

            sum_term = 0
            for j in range(n):
                if j != i:
                    sum_term += A[i, j] * x[j]
            # Se calcula el nuevo valor de la variable dividiendo la diferencia entre b[i] (el término independiente) y sum_term entre A[i, i] (el coeficiente diagonal)
            x_copy[i] = (B[i] - sum_term) / A[i, i]
        
        # Se calcula la norma del vector de corrección x_new - x. Si esta norma es menor que la tolerancia, se considera que el método ha convergido
        # caso contrario devuelve el mensaje
        if np.linalg.norm(x_copy - x) < tol:
            return np.around(x_copy,exactitud)
        
        x = x_copy.copy()
    
    print("El método de Jacobi no converge después de", max_iter, "iteraciones.")
    return x

def main():
    presentacion()
    DATE = datosJacobi()
    limpiarConsola()
    presentacion()
    # Imprimimos por pantalla la solucion
    print("para el sistema de ecuaciones lineal:\n")
    X = [f"x{i}" for i in range(DATE[1].shape[0])]
    print (DATE[0],"*",np.array(X),"=",DATE[1],"\n")
    print("la solucion aproximadad es:")
    print(np.array(X),":",jacobi(*DATE))
    
main()
