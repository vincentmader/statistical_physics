import random

from colour import Color
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm


random.seed(7)

J = 1
k_B = 1
N = 32


def initialize_spins(N):

    grid = np.ndarray((N, N))
    for i in range(N):
        for j in range(N):
            grid[i][j] = random.choice([-1, +1])

    return grid


def get_flip_energy(grid, i, j):

    def apply_periodic_bounds(cell_idx, N):
        if cell_idx >= N:
            cell_idx -= N
        elif cell_idx < 0:
            cell_idx += N
        return cell_idx

    dE = 0  # calculate energy difference after flip
    for di in [-1, 0, 1]:  # loop over neighbors
        for dj in [-1, 0,  1]:
            if di == dj == 0:
                continue  # no self-interaction
            # get row/col index for neighbor
            i_neighbor = apply_periodic_bounds(i+di, N)
            j_neighbor = apply_periodic_bounds(j+dj, N)
            # get spin of neighbor
            s_neighbor = grid[i_neighbor][j_neighbor]
            # subtract current state's energy, add new state's energy
            dE -= -J * s_neighbor * grid[i][j]
            dE += -J * s_neighbor * (-grid[i][j])

    return dE


def flip_random_spin(grid, T):

    def boltzmann_prob(dE, T):
        beta = 1 / (k_B * T)
        return np.exp(-beta * dE)

    # choose random grid cell
    i, j = random.choice(range(N)), random.choice(range(N))
    dE = get_flip_energy(grid, i, j)

    flip = False
    if dE < 0:  # flip spin
        flip = True
    if dE >= 0:  # flip only with Boltzmann probability
        if random.uniform(0, 1) < boltzmann_prob(dE, T):
            flip = True

    if flip:
        grid[i][j] *= -1
    return grid


def get_magnetization(grid):
    N = grid.shape[0]

    magnetization = 0
    for i in range(N):  # sum over all spins
        for j in range(N):
            magnetization += grid[i][j]

    return magnetization / N**2


def plot_magnetizations(magnetizations, temperatures):

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

    plt.xlabel('nr. of spin flips / $N^2$')
    plt.ylabel(r'magnetization $\langle M\rangle$')
    plt.legend(loc='lower right')
    plt.savefig('../figures/magnetization_vs_time.pdf')


def main():

    temperatures = [1.5, 3]

    magnetizations = []
    for T in temperatures:
        grid = initialize_spins(N)

        magnetization = []
        for run_idx in tqdm(range(300)):
            for _ in range(N**2):
                grid = flip_random_spin(grid, T)
            magnetization.append(get_magnetization(grid))
        magnetizations.append(magnetization)

    plot_magnetizations(magnetizations, temperatures)


if __name__ == "__main__":
    main()
