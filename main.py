import numpy as np
from algo import Interpolation
from vis import vis_func


def runge(x):
    return 1 / (1 + 25*x**2)


if __name__ == '__main__':
    start = -1
    end = 1
    itp = Interpolation(runge)
    # f_newton = itp.newton(start, end)
    vis_func(runge, start, end, 'runge')
    # vis_func(f_newton, start, end, 'runge_newton')
    # lang_xrange = [np.cos((2*i+1)/42*np.pi) for i in range(21)]
    # f_lang = itp.lagrange(lang_xrange)
    # vis_func(f_lang, start, end, 'langrange')
    f_piece_linear = itp.piecewise_linear(start, end)
    vis_func(f_piece_linear, start, end, 'piecewise_linear')
