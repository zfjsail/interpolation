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