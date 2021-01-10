import matplotlib.pyplot as plt
from tqdm import tqdm


def color_gradient(idx, nr_of_steps):
    r = int(255 * (1 - idx / nr_of_steps))
    g = int(255 * idx / nr_of_steps)

    r = hex(r)[2:]
    g = hex(g)[2:]

    r = f'0{r}' if len(r) == 1 else r
    g = f'0{g}' if len(g) == 1 else g

    return f'#{r}{g}00'


def main(trajectory, nr_of_steps, filename):

    plt.figure(figsize=(8, 8))
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xticks([])
    plt.yticks([])

    for idx, (x, y) in tqdm(enumerate(trajectory)):

        color = color_gradient(idx, nr_of_steps)

        if idx != 0:
            plt.plot(
                [x, trajectory[idx-1][0]],
                [y, trajectory[idx-1][1]],
                color=color
            )
        plt.scatter(
            x, y,
            color=color if idx not in [0, nr_of_steps-1] else 'k',
            s=20 if idx not in [0, nr_of_steps-1] else 50
        )

    # min_x = min(i[0] for i in trajectory)
    # max_x = max(i[0] for i in trajectory)
    # min_y = min(i[1] for i in trajectory)
    # max_y = max(i[1] for i in trajectory)
    # s = max(max_x-min_x, max_y-min_y)
    # plt.xlim(-s, s)
    # plt.ylim(-s, s)

    plt.savefig(f'../figures/{filename}.pdf')
