import numpy as np
from numpy import pi as PI
import matplotlib.pyplot as plt


dt = np.linspace(0, 18, 40, endpoint=True)
phase = 2.22
func1 = 1.56e3 * np.cos(0.419*dt)       + 0.114e3 * abs(np.sin(0.419*dt))       * np.sin(0.419*dt)        # kN
func2 = 1.56e3 * np.cos(0.419*dt-phase) + 0.114e3 * abs(np.sin(0.419*dt-phase)) * np.sin(0.419*dt-phase)  # kN

fig, ax = plt.subplots(sharex='all', figsize=(10, 20))
ax.set(title="Morrison", ylabel="Force [kn]", xlabel="Time [s]")

ax.plot(dt, func1, label="First cylinder", linestyle="--")
ax.plot(dt, func2, label="Second cylinder", linestyle="--")
ax.plot(dt, (func1+func2), label="Total force", linewidth=6)

plt.legend()
plt.show()

