import matplotlib.pyplot as plt
from Auxiliares import colores as col

# configurar parametros tipo Manim
plt.rcParams['font.family'] = 'serif'  
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['mathtext.rm'] = 'serif'



def configurar_ejes(ax):
    blanco = col.blanco
    ax.set_facecolor(col.fondo)
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

