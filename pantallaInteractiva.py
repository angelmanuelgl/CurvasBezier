import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'serif'  # Usa una fuente serif (similar a LaTeX)
plt.rcParams['mathtext.fontset'] = 'cm'  # Usa las fuentes "Computer Modern" (de LaTeX)
plt.rcParams['mathtext.rm'] = 'serif'

# event.button == 1 CLICK IZQUIERDO
# event.button == 3 CLICK DERECHIO 
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
    ax.set_title(r"Curvas de Bézier", color=blanco, fontsize=20)
    ax.text(
        9.5, -0.5,
        "Click izq: Seleccionar\\Mover \n Tecla d: Borrar nodo",
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
    punto_actual = None 

    # actualizar dibujo
    def actualizar_grafico():
        # acomodar
        nonlocal scatter
        ax.clear()
        configurar_ejes(ax)  
        # puntos y  lineas
        x_vals = [p[0] for p in puntos]
        y_vals = [p[1] for p in puntos]
        if len(puntos) > 1:
            ax.plot(x_vals, y_vals, color=blanco, linewidth=0.8) #, linestyle="--"
        scatter = ax.scatter(x_vals, y_vals, color=amarillo)

        # seleccionar
        if punto_actual is not None:
            ax.scatter(
                puntos[punto_actual][0], puntos[punto_actual][1],
                color=rojo, s=100, label="Seleccionado"
            )
            ax.legend(labelcolor=blanco, facecolor=fondo, edgecolor=blanco)   

        fig.canvas.draw()

    # dar click
    def on_click(event): 
        print("antes del click:", puntos)  
        nonlocal punto_actual
        # si se dio click &&  el clikc fue dentro de la pantalla
        if event.button == 1 and event.xdata is not None and event.ydata is not None:
            print("click izquierdo")
            # si hay un punto seleccionado
            if punto_actual is not None:
                puntos[punto_actual] = [event.xdata, event.ydata] 
                print(f"se movio a {puntos[punto_actual]}")
                punto_actual = None  
                actualizar_grafico()
        
            # si no, podemos seleccionar, o agregar uno nuevo
            else:       
                seleccionado = None
                if scatter:
                    xdata = event.xdata
                    ydata = event.ydata
                    distances = [(x - xdata) ** 2 + (y - ydata) ** 2 for x, y in puntos]
                    print(min(distances))
                    if( min(distances) < 0.5):
                        seleccionado = distances.index(min(distances)) if distances else None

                 # SELECCIONAR
                if seleccionado is not None:
                    punto_actual = seleccionado
                    print(f"Punto seleccionado: {puntos[seleccionado]}")
                    actualizar_grafico()
                    
                # AGREGAR
                else:
                    puntos.append([event.xdata, event.ydata])  
                    actualizar_grafico()
        print("al final del click:", puntos)  
    
    
    # eliminar
    def on_key(event): 
        nonlocal punto_actual
        # Tecla D eliminar
        if event.key == 'd' and punto_actual is not None: 
            print(f"se elimino {puntos[punto_actual]}")
            puntos.pop(punto_actual)
            punto_actual = None
            actualizar_grafico()

    # que se mueva
    def on_motion(event):
        if punto_actual is not None and event.xdata is not None and event.ydata is not None:
            puntos[punto_actual] = [event.xdata, event.ydata]
            actualizar_grafico()

    # para que funcione
    fig.canvas.mpl_connect("button_press_event", on_click)
    fig.canvas.mpl_connect("motion_notify_event", on_motion)
    fig.canvas.mpl_connect("key_press_event", on_key)
    plt.show()

    return puntos
