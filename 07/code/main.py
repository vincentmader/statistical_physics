import random

import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm


def random_step(x0, y0):

    dx = random.choice([-1, 0, 1])
    dy = random.choice([-1, 0, 1])
    x, y = x0+dx, y0+dy

    return x, y


def get_trajectory(n, self_avoiding, x=0, y=0):

    trajectory = []
    for i in range(n):
        x, y = random_step(x, y)

        if self_avoiding and (x, y) in trajectory:
            return None

        trajectory.append((x, y))

    return trajectory


def plot_trajectory(trajectory, filename):

    plt.figure(figsize=(8, 8))
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xticks([])
    plt.yticks([])
    for idx, (x, y) in tqdm(enumerate(trajectory)):
        if idx != 0:
            plt.plot(
                [x, trajectory[idx - 1][0]],
                [y, trajectory[idx - 1][1]], color='k'
            )
        color = (['g']+['k']*(len(trajectory)-2)+['r'])[idx]
        plt.scatter(x, y, color=color)

    plt.savefig(f'../figures/{filename}.pdf')


def plot_MSD_vs_n(N, self_avoiding=False):
    MSDs = []
    for n in tqdm(range(1, N+1)):
        squared_displacements = []
        for _ in range(100):
            trajectory = get_trajectory(n, self_avoiding)
            squared_displacement = trajectory[-1][0]**2 + trajectory[-1][1]**2
            squared_displacements.append(squared_displacement)
        MSDs.append(np.mean(squared_displacements))

    plt.plot(range(N), MSDs)
    plt.xlabel('nr. of random steps $n$')
    plt.ylabel(r'mean squared displacement $\langle x^2\rangle$')
    plt.savefig('../figures/MSD_vs_N.pdf')


def main(n, self_avoiding=True):

    trajectory = get_trajectory(n, self_avoiding)
    while self_avoiding and trajectory == None:
        trajectory = get_trajectory(n, self_avoiding)

    filename = 'SAW' if self_avoiding else 'RW'
    plot_trajectory(trajectory, filename)


if __name__ == "__main__":
    # main(400, self_avoiding=False)
    # main(30, self_avoiding=True)
    plot_MSD_vs_n(400)
