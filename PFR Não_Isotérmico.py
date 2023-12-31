# Reator PFR
# Operação Adiabática De Reator Contínuo
# A ---> B + C
#Hipóteses
#--> Estado Estacionario
#--> Sem mudança de fase
#--> Reação Irreversível
#Bibliotecas
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#Dados Do Problema

Fa0 = 10                   # mol/min
Ca0 = 2/(0.082*1100)       # mol / L

v0 = Fa0 / Ca0             # Vazão volumetrica
Ft0 = Fa0

T0 = 1100                  # K
dHrx = 80000               # J/mol a 298K
Cpa = 170                  # J/mol/K
Cpb = 90                   # J/mol/K
Cpc = 80                   # J/mol/K
Cpi = 200                  # J/mol/K
Ci0 = Ca0   
theta = 100                   
e = 1/(1+theta)
To = 1100
Ca01 = (Ca0+Ci0)/(theta+1)     #Concentração Total

def adiabatic_pfr(Y, V, Fi0):
    x, T = Y 
    #T = (x*(-dHrx)+(Cpa+theta*Cpi)*To)/(Cpa+theta*Cpi) 
    k = np.exp(34.3 - 34222.0 / T)
    Ca = Ca01
    r = k * Ca01*(1-x)*T0/(1+e*x)/T
    ra = r

    dXdV = r/Fa0
    dTdV = (-dHrx * ra) / (Fa0 * Cpa + Fi0 * Cpi)

    return [dXdV, dTdV]


V = np.linspace(0, 500) # volume L
Y0 = [0, T0]


#colors = 'rgbk' 
for i, Fi0 in enumerate([10,2.5,0.0]):
    sol = odeint(adiabatic_pfr, Y0, V, args=(Fi0,))

    X = sol[:, 0]
    T = sol[:, 1]
    #X = ((Fa - Fa0) * (-1) / Fa0)

    plt.subplot(1,2,1)
    plt.plot(V, X,  label='Fi0 = {0} mol/s'.format(Fi0))
    plt.xlabel('Volume (L)')
    plt.ylabel('Conversão(%)')

    plt.subplot(1,2,2)
    plt.plot(V, T,  label='Fi0 = {0} mol/s'.format(Fi0))
    plt.xlabel('Volume (L)')
    plt.ylabel('Temperature (K)')

plt.subplot(1,2,1)
plt.legend(loc='best')

plt.subplot(1,2,2)
plt.legend(loc='best')

plt.tight_layout()

plt.show()



