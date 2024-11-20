import matplotlib.pyplot as plt
fondo = "#010101"  # 3b1b
azul = "#1c758a"
azul_claro = "#29a0b1"
verde = "#76c893"
amarillo = "#f4d160"
rojo = "#eb7245"
morado = "#9a72ac"
blanco = "#f9f9f9"


def pantalla_interactiva():
    puntos = []

    fig, ax = plt.subplots()
    fig.patch.set_facecolor(fondo)
    ax.set_facecolor(fondo)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_title("Curva de Bezier Interactiva", color=blanco)
    ax.tick_params(colors=blanco)  
    ax.spines['top'].set_color(blanco)
    ax.spines['bottom'].set_color(blanco)
    ax.spines['left'].set_color(blanco)
    ax.spines['right'].set_color(blanco)
    ax.xaxis.label.set_color(blanco)  
    ax.yaxis.label.set_color(blanco)

    ax.text(
        9, -0.5, 
        "Click derecho: Seleccionar\nClick izquierdo: Agregar\nTecla 'd': Borrar nodo",
        fontsize=8, color=blanco, ha="right", va="top", linespacing=1.0
    )

    
    # hacer clilc
    def on_click(event):
         # clicl si adentro
        if event.xdata is not None and event.ydata is not None: 
            x, y = event.xdata, event.ydata
            puntos.append([x, y])  

            # puntos de control
            print(f" x={x:.2f}, y={y:.2f}")
            scatter = ax.scatter(x, y, color=verde)  
    
            # lineas de control
            if len(puntos) > 1:
                xx = [puntos[-2][0], puntos[-1][0]]  
                yy = [puntos[-2][1], puntos[-1][1]]  
                ax.plot(xx, yy, linestyle='--', color=azul_claro, linewidth=1.5)  # Línea azul
            

            fig.canvas.draw()

    # evento
    fig.canvas.mpl_connect("button_press_event", on_click)

    plt.show()
