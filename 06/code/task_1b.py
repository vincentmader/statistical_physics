import matplotlib.pyplot as plt
from numpy import log, cosh, tanh, linspace, logspace


kB, N, a, T = 1.38e-23, 1e7, 1, 1e4
E = 1


def F(X):
    return -E / X
    # return -X / (N * a**2) * kB * T


def entropy(X):

    foo = F(X) * a / (kB * T)
    bar = log(2 * cosh(foo)) - tanh(foo) * foo

    return kB * N * bar


X = linspace(1, N * a, 1000)
S = entropy(X)

plt.plot(X, S / (kB * N))
plt.xticks(
    [0, 0.2 * N, 0.4 * N, 0.6 * N, 0.8 * N, N],
    [0, 0.2, 0.4, 0.6, 0.8, 1]
)
plt.xlim(0, N)
plt.ylim(0, 1)
plt.xlabel('$X / L_0$')
plt.ylabel(f'$S / (N \cdot k_B)$')
plt.savefig('../figures/entropy.pdf')
