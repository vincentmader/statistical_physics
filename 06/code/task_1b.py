import matplotlib.pyplot as plt
from numpy import log, cosh, tanh, linspace, logspace


kB, N, a, T = 1.38e-23, 1e4, 1, 1e4


def F(X):
    return -X / (N * a**2) * kB * T


def entropy(X):

    foo = F(X) * a / (kB * T)
    bar = log(2 * cosh(foo)) - tanh(foo) * F(X) * a / (kB * T)

    return kB * N * bar


X = linspace(0, 1, 1000)
S = entropy(X) / (kB * N)

plt.plot(X, S)
plt.savefig('../figures/entropy.pdf')
