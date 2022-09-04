import matplotlib.pyplot as plt
import math
import random

n = int(input())
mu = int(input())
sigma = int(input())
x = []
for i in range(-50, 51):
    x.append(random.gauss(mu, sigma))
plt.hist(x, color='lime', bins=int(math.sqrt(n)))
plt.xlabel('Значение', fontsize=16)
plt.ylabel('Высота', fontsize=16)
plt.title('Распределение Гаусса', fontsize=16)
plt.grid(True)
plt.show()
