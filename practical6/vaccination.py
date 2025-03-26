import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

N = 10000  
beta = 0.3  
gamma = 0.05  
I0 = 1  
t_steps = 1000  
vaccination_rates = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
for rate in vaccination_rates:
    S0 = int(N * (1 - rate))  
    V0 = N - S0  
    I0 = 1  
    R0 = 0  
    S = [S0]
    I = [I0]
    R = [R0]
    V = [V0]

    for _ in range(t_steps):
        if (N-V[-1])!=0:
            new_infections = np.random.choice([0, 1], size=S[-1], p=[1 - (beta * I[-1] / (N - V[-1])), (beta * I[-1] / (N - V[-1]))]).sum()
            new_recoveries = np.random.choice([0, 1], size=I[-1], p=[1 - gamma, gamma]).sum()

        S.append(S[-1] - new_infections)
        I.append(I[-1] + new_infections - new_recoveries)
        R.append(R[-1] + new_recoveries)
        V.append(V[-1])
    plt.plot(I, label=f'{rate * 100}%', c=cm.viridis(int(rate * 10 * 9)))
plt.xlabel('Time step')
plt.ylabel('Number of infected people')
plt.title('SIR model with different vaccination rates')
plt.legend()
plt.show()