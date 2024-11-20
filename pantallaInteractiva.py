import matplotlib.pyplot as plt

# 3b1b
fondo = "#000000"  
azul = "#1c758a"
azul_claro = "#29a0b1"
verde = "#76c893"
amarillo = "#f4d160"
rojo = "#eb7245"
morado = "#9a72ac"
blanco = "#f9f9f9"

# auxiliar
def configurar_ejes(ax):
    ax.set_facecolor(fondo)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_title("Curvas de Bézier", color=blanco, fontsize=20)
    ax.text(
        9.5, -0.5,
        "Clic izquierdo: Agregar\nClic derecho: Seleccionar/Mover\n'd': Borrar nodo",
        fontsize=10, color=blanco, ha="right", va="top"
    )
    ax.tick_params(colors=blanco)
    ax.spines['top'].set_color(blanco)
    ax.spines['bottom'].set_color(blanco)
    ax.spines['left'].set_color(blanco)
    ax.spines['right'].set_color(blanco)
    ax.xaxis.label.set_color(blanco)
    ax.yaxis.label.set_color(blanco)

def pantalla_interactiva():
    # acomodar
    fig, ax = plt.subplots()
    fig.patch.set_facecolor(fondo)
    configurar_ejes(ax) 

    # datos 
    puntos = []
    scatter = None
    selected_point = None 

    # actualizar dibujo
    def actualizar_grafico():
        # acomodar
        nonlocal scatter
        ax.clear()
        configurar_ejes(ax)  

        # puntos y  lineas
        x_vals = [p[0] for p in puntos]
        y_vals = [p[1] for p in puntos]
        scatter = ax.scatter(x_vals, y_vals, color=azul_claro)
        if len(puntos) > 1:
            ax.plot(x_vals, y_vals, color=azul, linewidth=1.5, linestyle="--")

        # seleecionado
         # Seleccionar
        if selected_point is not None:
            ax.scatter(
                puntos[selected_point][0], puntos[selected_point][1],
                color=amarillo, s=100, label="Seleccionado"
            )
            ax.legend(labelcolor=blanco, facecolor=fondo, edgecolor=blanco)   

        fig.canvas.draw()

    # dar click
    def on_click(event):
        nonlocal selected_point
        if event.button == 1:  # Clic izquierdo
            if event.xdata is not None and event.ydata is not None:
                if selected_point is not None:  # Si hay un punto seleccionado
                    puntos[selected_point] = [event.xdata, event.ydata]  # Mover el punto seleccionado
                    print(f"Punto movido a: {puntos[selected_point]}")
                    selected_point = None  # Deseleccionar el punto
                else:
                    puntos.append([event.xdata, event.ydata])  # Agregar un nuevo punto
                actualizar_grafico()
        elif event.button == 3:  # Clic derecho para seleccionar un punto
            if scatter:
                # Detectar el punto más cercano al clic
                xdata = event.xdata
                ydata = event.ydata
                distances = [(x - xdata) ** 2 + (y - ydata) ** 2 for x, y in puntos]
                selected_point = distances.index(min(distances)) if distances else None
                print(f"Punto seleccionado: {puntos[selected_point]}" if selected_point is not None else "Ningún punto seleccionado")
                actualizar_grafico()

    # eliminar
    def on_key(event):
        nonlocal selected_point
        if event.key == 'd' and selected_point is not None:  # Tecla 'd' para eliminar
            print(f"Punto eliminado: {puntos[selected_point]}")
            puntos.pop(selected_point)
            selected_point = None
            actualizar_grafico()

    def on_motion(event):
        if selected_point is not None and event.xdata is not None and event.ydata is not None:
            puntos[selected_point] = [event.xdata, event.ydata]
            actualizar_grafico()

    # para que funcione
    fig.canvas.mpl_connect("button_press_event", on_click)
    fig.canvas.mpl_connect("motion_notify_event", on_motion)
    fig.canvas.mpl_connect("key_press_event", on_key)
    plt.show()

    return puntos
