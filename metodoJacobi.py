# Importamos libreria numpy
import numpy as np


# Funcion que realiza el algoritmo de Jacobi y retorna la solucion
def jacobi(A, b, x0, max_iterations=100, tolerance=1e-6):
    n = len(A)
    x = x0.copy()
    x_prev = x0.copy()

    for iteration in range(max_iterations):
        for i in range(n):
            sum_term = np.dot(A[i, :i], x_prev[:i]) + np.dot(A[i, i+1:], x_prev[i+1:])
            x[i] = (b[i] - sum_term) / A[i, i]

        if np.linalg.norm(x - x_prev) < tolerance:
            return x

        x_prev = x.copy()

    return x

# Ejemplo de uso, creamos una matriz A con distintos elementos, un vector B y un vector x0 lleno de numeros 0
A = np.array([[4, 1, -1],
              [2, 7, 1],
              [1, -3, 12]])

b = np.array([3, 2, 13])

x0 = np.array([0, 0, 0])

# Pasamos por parametro las variables
solution = jacobi(A, b, x0)

# Imprimimos por pantalla la solucion
print("Solución:", solution)
