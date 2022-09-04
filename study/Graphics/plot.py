import matplotlib.pyplot as plt
import cmath

k1 = len('Александр')
k2 = len('Храпов')

x1 = []
for i in range(-300, 500):
    x1.append(i*0.1)
y1 = []
for i in x1:
    y1.append((i-k1)**3 + cmath.sqrt(abs(i+k2)))
x2 = []
for i in range(-50, 51):
    x2.append(i*0.1)
y2 = []
for i in x2:
    y2.append(k1 * cmath.sin(i**5) * cmath.log(i-k2))

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(x1, y1, color=(0.3, 0.6, 0.3), linewidth=4.0)
plt.xlabel('x', fontsize=16)
plt.ylabel('y', fontsize=16)
plt.title('y = (x-k1)^3 + sqrt(|x+k2|)', fontsize=16)
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(x2, y2, color=(0.3, 0.6, 0.3), linewidth=4.0)
plt.xlabel('x', fontsize=16)
plt.ylabel('y', fontsize=16)
plt.title('y = k1 * sin(x^5) * ln(x-k2)', fontsize=16)
plt.grid(True)

plt.show()
