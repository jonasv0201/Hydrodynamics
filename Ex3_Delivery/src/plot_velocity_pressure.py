import numpy as np
from numpy import pi as PI
import matplotlib.pyplot as plt
import matplotlib.animation as animation

OMEGA, K, G, H, Z, RHO, t0 = PI/6, 0.03067, 9.81, 50, 4, 1025, 0
xmin, xmax, ymin, ymax = 0, 250, -50, 0


def pressure(x_point, z_point, t):
    return RHO*G*Z * (np.cosh(K*H+K*z_point)/np.cosh(K*H)) * np.cos(K*x_point-OMEGA*t)


def zeta(x, t):
    return Z*np.cos(OMEGA*t-K*x)


def w(x, z, t):
    return (K*G*Z/OMEGA)*(np.sinh(K*H+K*z)/np.cosh(K*H)) * np.sin(K*x-t*OMEGA)


def u(x, z, t):
    return (K*G*Z/OMEGA)*(np.cosh(K*H+K*z)/np.cosh(K*H)) * np.cos(K*x-t*OMEGA)


fig = plt.figure(figsize=[30, 5])
ax = fig.subplots(1, 2)

x_surface = np.arange(0, 250, 1)

ax[0].set(xlabel='[m]', ylabel='[m]', title='Wave velocity', ylim=(ymin, Z+1), xlim=(xmin, xmax))
ax[1].set(xlabel='[m]', ylabel='[m]', title='Wave pressure', ylim=(ymin, Z+1), xlim=(xmin, xmax))

# Define grid
xi = np.linspace(start=xmin, stop=xmax, num=100, endpoint=True)
zi = np.linspace(start=ymax, stop=ymin, num=20, endpoint=True)


# Generate PressureData
pressureData = np.zeros((zi.size, xi.size))
for i in range(0, xi.size):
    for j in range(0, zi.size):
        pressureData[j, i] = pressure(xi[i], zi[j], t0)

ax[1].contourf(xi, zi, pressureData, 15)


xi_vel = np.linspace(start=xmin, stop=xmax, num=18, endpoint=True)
zi_vel = np.linspace(start=ymax, stop=ymin, num=18, endpoint=True)
u_vel = np.zeros((zi_vel.size, xi_vel.size))
w_vel = np.zeros((zi_vel.size, xi_vel.size))
for i in range(0, xi_vel.size):
    for j in range(0, zi_vel.size):
        u_vel[j, i] = u(xi_vel[i], zi_vel[j], t0)
        w_vel[j, i] = w(xi_vel[i], zi_vel[j], t0)

ax[0].quiver(xi_vel, zi_vel, u_vel, w_vel, pivot='middle')

line1, = ax[1].plot(x_surface, zeta(x_surface, t0))
line0, = ax[0].plot(x_surface, zeta(x_surface, t0))


def init():
    line1.set_ydata([np.nan]*len(x_surface))
    line0.set_ydata([np.nan] * len(x_surface))

    return line1, line0,


def animate(t):
    line1.set_ydata(zeta(x_surface, t))
    line0.set_ydata(zeta(x_surface, t))

    return line1, line0


ani = animation.FuncAnimation(fig, animate, init_func=init, interval=150, blit=True, save_count=50)

plt.show()
