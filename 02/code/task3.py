import random

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


# def gaussian(x, p):
#     return p[0] * np.exp(-((x-p[1])/p[2])**2) / ((2*np.pi)**.5 * p[2])


# Ns = [10, 100, 1000]

# rs = []
# plt.figure(figsize=(5, 5))

# for N in Ns:

#     for i in range(N):
#         r = random.uniform(-1, 1) + random.uniform(-1, 1)
#         rs[r] = rs[r] + 1 if r in rs.keys() else 1
#     print(rs)

#     x = list(rs.keys())
#     y = list(rs.values())
#     plt.bar(x, y)
#     # plt.hist(rs, bins=20, width=.12)
#     plt.savefig(f'{N}.pdf')
#     plt.close()


M = 1000

for N in [10, 100, 1000]:
    rs = []
    for _ in range(M):
        r = 0
        for i in range(N):
            r += random.uniform(-1, 1)
        rs.append(r / N)

    plt.figure(figsize=(4, 4))
    plt.tight_layout(True)
    plt.xlim(-0.6, 0.6)
    plt.ylim(0, 140)
    plt.xticks([-.5, -.25, 0, .25, .5], size=14)
    plt.yticks(size=14)
    # plt.xlabel('value of random sum', fontsize=14)
    # plt.xlabel('count', fontsize=14)
    plt.hist(rs, bins=20)
    plt.savefig(f'../figures/{N}.pdf')
    plt.close()
