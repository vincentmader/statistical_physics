import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

from calc_random_walk_trajectory import main as calc_random_walk_trajectory


def main(step_num, self_avoiding=False):

    MSDs = []
    for n in tqdm(range(1, step_num+1, 2)):
        squared_displacements = []
        for i in range(100):
            print(i)
            trajectory = None
            while trajectory is None:
                trajectory = calc_random_walk_trajectory(n, self_avoiding)
            squared_displacement = trajectory[-1][0]**2 + trajectory[-1][1]**2
            squared_displacements.append(squared_displacement)
        MSDs.append(np.mean(squared_displacements))

    np.savetxt('./MSDs.txt', MSDs)

    plt.figure(figsize=(4, 4))
    plt.plot(range(1, step_num+1, 2), MSDs)
    plt.xlabel('nr. of random steps $n$')
    plt.ylabel(r'mean squared displacement $\langle x^2\rangle$')
    # plt.xlim(0, step_num)
    # plt.ylim(0, max(MSDs))
    plt.tight_layout()
    if self_avoiding:
        plt.savefig('../figures/MSD_vs_N_SA.pdf')
    else:
        plt.savefig('../figures/MSD_vs_N.pdf')

    plt.figure(figsize=(4, 4))
    plt.loglog(range(1, step_num+1, 2), MSDs)
    # plt.scatter(range(step_num), MSDs)
    # plt.gca().set_yscale('log')
    # plt.gca().set_xscale('log')
    plt.xlabel('nr. of random steps $n$')
    plt.ylabel(r'mean squared displacement $\langle x^2\rangle$')
    # plt.xlim(0, step_num)
    # plt.ylim(0, max(MSDs))
    plt.tight_layout()
    if self_avoiding:
        plt.savefig('../figures/MSD_vs_N_loglog_SA.pdf')
    else:
        plt.savefig('../figures/MSD_vs_N_loglog.pdf')
