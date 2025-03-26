# Model parameters
#beta = 0.3  # Infection rate
#gamma = 0.05  # Recovery rate
#t_steps = 100  # Number of time steps
#vaccination_rate = 0.2  # Vaccination rate

# Create a 100x100 population array, all susceptible initially (0)
#population = Array(100, 100) initialized with 0

# Randomly vaccinate some people (mark as 3)
#num_to_vaccinate = 100 * 100 * vaccination_rate
#vaccinated_indices = Randomly choose num_to_vaccinate distinct indices from 0 to 9999
#for each index in vaccinated_indices:
  #  i, j = index / 100 (get row and col indices)
 #   population[i, j] = 3

# Randomly select an initial infected person (not vaccinated, mark as 1)
#outbreak = Randomly choose a pair of indices from 0 to 99
#while population[outbreak[0], outbreak[1]] == 3:
 #   outbreak = Randomly choose a pair of indices from 0 to 99
#population[outbreak[0], outbreak[1]] = 1

# Simulation loop for disease spread
#for each time_step in range(t_steps):
    #new_infections = []
    #new_recoveries = []
    #for i in range(100):
        #for j in range(100):
            #if population[i, j] == 1:  # Infected
           #     # Try to infect neighbors
          #      for x in range(max(0, i - 1), min(100, i + 2)):
         #           for y in range(max(0, j - 1), min(100, j + 2)):
        #                if population[x, y] == 0 and random number between 0 and 1 < beta:
       #                     new_infections.append((x, y))
                # Check for recovery
      #          if random number between 0 and 1 < gamma:
     #               new_recoveries.append((i, j))

    # Update population based on new infections and recoveries
    #for each (x, y) in new_infections:
    #    population[x, y] = 1
  #  for each (x, y) in new_recoveries:
   #     population[x, y] = 2  # Recovered

# Plot the result
#Create a plot with size (6, 4) and dpi 150
#lot the population array with 'viridis' colormap and nearest interpolation
#Show the plot

import numpy as np
import matplotlib.pyplot as plt

# 模型参数
beta = 0.3  # 感染率
gamma = 0.05  # 康复率
t_steps = 100  # 时间步数

# 创建全是易感者的100x100数组
population = np.zeros((100, 100))

# 随机选择一个初始感染者
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1

# 绘制初始状态
plt.figure(figsize=(6, 4), dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.show()

# 模拟疾病传播
for _ in range(t_steps):
    new_infections = []
    new_recoveries = []
    for i in range(100):
        for j in range(100):
            if population[i, j] == 1:  # 如果是感染者
                # 感染邻居
                for x in range(max(0, i - 1), min(100, i + 2)):
                    for y in range(max(0, j - 1), min(100, j + 2)):
                        if population[x, y] == 0 and np.random.rand() < beta:
                            new_infections.append((x, y))
                # 康复
                if np.random.rand() < gamma:
                    new_recoveries.append((i, j))
    for x, y in new_infections:
        population[x, y] = 1
    for x, y in new_recoveries:
        population[x, y] = 2

    # 每10个时间步绘制一次结果
    if _ % 10 == 0:
        plt.figure(figsize=(6, 4), dpi=150)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.show()