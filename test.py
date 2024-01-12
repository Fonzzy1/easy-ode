from stepping_matrix import expanded_euler
import numpy as np
from IVP import linear

# Simple euler integration
y = np.array([1, 0, 0, 10, -9.8])
sol = linear(y, expanded_euler, np.identity(5))


# Harmonic motion , y'' = -a*y
y = np.array([1, 0, 0, 1, 0])
a = 0.4
T_matix = np.array(
    [
        [1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, -a, 0, 0],
    ]
)
sol = linear(y, expanded_euler, T_matix, steps=100)
