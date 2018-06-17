from algo import Interpolation
from vis import vis_func


def runge(x):
    return 1 / (1 + 25*x**2)


if __name__ == '__main__':
    start = -1
    end = 1
    itp = Interpolation(runge)
    f_newton = itp.newton(start, end)
    vis_func(runge, start, end, 'runge')
    vis_func(f_newton, start, end, 'runge_newton')
