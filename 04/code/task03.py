import matplotlib.pyplot as plt
import numpy as np

x1s, y1s = [], []
x2s, y2s = [], []

A = 0

N = 100000
for _ in range(N):
    x = np.random.uniform(-1, 1)
    y = np.random.uniform(-1, 1)
    if x**2 + y**2 <= 1:
        A += 1
        x1s.append(x)
        y1s.append(y)
    else:
        x2s.append(x)
        y2s.append(y)

z = 4 * A / N
print(z)

plt.figure(figsize=(6, 6))
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(x1s, y1s, color='red', s=.2, label=r'$x^2+y^2\leq1$')
plt.scatter(x2s, y2s, color='blue', s=.2, label=r'$x^2+y^2<1$')
# plt.legend(loc='upper right')
plt.savefig(f'../figures/task_03_N{N}')
