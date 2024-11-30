import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from Auxiliares import colores as col
from Auxiliares import dibujar as dib
from Bezier.curvas import curva_bezier
from Bezier.curvas import dibuja_bezier

def pantalla_interactiva():
    # acomodar
    fig, ax = plt.subplots()
    fig.patch.set_facecolor(col.fondo)
    dib.configurar_ejes(ax) 
    ax.text(
        9.5, -0.5,
        "Presiona 'l' para iniciar animacion",
        fontsize=10, color=col.blanco, ha="right", va="top"
    )
    # datos 
    puntos = []
    scatter = None
    punto_actual = None 


    def actualizar_grafico(conBezi = True ):
        # acomodar
        nonlocal scatter
        ax.clear()
        dib.configurar_ejes(ax) 
        ax.text(
            9.5, -0.5,
            "Presiona 'l' para iniciar animacion",
            fontsize=10, color=col.blanco, ha="right", va="top"
        )
        
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
        if( conBezi ):
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
    
    


    def animar_bezier():
        if len(puntos) < 2:
            print("Se necesitan al menos dos puntos para generar una curva.")
            return

        # Generar las divisiones progresivas para la curva de Bézier
        curva = curva_bezier(puntos, cantidad=100)
        intermedios = []  # Lista para almacenar las posiciones intermedias

        def calcular_intermedios(puntos, t):
            if len(puntos) == 1:
                return puntos
            nuevos_puntos = []
            for i in range(len(puntos) - 1):
                x = (1 - t) * puntos[i][0] + t * puntos[i + 1][0]
                y = (1 - t) * puntos[i][1] + t * puntos[i + 1][1]
                nuevos_puntos.append([x, y])
            return nuevos_puntos

        # Calcular todas las iteraciones
        nn = 100
        for t in range(nn+1):
            t_normalizado = t / nn
            nivel_actual = puntos[:]
            niveles = []
            while len(nivel_actual) > 1:
                nivel_actual = calcular_intermedios(nivel_actual, t_normalizado)
                niveles.append(nivel_actual)
            intermedios.append(niveles)

        # Función para actualizar el gráfico en cada cuadro
        def update(frame):
            nonlocal scatter
            ax.clear()
            dib.configurar_ejes(ax)
            actualizar_grafico(conBezi=False)

            # colores
            colores_niveles = [col.verde, col.azul, col.rojo, col.morado, col.amarillo]

            # las de enmedio
            for nivel_idx, nivel in enumerate(intermedios[frame]):
                tam = 10
                if( nivel_idx == len(intermedios[frame] )  -1 ):
                    tam = 40

                x_nivel = [p[0] for p in nivel]
                y_nivel = [p[1] for p in nivel]
                color_nivel = colores_niveles[nivel_idx % len(colores_niveles)] 

                # linea
                ax.plot(x_nivel, y_nivel, color=color_nivel, linewidth=1)

                # inicio y fin
                ax.scatter(x_nivel[0], y_nivel[0], color=col.blanco, edgecolor=color_nivel, s=tam, zorder=5, label="Inicio")
                ax.scatter(x_nivel[-1], y_nivel[-1], color=col.blanco, edgecolor=color_nivel, s=tam, zorder=5, label="Fin")

            # curva bezier grado i
            x_curve = [curva[i][0] for i in range(frame + 1)]
            y_curve = [curva[i][1] for i in range(frame + 1)]
            ax.plot(x_curve, y_curve, color=col.azul, linewidth=2)
            punto_actual = [curva[frame][0], curva[frame][1]]
            ax.scatter(punto_actual[0], punto_actual[1], color=col.rojo, s=tam)

            fig.canvas.draw()

        # aniamcion como variable global
        global anim
        anim = FuncAnimation(fig, update, frames=len(intermedios), interval=25, repeat=False)
        plt.show()


        # eliminar
    def on_key(event): 
        nonlocal punto_actual
        # tecla D eliminar
        if event.key == 'd' and punto_actual is not None: 
            print(f"se elimino {puntos[punto_actual]}")
            puntos.pop(punto_actual)
            punto_actual = None
            actualizar_grafico()
        
        # tresionar l  iniciar la animación
        if event.key == 'l': 
            animar_bezier()
    
    # que se mueva
    def on_motion(event):
        if punto_actual is not None and event.xdata is not None and event.ydata is not None:
            puntos[punto_actual] = [event.xdata, event.ydata]
            actualizar_grafico()

    # Conectar eventos
    fig.canvas.mpl_connect("button_press_event", on_click)
    fig.canvas.mpl_connect("key_press_event", on_key)
    fig.canvas.mpl_connect("motion_notify_event", on_motion)
    plt.show()
    plt.show()

    return puntos

if __name__ == "__main__":
    pantalla_interactiva()