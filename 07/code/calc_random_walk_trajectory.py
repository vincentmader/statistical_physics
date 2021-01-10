import numpy as np


def main(nr_of_steps, self_avoiding=True, x=0, y=0):

    def random_step(x, y):
        direction = np.random.choice(['x', 'y'])
        if direction == 'x':
            dx = np.random.choice([-1, 1])
            dy = 0
        elif direction == 'y':
            dx = 0
            dy = np.random.choice([-1, 1])
        # dx = np.random.choice([-1, 0, 1])
        # dy = np.random.choice([-1, 0, 1])  # if not dx else 0
        return x+dx, y+dy

    trajectory = []
    for i in range(nr_of_steps):
        x, y = random_step(x, y)

        if self_avoiding and (x, y) in trajectory:
            return None

        trajectory.append((x, y))

    return trajectory
