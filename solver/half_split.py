from solver.interfaces import FunctionSolver
from solver.time_counter import add_clock
from functions.function import Function
from copy import deepcopy


class HalfSplitMethod(FunctionSolver):

    __max_iterations = 1000

    @add_clock
    def solve(self, function: Function, borders, accuracy):
        if function.value(borders[0]) * function.value(borders[1]) >= 0:
            raise ValueError(borders)

        edges = deepcopy(borders)
        epsilon = edges[1] - edges[0]
        is_positive = function.value(borders[1]) > 0
        iterations = 0

        while abs(epsilon) > accuracy and iterations < self.__max_iterations:
            iterations += 1
            epsilon = edges[1] - edges[0]
            new_x = sum(edges) / 2.0
            new_y = function.value(new_x)
            if new_y == 0:
                return new_x, iterations
            if is_positive:
                if new_y > 0:
                    edges[1] = new_x
                else:
                    edges[0] = new_x
            else:
                if new_y > 0:
                    edges[0] = new_x
                else:
                    edges[1] = new_x
        return sum(edges) / 2.0, iterations

    def __str__(self):
        return "Метод половинного деления"
