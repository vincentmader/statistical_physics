import matplotlib.pyplot as plt
import numpy as np
from numpy import log, cosh


def K_new(K):
    return log(cosh(2*K)) / 2


def g(K):
    return log(2) / 2 + log(cosh(2*K)) / 4


Ks = [1]
for i in range(40):
    Ks.append(K_new(Ks[i]))
gs = []
for K in Ks:
    gs.append(g(K))

print([round(k, 2) for k in Ks[:5]])
print([round(g, 2) for g in gs[:5]])


plt.figure(figsize=(4, 4))
plt.plot(Ks)
plt.xlabel('$i$')
plt.ylabel('$K_i$')
plt.xlim(0, 30)
plt.ylim(0, 1)
plt.savefig('../figures/K_series.pdf')
plt.close()

plt.figure(figsize=(4, 4))
plt.plot(gs)
plt.xlabel('$i$')
plt.ylabel('$K_i$')
plt.xlim(0, 30)
plt.ylim(0, 1)
plt.savefig('../figures/g_series.pdf')
plt.close()
