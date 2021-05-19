import numpy as np
import matplotlib.pyplot as plt


def force(theta):
    return 505430*np.sin(theta) + 28155 * abs(np.cos(theta))*np.cos(theta)


theta_i = np.linspace(0, 2*np.pi, 1001)

fk = force(theta_i)


print('Max force is:  ' + str(max(fk)) + ' Newton')

plt.plot(theta_i, fk)
plt.show()

