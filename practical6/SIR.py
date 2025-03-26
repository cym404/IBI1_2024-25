import numpy as np
import matplotlib.pyplot as plt
N=10000
beta=0.3
gamma=0.05
##// Initialize parameters
#N = 10000 // Total population size
#beta = 0.3 // Infection rate
#gamma = 0.05 // Recovery rate
#S = N - 1 // Initial number of susceptible individuals, 1 infected
#I = 1 // Initial number of infected individuals
#R = 0 // Initial number of recovered individuals
#t_steps = 1000 // Number of time steps

#// Create arrays to store the number of individuals in each state over time
#susceptible_array = [S]
#infected_array = [I]
#recovered_array = [R]

#// Time loop
#for each time_step from 1 to t_steps
 #   // Calculate new infections
  #  new_infections = 0
   # for each susceptible_person in S
    #    infection_probability = beta * (I / N)
     #   if a random number between 0 and 1 is less than infection_probability
      #      new_infections = new_infections + 1
    
    #// Calculate new recoveries
    #new_recoveries = 0
    #for each infected_person in I
     #   recovery_probability = gamma
      #  if a random number between 0 and 1 is less than recovery_probability
       #     new_recoveries = new_recoveries + 1
    
    #// Update the number of individuals in each category
    #S = S - new_infections
    #I = I + new_infections - new_recoveries
    #R = R + new_recoveries
    
    #// Store the results for the current time step
    #append S to susceptible_array
    #append I to infected_array
    #append R to recovered_array

#// Plotting (pseudocode indication)
#plot susceptible_array with label "susceptible"
#plot infected_array with label "infected"
#plot recovered_array with label "recovered"
#add x - label "Time step"
#add y - label "Number of people"
#add title "SIR model"
#display legend
I0=1
S0=N-I0
R0=0
S=[S0]
I=[I0]
R=[R0]
t_steps=1000

for _ in range(t_steps):
    new_infections = np.random.choice([0, 1], size=S[-1], p=[1 - (beta * I[-1] / N), (beta * I[-1] / N)]).sum()
    new_recoveries = np.random.choice([0, 1], size=I[-1], p=[1 - gamma, gamma]).sum()
    S.append(S[-1] - new_infections)
    I.append(I[-1] + new_infections - new_recoveries)
    R.append(R[-1] + new_recoveries)
plt.plot(S, label='susceptible')
plt.plot(I, label='infected')
plt.plot(R, label='recovered')
plt.xlabel('Time step')
plt.ylabel('Number of people')
plt.title('SIR model')
plt.legend()
plt.show()