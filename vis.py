import os
import numpy as np
import matplotlib.pyplot as plt


def vis_func(f, start, end, name, intervals=1000):
    x_range = np.linspace(start, end, intervals)
    y_range = [f(x) for x in x_range]
    # y_range = f(x_range)
    plt.plot(x_range, y_range)
    plt.title(name)
    out_dir = 'out'
    os.makedirs(out_dir, exist_ok=True)
    plt.savefig('out/{}.png'.format(name))
    plt.show()


if __name__ == '__main__':
    vis_func(np.sin, -5, 5, 'sin')
