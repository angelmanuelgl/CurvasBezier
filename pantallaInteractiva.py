import matplotlib.pyplot as plt
from Auxiliares import colores as col
from Auxiliares import dibujar as dib

from Bezier.curvas import curva_bezier
from Bezier.curvas import dibuja_bezier


# # # # # # # # # # # # # # # # # # # # # # # # # # 
# P A N T A L L A    I N T E R A C T I V A 
# # # # # # # # # # # # # # # # # # # # # # # # # # 

def pantalla_interactiva():
    # acomodar
    fig, ax = plt.subplots()
    fig.patch.set_facecolor(col.fondo)
    dib.configurar_ejes(ax) 

    # datos 
    puntos = []
    scatter = None
    punto_actual = None 

    # actualizar dibujo
    def actualizar_grafico():
        # acomodar
        nonlocal scatter
        ax.clear()
        dib.configurar_ejes(ax) 

        # puntos y  lineas
        x_vals = [p[0] for p in puntos]
        y_vals = [p[1] for p in puntos]
        if len(puntos) > 1:
            ax.plot(x_vals, y_vals, color=col.blanco, linewidth=0.8) #, linestyle="--"
        scatter = ax.scatter(x_vals, y_vals, color=col.amarillo)

        # formato del seleccioado
        if punto_actual is not None:
            print("hi")
            ax.scatter(
                puntos[punto_actual][0], puntos[punto_actual][1],
                color=col.rojo, s=100, label="Seleccionado"
            )
            ax.legend(labelcolor=col.blanco, facecolor=col.fondo, edgecolor=col.blanco) 

        # dibujar BEZIER   
        dibuja_bezier(ax, puntos)
        
        fig.canvas.draw()


    #  #  #  A  C  C  I  O  N  E  S  #  #  #
    # dar click
    def on_click(event): 
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
                if scatter:
                    xdata = event.xdata
                    ydata = event.ydata
                    distances = [(x - xdata) ** 2 + (y - ydata) ** 2 for x, y in puntos]    
                    punto_actual = distances.index(min(distances)) if ( min(distances) < 0.5) else None

                # SELECCIONAR
                if punto_actual is not None:
                    actualizar_grafico()
                    
                # AGREGAR
                else:
                    puntos.append([event.xdata, event.ydata])  
                    actualizar_grafico()

        #print("al final del click:", puntos)  
    
    
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
