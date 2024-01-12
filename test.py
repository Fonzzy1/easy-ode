from stepping_matrix import euler
import numpy as np
from IVP import linear

t = 0
y = np.array([0, 10, -9.8])


sol = linear(t, y, euler, np.identity(3))
