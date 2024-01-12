from stepping_matrix import euler
import numpy as np
from IVP import linear


# Simple euler integration
t = 0
y = np.array([0, 10, -9.8])
sol = linear(t, y, euler, np.identity(3))


# Harmonic motion , y'' = -a*y
t = 0
y = np.array([0, 1, 0])
a = 0.4
T_matix = np.array([[1, 0, 0], [0, 1, 0], [-a, 0, 0]])
sol = linear(t, y, euler, T_matix, steps=100)
