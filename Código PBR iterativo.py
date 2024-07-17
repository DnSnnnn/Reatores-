from IPython.display import display
import ipywidgets as widgets
import numpy as np
import pandas as pd
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Definir a função que resolve o sistema de equações diferenciais
def edo(t,w,b,c,d):
    x,y=t
    dydt=[b*y*(1-x/(1-c*x)),d*((1-(c*x))/y)]
    return dydt

# Definir as constantes do sistema
b=0.0536
c=0.148
d=-0.0184

# Definir as condições iniciais
y0=[0,1]

# Criar um widget para a variável w
w_slider = widgets.FloatSlider(min=0, max=21, step=0.1, value=10.5, description="w")

# Criar uma função que plota o resultado da solução do sistema de equações diferenciais usando o valor do widget
@widgets.interact(w=w_slider)
def plot_result(w):
    # Resolver o sistema de equações diferenciais usando o valor do widget
    sol = odeint(edo,y0,[0,w],args=(b,c,d))
    # Plotar o resultado usando matplotlib
    plt.title("Reator PBR",color="blue") #Color do título
    plt.xlabel("Massa de catalisador",color="black") # Eixo Horizontal
    plt.ylabel("Conversão Queda de Pressão",color="black") # Eixo Vertical
    plt.rcParams['figure.figsize'] = (16,10.5)
    plt.plot([0,w],sol[:,0],"--", label="(Massa de Catalisador)",color="Springgreen") #legenda dos Eixos
    plt.plot([0,w],sol[:,1],"--", label="(Conversão)",color="black") #legenda dos Eixos
    plt.legend(loc="best")  #legenda no melhor lugar
    plt.grid(True)
    plt.show()
