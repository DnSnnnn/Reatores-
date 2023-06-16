# Reator CSTR
# Operação Adiabática De Reator Contínuo
        # A ---> B
#Hipotéses
    #--> Estado Estacionario
    #--> Sem mudança de fase
    #--> Reação Irreversível
from math import*
import numpy as np
import matplotlib.pyplot as plt
#Dados do problema
Fao = 5         #mol/min
To  = 300       #K
Fi  = 10        #mol/min
Cao = 2         #mol/min
Cpa = 164       #cal/mol
Cpb = 164       #cal/mol
Cpi = 18        #cal/mol
k0  = 0.1       #Constante Cinética a 298K [1/min]
Ea  = 10000     #Energia de Ativação [cal/mol]
DHrxn = -20000  #Delta H de reação [cal/mol.A]
R   = 1.987     #Constante dos gases [cal]

#Equacionamento
# 1) Balanço de Massa(CSTR, Reação de 1° Ordem)
        #Fao - Fa + (-ra)*V=0
# 2) Cinética
        # ra = K * Ca
        # k = ko*exp[Ea/R*(1/To-1/T)]  Equação de Arrhenius
# 3) Estequiométria
        # Ca = Cao(1-x)
        # Fa = Fao*(1-x)
# 4) Balanço de Energia
        # T = To + DHrxn*xa/(theta(i)*Cpi)
        # x = ∑(theta(i)*Cpi) *(T-To)/(-DHrxn)

# A) Qual o volume do reator necessário para alcançar 80% de conversão?
x=0.80
        # V = Fao - Fao(1 - x) / k * Cao * (1 - x)

#--> Aplicando Balanço de Energia para determinar a temperatura 
    #theta(a) = 1  -->Apenas um reagente 
    #theta(b) = 0  -->Produto, logo a relação Fbo/Fao = 0
    #theta(i) = Fio/Fao 
    #∑(theta(i)*Cpi) = Cpa * 1 + Cpi*(Fio/Fao)

T = To + (-DHrxn*x)/ (Cpa*1 + Cpi*(Fi/Fao))
#print(T)

# --> Aplicando a lei de Arrhenius para determinar o k
k = k0*exp(Ea/R*(1/298-1/T))
#print(k)

# --> Determinado o Volume 
V = (Fao - (Fao*(1 - x))) / (k * Cao * (1 - x))
#print(V)


# B) Se a temperatura do reator é 360K, qual o volume do reator?
#--> Aplicando Bal
# anço de Energia para determinar a conversão 
    #theta(a) = 1  -->Apenas um reagente 
    #theta(b) = 0  -->Produto, logo a relação Fbo/Fao = 0
    #theta(i) = Fio/Fao 
    #∑(theta(i)*Cpi) = Cpa * 1 + Cpi*(Fio/Fao)
    # x = ∑(theta(i)*Cpi) *(T-To)/(-DHrxn)
x = (Cpa*1 + Cpi *(Fi/Fao))*(360 - 300)/(-DHrxn)
#print(x) 

k = k0*exp(Ea/R*(1/298-1/360))
#print(k)

# --> Determinado o Volume 
V = (Fao - (Fao*(1 - x))) / (k * Cao * (1 - x))
#print(V)

# C) Gráfico de Levenspiel
x = np.linspace(0,0.97,12)
T_list = []
k_list = []
for i in x: 
    T = 300 + (-DHrxn*x)/ (Cpa*1 + Cpi*(Fi/Fao))
    k = k0 * np.exp(Ea/R*(1/298 - 1/T ))
    ra = k * (Cao*(1-x))
    FaoRa = Fao/ra
    #T_list.append(T)
    #k_list.append(k)
# Gerando Gráfico de Levenspiel
plt.title("Gráfico de Levenspiel",color="blue") #Color do título
plt.xlabel("Conversão",color="black") # Eixo Horizontal
plt.ylabel("Fao/(Ra)",color="black") # Eixo Vertical
plt.plot(x,FaoRa,"--",color="springgreen")
plt.grid(True)
plt.show()
