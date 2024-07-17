import numpy as np
import pandas as pd

#dx/dw=0.00536y[1-x/(1-0.148*x)]
#dy/dw=-0.0184*(1-0.148*x)/y

def edo(t,w,b,c,d):
    x,y=t
    dydt=[b*y*(1-x/(1-c*x)),d*((1-(c*x))/y)]
    return dydt

#Constantes do Sistema
b=0.0536
c=0.148
d=-0.0184

#Condições Iniciais
y0=[0,1]
w=np.linspace(0,21,22)

#Resolvendo o Sistema

from scipy.integrate import odeint
sol=odeint(edo,y0,w,args=(b,c,d))
#print(sol)
#print(w)


#Armazenar resultados em uma planilha
#from pandas import DataFrame
massa=w
x=sol[:,0]
y=sol[:,1]
df=pd.DataFrame({"W(kg)":massa, "x(massa)":x,"y(conversão)":y})
df.to_excel("SistEdo4.0.xlsx",sheet_name="sheet1",index=False)

#Mostrando Dados do gráfico
tabela=pd.DataFrame({"M":massa,"X(conversão)":sol[:,0],"Y(Queda de P)":sol[:,1]})
print(tabela)

#Criando Gráfico
import matplotlib.pyplot as plt
plt.title("Reator PBR",color="blue") #Color do título
plt.xlabel("Massa de catalisador",color="black") # Eixo Horizontal
plt.ylabel("Conversão Queda de Pressão",color="black") # Eixo Vertical
plt.rcParams['figure.figsize'] = (16,10.5)
plt.plot(w,sol[:,0],"--", label="(Massa de Catalisador)",color="Springgreen") #legenda dos Eixos
plt.plot(w,sol[:,1],"--", label="(Conversão)",color="black") #legenda dos Eixos
plt.legend(loc="best")  #legenda no melhor lugar
plt.grid(True)
plt.savefig("GRF_EDO.pdf")  #Salvando o gráfico em pdf
plt.show()

