import matplotlib.pyplot as plt
from curvas import bezier_curve

# # # # # # # # # # # # # # # # # # # # 
#   C   U   R   V   A   S 
# # # # # # # # # # # # # # # # # # # # 
def main():
    print("hi")
    puntos_control = [[0, 1], [1.5, 1.5], [3, 3], [2,4], [1,3]] 
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


# Punto de entrada del programa
if __name__ == "__main__":
    main()
    