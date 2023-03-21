from solver.interfaces import FunctionSolver
from solver.time_counter import add_clock
from copy import deepcopy
from functions.function import Function


class NewtonMethod(FunctionSolver):

    __max_iterations = 1000

    @add_clock
    def solve(self, function: Function, start, accuracy):
        dyn_cord = deepcopy(start)
        diff_x = dyn_cord + 100
        iterations = 0

        while abs(diff_x) > 0 and iterations < self.__max_iterations:
            iterations += 1
            new_x = dyn_cord - function.value(dyn_cord) / function.derivative(dyn_cord)
            diff_x = dyn_cord - new_x
            dyn_cord = new_x
        return dyn_cord, iterations

    def __str__(self):
        return "Метод касательных"
