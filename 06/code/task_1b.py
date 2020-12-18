import matplotlib.pyplot as plt
from numpy import log, cosh, tanh, linspace, logspace


kB, N, F, a = 1, 1, 1, 1


def entropy(T):

    foo = F * a / (kB * T)
    bar = kB * N * log(2 * cosh(foo)) - tanh(foo) * N * F * a / T

    return bar


T = linspace(1, 1e2, 1000)
S = entropy(T)

plt.plot(T, S)
plt.savefig('../figures/entropy.pdf')
