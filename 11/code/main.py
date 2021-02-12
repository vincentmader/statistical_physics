import random

from colour import Color
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm


J = 1
k_B = 1
N = 32
temperatures = [0.5, 1.5, 2.5, 3]


def initialize_spins(N):

    grid = np.ndarray((N, N))
    for i in range(N):
        for j in range(N):
            grid[i][j] = random.choice([-1, +1])

    return grid


def apply_periodic_bounds(cell_idx, N):

    if cell_idx >= N:
        cell_idx -= N
    elif cell_idx < 0:
        cell_idx += N

    return cell_idx


def get_flip_energy(grid, i, j):

    H = 0
    for di in [-1, 1]:
        for dj in [-1, 1]:
            H += - J * grid[
                apply_periodic_bounds(i + di, N)
            ][
                apply_periodic_bounds(j + dj, N)
            ]

    return H


def get_magnetization(grid):
    N = grid.shape[0]

    magnetization = 0
    for i in range(N):
        for j in range(N):
            magnetization += grid[i][j]

    return magnetization / N**2


def flip_random_spin(grid, T):

    def boltzmann_prob(dE, T):
        beta = 1 / (k_B * T)
        return np.exp(-beta * dE)

    i = random.choice(range(N))
    j = random.choice(range(N))
    flip = False

    dE = get_flip_energy(grid, i, j)
    if dE < 0:  # flip spin
        flip = True
    if dE > 0:  # TODO: >= 0?
        if random.uniform(0, 1) < boltzmann_prob(dE, T):
            flip = True

    if flip:
        grid[i][j] = not grid[i][j]
    return grid


def plot_magnetizations(magnetizations):

    def get_color_gradient(from_color, to_color, nr_of_samples):
        gradient = Color(from_color).range_to(Color(to_color), nr_of_samples)
        colors = [c.rgb for c in gradient]
        return colors

    colors = get_color_gradient('green', 'red', len(temperatures))
    for idx, magnetization in enumerate(magnetizations):
        T = temperatures[idx]
        plt.plot(
            magnetization,
            label=f'$T={T}$',
            color=colors[idx],
        )

    plt.ylabel(r'magnetization $\langle M\rangle$')
    plt.legend(loc='lower right')
    plt.savefig('../figures/magnetization_vs_time.pdf')


def main():

    magnetizations = []
    for T in temperatures:
        grid = initialize_spins(N)
        magnetization = []
        for run_idx in tqdm(range(60)):
            for _ in range(N**2):
                grid = flip_random_spin(grid, T)
            magnetization.append(get_magnetization(grid))
        magnetizations.append(magnetization)

    plot_magnetizations(magnetizations)


if __name__ == "__main__":
    main()
