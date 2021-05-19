from scipy import constants as sci
import scipy.optimize as min
import numpy as np

omega = np.pi / 6
g = 9.81
h = 50


def f(k):
    return k * g * np.tanh(k * h) - omega ** 2


ans = min.newton(f, 0.1, tol=1e-20, maxiter=100)
print(ans)
# k = 0.030674709805243193

