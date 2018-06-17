import numpy as np


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
            y = 0
            flag = False
            for i, x_i in enumerate(inter_points[:-1]):
                left = x_i
                right = inter_points[i+1]
                if x == left:
                    y = self.func(left)
                    flag = True
                elif x == right:
                    y = self.func(right)
                    flag = True
                elif left < x < right:
                    y = (x - right) / (left - right) * self.func(left) + (x - left) / (right - left) * self.func(right)
                if flag:
                    break
            return y
        return f_piecewise
