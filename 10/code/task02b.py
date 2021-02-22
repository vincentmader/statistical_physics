import matplotlib.pyplot as plt
import numpy as np
from numpy import cosh, sinh


def M(x):
    return cosh(x)/sinh(x) - 1/x


x = np.linspace(0, 100)

plt.plot(x, M(x))
plt.xlabel(r'$x$')
plt.ylabel(r'$\coth(x)-\frac{1}{x}$')
plt.savefig('../figures/magnetization.pdf')
