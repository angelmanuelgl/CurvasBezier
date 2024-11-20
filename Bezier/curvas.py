import numpy as np
from math import comb 
from Auxiliares import colores as col

def curva_bezier(puntos, cantidad=100):
    def polinomo_bernstein(i, n, t):
        return (comb(n, i)) * ((1 - t) ** (n - i)) * (t ** i)

    n = len(puntos) - 1
    curve = []

    # parametro t
    t_values = np.linspace(0, 1, cantidad)

    for t in t_values:
        # inicializar el punto de la curva en el primero
        unPunto = np.zeros(len(puntos[0]))
        for i in range(n + 1):
            # las contribuciones de cada punto de control
            unPunto += polinomo_bernstein(i, n, t) * np.array(puntos[i])
        curve.append(unPunto.tolist())

    return curve


def dibuja_bezier(ax, puntos):
    curva = curva_bezier(puntos, cantidad=200)
    x_curve = [p[0] for p in curva]
    y_curve = [p[1] for p in curva]
    x_control = [p[0] for p in puntos]
    y_control = [p[1] for p in puntos]
    ax.plot(x_curve, y_curve, label="Curva de Bézier",color=col.azul, linewidth=2)
    return ax