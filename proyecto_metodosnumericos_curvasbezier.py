# -*- coding: utf-8 -*-
""" Version 1.0

empezo en
    https://colab.research.google.com/drive/1DAw-eIIGIr2DHvaGS69uIDRj114Xsauc
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# # no sirve marplot en colab
# import matplotlib
# # %matplotlib notebook ## esto ya no
# %matplotlib inline

# pip install plotly
import plotly.graph_objects as go
from plotly.subplots import make_subplots

"""# **Expresion**
La curva de Bézier:
$$
B(t) = \sum_{i=0}^{n} B_{i,n}(t) P_i, \quad \text{con } t \in [0, 1],
$$
donde:
$$
B_{i,n}(t) = \binom{n}{i} (1-t)^{n-i} t^i,
$$
son los polinomios de Bernstein de grado $n$

*Nota:* ignoramos la definicion de que caracteriza a la curva de Bézier puede describirse como el lugar geométrico de todos los puntos que dividen proporcionalmente las líneas entre los puntos de control de manera iterativa, pues es ams dificl de simular
"""

def bezier_curve(points, num_points=100):
    def polinomo_bernstein(i, n, t):
        return (np.math.comb(n, i)) * ((1 - t) ** (n - i)) * (t ** i)

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

# E J E M P L O
puntos_control = [[0, 1], [1, 2], [3, 3], [4, 0]]  # Puntos de control
curva = bezier_curve(puntos_control, num_points=200)


# cordenadas
x_curve = [p[0] for p in curva]
y_curve = [p[1] for p in curva]
x_control = [p[0] for p in puntos_control]
y_control = [p[1] for p in puntos_control]

# imprimir
plt.figure(figsize=(8, 6))
plt.plot(x_curve, y_curve, label="Curva de Bézier", linewidth=2)
# puntos de control
plt.scatter(x_control, y_control, color='red', label="Puntos de Control")
plt.plot(x_control, y_control, 'r--')
plt.legend()
plt.title("Curva de Bézier")
plt.grid()
plt.show()

"""# Pantalla Interactuable

checar la docu:

https://matplotlib.org/stable/users/explain/figure/event_handling.html
https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html
"""



from google.colab import output
output.enable_custom_widget_manager()

"""Support for third party widgets will remain active for the duration of the session. To disable support:"""