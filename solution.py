import numpy as np


class Solution:
    def __init__(self, input_list: list):
        solution_list = sorted(input_list, key=lambda x: x[1])

        dims = len(solution_list[0]) - 2
        self.x = np.array([x[1] for x in input_list])

        value_lists = [[] for _ in range(dims)]

        for v in input_list:
            for i in range(dims):
                value_lists[i].append(v[i + 2])

        for i in range(dims):
            self.__dict__[f"y_{i}"] = np.array(value_lists[i])

    def interpolate(self, x, y_n):
        """
        allows you to get any value from the solution by interpolating the points

        """
        y_values = self.__dict__[f"y_{y_n}"]

        x_max_index = np.where(self.x >= x)[0][0]
        x_min_index = np.where(self.x <= x)[0][-1]

        x_at_x_max = self.x[x_max_index]
        x_at_x_min = self.x[x_min_index]

        y_at_x_max = y_values[x_max_index]
        y_at_x_min = y_values[x_min_index]

        slope = (y_at_x_max - y_at_x_min) / (x_at_x_max - x_at_x_min)

        value = y_at_x_min + slope * (x - x_at_x_min)
        return value
