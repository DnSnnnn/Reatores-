import numpy as np
import matplotlib.pyplot as plt

# Definir as funções do sistema de equações diferenciais
def f(w, Z):
    x, y = Z
    dx_dw = 0.0536*y*(1-x/(1-0.148*x))
    dy_dw = -0.0184*(1-0.148*x)/y
    return [dx_dw, dy_dw]

# Definir as condições iniciais
x0 = 0
y0 = 1
Z0 = [x0, y0]

# Definir o intervalo de integração
w = np.linspace(0, 21, 20)

# Usar o método de Runge-Kutta de quarta ordem para resolver o sistema de equações
from scipy.integrate import solve_ivp
sol = solve_ivp(f, [w[0], w[-1]], Z0, t_eval=w)

# Plotar as soluções
plt.plot(sol.t, sol.y[0], label='x(w)',color="black")
plt.plot(sol.t, sol.y[1] , label='y(w)',color="r")
plt.legend(loc='best')
plt.xlabel('w')
plt.grid()
plt.show()