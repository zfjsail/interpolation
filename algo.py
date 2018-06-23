import numpy as np
from scipy.linalg import solve_banded


def binary_search_interval(x, start, end, intervals=20):  # assume start <= x <= end
    range_end = intervals + 1
    h = (end - start) / intervals
    inter_points = [start + h * i for i in range(range_end)]
    li = 0
    ri = intervals
    while ri - li > 1:
        mid = (ri + li) // 2
        mid_value = inter_points[mid]
        if mid_value == x:
            return mid - 1  # return left
        elif mid_value < x:
            li = mid
        else:
            ri = mid
    return li


class Interpolation:
    def __init__(self, f):
        self.func = f

    def newton(self, start, end, intervals=20):
        range_end = intervals + 1
        a = np.zeros((range_end, range_end))
        h = (end - start) / intervals
        inter_points = [start + h * i for i in range(range_end)]
        for i in range(range_end):
            a[0, i] = self.func(inter_points[i])
        for i in range(1, range_end):
            for j in range(range_end-i):
                a[i, j] = (a[i-1, j+1] - a[i-1, j]) / (inter_points[i+j]-inter_points[j])

        def f_newton(x):
            y = 0
            for i in range(range_end):
                w = 1.
                for j in range(i):
                    w *= (x - inter_points[j])
                y += w * a[i, 0]
            return y
        return f_newton

    def lagrange(self, x_range):
        def f_lagrange(x):
            x_subs = [x - x_i for x_i in x_range]
            y = 0
            for i, x_i in enumerate(x_range):
                f_i = self.func(x_i)
                w = 1.
                for j, x_j in enumerate(x_range):
                    if j != i:
                        w *= (x_subs[j] / (x_i - x_j))
                y += (f_i * w)
            return y
        return f_lagrange

    def piecewise_linear(self, start, end, intervals=20):
        range_end = intervals + 1
        h = (end - start) / intervals
        inter_points = [start + h * i for i in range(range_end)]

        def f_piecewise(x):
            li = binary_search_interval(x, start, end, intervals)
            left = inter_points[li]
            right = inter_points[li+1]
            if x == left:
                y = self.func(left)
            elif x == right:
                y = self.func(right)
            else:
                y = (x - right) / (left - right) * self.func(left) + (x - left) / (right - left) * self.func(right)
            return y
        return f_piecewise

    def spline(self, start, end, intervals=20):
        range_end = intervals + 1
        h = (end - start) / intervals
        inter_points = [start + h * i for i in range(range_end)]

        m = np.zeros(intervals+1)
        a = np.zeros((3, intervals-1))
        a[0, 1:-1] = 0.5
        a[1, :] = 2
        a[2, 1:-1] = 0.5
        d1 = np.zeros(intervals)
        for i in range(len(d1)):
            d1[i] = (self.func(inter_points[i+1]) - self.func(inter_points[i]))/h
        d2 = np.zeros(intervals-1)
        for i in range(len(d2)):
            d2[i] = 6*(d1[i+1]-d1[i])/(2*h)  # note 6*
        m[1:-1] = solve_banded((1, 1), a, d2)

        def f_spline(x):
            li = binary_search_interval(x, start, end, intervals)
            x_left = inter_points[li]
            x_right = inter_points[li+1]
            s = m[li]*((x_right-x)**3)/(6*h) + m[li+1]*((x-x_left)**3)/(6*h) + \
                (self.func(x_left)-(m[li]*h*h)/6)*(x_right-x)/h + (self.func(x_right) - m[li+1]*h*h/6)*(x-x_left)/h
            return s
        return f_spline
