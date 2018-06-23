import numpy as np
from algo import Interpolation
from vis import vis_func


def runge(x):
    return 1 / (1 + 25*x**2)


def f2(x):
    if -1 <= x < 0:
        return np.sin(np.pi*x)
    elif 0 <= x < 0.5:
        return np.cos(np.pi*x)
    elif 0.5 <= x <= 1:
        return 0


app_f = f2
prefix = 'f2'


if __name__ == '__main__':
    start = -1
    end = 1
    funcs = [runge, f2]
    f_names = ['runge', 'f2']
    methods = ['newton', 'langrange', 'piecewise_linear', 'spline']
    for i in range(len(funcs)):
        cur_f = funcs[i]
        cur_fname = f_names[i]
        itp = Interpolation(cur_f)
        vis_func(cur_f, start, end, cur_fname, cont=False)
        for j in range(len(methods)):
            cur_method = methods[j]
            print(cur_fname, cur_method)
            f_itp = None
            if cur_method == 'newton':
                f_itp = itp.newton(start, end)
            elif cur_method == 'langrange':
                lang_xrange = [np.cos((2*i+1)/42*np.pi) for i in range(21)]
                f_itp = itp.lagrange(lang_xrange)
            elif cur_method == 'piecewise_linear':
                f_itp = itp.piecewise_linear(start, end)
            elif cur_method == 'spline':
                f_itp =itp.spline(start, end)
            vis_func(f_itp, start, end, '{}_{}'.format(cur_fname, cur_method))
