import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Simulate recursive feedback and growth dynamics
def golden_spiral_3d(n, growth_factor, decay_factor):
    theta = np.linspace(0, 4 * np.pi, n)  # Angular progression
    z = np.linspace(0, 10, n)  # Z-axis progression (e.g., time or iteration)
    r = [1]  # Initial radius
    for i in range(1, n):
        new_radius = r[-1] * growth_factor / (1 + decay_factor * i)
        r.append(new_radius)
    r = np.array(r)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y, z

# Parameters
n = 500  # Number of cycles
growth_factor = 1.618  # Approximate golden ratio
decay_factor = 0.05  # Damping factor

# Generate spiral data
x, y, z = golden_spiral_3d(n, growth_factor, decay_factor)

# Plot the 3D spiral
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, label="3D Golden Spiral")
ax.set_title("3D Golden Spiral Effect in Recursive Dynamics")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.legend()
plt.show()