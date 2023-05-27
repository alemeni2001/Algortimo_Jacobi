# Importamos libreria numpy
import numpy as np

print ("Metodo Jacobi que resuelve ecuaciones lineales con una matriz de N X N")

# Pedir al usuario la dimensión del sistema de ecuaciones
n = int(input("Ingrese la dimensión del sistema de ecuaciones: "))

# Pedir al usuario los elementos de la matriz A

A = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        A[i, j] = float(input(f"Ingrese el elemento A[{i}][{j}]: "))

# Pedir al usuario los elementos del vector B

B = np.zeros(n)
for i in range(n):
    B[i] = float(input(f"Ingrese el elemento b[{i}]: "))


x0 = x0 = np.zeros_like(B)


# A = matriz, B = vector independiente x0 = vector inicial para el metodo de Jacobi
# tol = tolerancia para determinar convergencia de metodo, max_iter = Número máximo de iteraciones permitidas 
def jacobi(A, B, x0, tol=1e-6, max_iter=100):
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
            return x_copy
        
        x = x_copy.copy()
    
    print("El método de Jacobi no converge después de", max_iter, "iteraciones.")
    return x


# Pasamos por parametro las variables para que opere la solucion
solution = jacobi(A, B, x0)

# Imprimimos por pantalla la solucion
print("Solución:", solution)
