from stepping_matrix import euler
import numpy as np
from main import IVP

t = 0
y = np.array([0, 10, -9.8])
out_dict = IVP(t, y, euler)
