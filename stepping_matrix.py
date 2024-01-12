import numpy as np
import math


def euler(dims, h):
    # Start with an identity matrix
    step_matrix = np.identity(dims)
    # Add in all the h values
    for i in range(dims - 1):
        step_matrix[i, i + 1] = h
    expanded_matrix = add_x_and_1(step_matrix, h)
    return expanded_matrix


def expanded_euler(dims, h):
    step_matrix = np.zeros((dims, dims))
    for i in range(dims):
        for j in range(i, dims):
            # Is 1, and h at j-i =0, 1 respectively
            step_matrix[i, j] = h ** (j - i) / math.factorial(j - i)
    expanded_matrix = add_x_and_1(step_matrix, h)
    return expanded_matrix


def add_x_and_1(original_matrix, h):
    new_size = len(original_matrix) + 2
    new_matrix = np.zeros((new_size, new_size), dtype=original_matrix.dtype)

    # Set the 2x2 top left matrix
    new_matrix[0:2, 0:2] = [[1, 0], [h, 1]]

    # Copy the original matrix to the bottom right of the new matrix.
    new_matrix[2:, 2:] = original_matrix
    return new_matrix
