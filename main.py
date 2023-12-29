def IVP(x, y, step_matrix_generator, steps=10, h=0.1):
    dims = len(y)
    step_matrix = step_matrix_generator(dims, h)
    output_dict = {x: y}

    x_n = x
    y_n = y.copy()
    i = 0
    while i < steps:
        y_n = step_matrix @ y_n
        x_n += h
        output_dict[x_n] = y_n
        i += 1

    return output_dict
