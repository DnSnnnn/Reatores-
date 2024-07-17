import numpy as np
import matplotlib.pyplot as plt

# Definir parâmetros
a = 0
b = 21
N = 1000
h = (b-a)/N

# Definir funções
def f1(x,y):
    return 0.0536*y*(1-x/(1-0.148*x))

def f2(x,y):
    return -0.0184*(1-0.148*x)/y

# Definir condições iniciais
x = 0
y = 1

# Inicializar arrays para soluções
w = np.zeros(N+1)
X = np.zeros(N+1)
Y = np.zeros(N+1)

# Definir valores iniciais
w[0] = a
X[0] = x
Y[0] = y

# Implementar método de Runge-Kutta
for i in range(N):
    k1 = h * f1(X[i], Y[i])
    l1 = h * f2(X[i], Y[i])
    k2 = h * f1(X[i] + 0.5*h, Y[i] + 0.5*k1)
    l2 = h * f2(X[i] + 0.5*h, Y[i] + 0.5*l1)
    k3 = h * f1(X[i] + 0.5*h, Y[i] + 0.5*k2)
    l3 = h * f2(X[i] + 0.5*h, Y[i] + 0.5*l2)
    k4 = h * f1(X[i] + h, Y[i] + k3)
    l4 = h * f2(X[i] + h, Y[i] + l3)
    X[i+1] = X[i] + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
    Y[i+1] = Y[i] + (1/6)*(l1 + 2*l2 + 2*l3 + l4)
    w[i+1] = w[i] + h

# Traçar soluções
plt.plot(w, X,"--", label='x',color="blue")
plt.plot(w, Y,"--", label='y',color="green")
plt.xlabel('w')
plt.legend()
plt.show()