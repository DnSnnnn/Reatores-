import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

# Definindo a função que representa a equação diferencial
def edo(t,w,Cao,T,Cpa,theta,Cpi,To,e,k):
    x,y=t
    dydt=[(-k*Cao1*(1-x)*To/(1+e*x)/T),(x*(-dHrx)+(Cpa+theta*Cpi)*To)/(Cpa+theta*Cpi)]
    return dydt

#Condições Iniciais
x0=[0,1]
w=np.linspace(0,500,501)
# Definindo os parâmetros e o valor inicial
Cao = 2/.082/1100
Cio = Cao
theta = 100
Fao = 10
Cao1 = (Cao+Cio)/(theta+1)
e = 1/(1+theta)
To = 1100
dHrx = 80000
Cpa = 170
Cpi = 200
T = (x0*(-dHrx)+(Cpa+theta*Cpi)*To)/(Cpa+theta*Cpi)
k = np.exp(34.34-34222/np.array(T))
x=[0,T]

"""#Resolvendo o Sistema

from scipy.integrate import odeint
sol=odeint(edo,x,w,args=((Cao,T,Cpa,theta,Cpi,To,e,k)))
print(sol)
print(w)"""



