import numpy as np
import math


def euler(dims, h):
    # Start with an identity matrix
    step_matrix = np.identity(dims)
    # Add in all the h values
    for i in range(dims - 1):
        step_matrix[i, i + 1] = h
    return step_matrix


def expanded_euler(dims, h):
    step_matrix = np.zeros((dims, dims))
    for i in range(dims):
        for j in range(i, dims):
            # Is 1, and h at j-i =0, 1 respectively
            step_matrix[i, j] = h ** (j - i) / math.factorial(j - i)
    return step_matrix
