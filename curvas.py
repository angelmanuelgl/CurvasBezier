import numpy as np
from math import comb 

def bezier_curve(points, num_points=100):
    def polinomo_bernstein(i, n, t):
        return (comb(n, i)) * ((1 - t) ** (n - i)) * (t ** i)

    n = len(points) - 1
    curve = []

    # Generar valores para el parámetro t
    t_values = np.linspace(0, 1, num_points)

    for t in t_values:
        # inicializar el punto de la curva en el primero
        point = np.zeros(len(points[0]))
        for i in range(n + 1):
            # las contribuciones de cada punto de control
            point += polinomo_bernstein(i, n, t) * np.array(points[i])
        curve.append(point.tolist())

    return curve