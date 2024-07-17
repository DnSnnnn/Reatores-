#Caso 1 temperatura a 651°K
import numpy as np
import pandas as pd

#dx/dw=0.00536y[1-x/(1-0.148*x)]
#dy/dw=-0.0184*(1-0.148*x)/y

def edo(t,w,b,c):
    x,y=t
    dydt=[b*y*((1-x)/(1+x)),-c/(1-x)*y]
    #dydt=[b*y*(1-x/(1-c*x)),d*((1-(c*x))/y)]
    return dydt

#Constantes do Sistema
b=11.007
c=0.1321
#Condições Iniciais
y0=[0,1]
w=np.linspace(0,0.36,1000)

#Resolvendo o Sistema

from scipy.integrate import odeint
sol1=odeint(edo,y0,w,args=(b,c))
#print(sol)
#print(w)


#Armazenar resultados em uma planilha
#from pandas import DataFrame
massa=w
x=sol1[:,0]
y=sol1[:,1]
df=pd.DataFrame({"W(kg)":massa, "x(massa)":x,"y(conversão)":y})
#df.to_excel("SistEdo4.0.xlsx",sheet_name="sheet1",index=False)

#Mostrando Dados do gráfico
tabela=pd.DataFrame({"M":massa,"X(conversão)":sol1[:,0],"Y(Queda de P)":sol1[:,1]})
print(tabela)

#Criando Gráfico
import matplotlib.pyplot as plt
plt.title("Reator PBR",color="blue") #Color do título
plt.xlabel("Massa de catalisador",color="black") # Eixo Horizontal
plt.ylabel("Conversão/Queda de Pressão",color="black") # Eixo Vertical
plt.rcParams['figure.figsize'] = (16,11)
plt.plot(w,sol1[:,0],"--", label="(Massa de Catalisador)",color="Springgreen") #legenda dos Eixos
plt.plot(w,sol1[:,1],"--", label="(Conversão)",color="black") #legenda dos Eixos
plt.legend(loc="best")  #legenda no melhor lugar
plt.grid(True)
plt.savefig("GRF_EDO.pdf")  #Salvando o gráfico em pdf
plt.show()

#Caso 2 temperatura a 621°K
import numpy as np
import pandas as pd

def edo2(t,w,d,e):
    x,y=t
    dydt=[d*y*((1-x)/(1+x)),-e/(1-x)*y]
    #dydt=[b*y*(1-x/(1-c*x)),d*((1-(c*x))/y)]
    return dydt

#Constantes do Sistema
d=9.75
e=0.12
y0=[0,1]
w2=np.linspace(0,0.43,10)
#Resolvendo o Sistema

from scipy.integrate import odeint
sol2=odeint(edo2,y0,w2,args=(d,e))
print(sol2)
print(w2)

#Mostrando Dados do gráfico
massa=w2
tabela=pd.DataFrame({"M":massa,"X(conversão)":sol2[:,0],"Y(Queda de P)":sol2[:,1]})
print(tabela)