import numpy as np

from plot_MSD_vs_step_num import main as plot_MSD_vs_step_num
from calc_random_walk_trajectory import main as calc_random_walk_trajectory
from plot_trajectory import main as plot_trajectory


def main(nr_of_steps=30, self_avoiding=True):

    seed = 42069
    # seed = np.random.get_state()[1][0]
    np.random.seed(seed=seed)
    # print(seed)

    trajectory = calc_random_walk_trajectory(nr_of_steps, self_avoiding)
    if self_avoiding:
        while trajectory is None:
            trajectory = calc_random_walk_trajectory(
                nr_of_steps, self_avoiding
            )

    filename = 'SAW' if self_avoiding else 'RW'
    plot_trajectory(trajectory, nr_of_steps, filename)


if __name__ == "__main__":
    # main(nr_of_steps=300, self_avoiding=False)
    # main(nr_of_steps=30, self_avoiding=True)
    plot_MSD_vs_step_num(500)
