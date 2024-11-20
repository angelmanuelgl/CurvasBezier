import matplotlib.pyplot as plt

def pantalla_interactiva():
    puntos = []


    fig, ax = plt.subplots()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_title("Curva de Bezier Interactiva")

    # hacer clilc
    def on_click(event):
         # clicl si adentro
        if event.xdata is not None and event.ydata is not None: 
            x, y = event.xdata, event.ydata
            puntos.append([x, y])  


            # puntos de control
            print(f" x={x:.2f}, y={y:.2f}")
            ax.scatter(x, y, color='red')  

            # lineas de control
            if len(puntos) > 1:
                xx = [puntos[-2][0], puntos[-1][0]]  # Últimos dos puntos (x)
                yy = [puntos[-2][1], puntos[-1][1]]  # Últimos dos puntos (y)
                ax.plot(xx, yy, color='blue', linewidth=1.5)  # Línea azul
            

            fig.canvas.draw()

    # evento
    fig.canvas.mpl_connect("button_press_event", on_click)

    plt.show()
