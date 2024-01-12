from solution import Solution


def linear(y, step_matrix_generator, transformation_matrix, steps=10, h=0.1):
    dims = len(y) - 2
    step_matrix = transformation_matrix @ step_matrix_generator(dims, h)
    output_list = []

    y_n = y.copy()
    i = 0
    while i < steps:
        y_n = step_matrix @ y_n
        output_list.append(y_n)
        i += 1

    return Solution(output_list)
