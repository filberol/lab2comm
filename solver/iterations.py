from solver.interfaces import SystemSolver
from solver.time_counter import add_clock
from functions.function import Function
from copy import deepcopy


class IterationMethod(SystemSolver):

    __max_iterations = 10000

    @add_clock
    def solve(self, func_of_x: Function, func_of_y: Function, coords, accuracy):
        dyn_cords = deepcopy(coords)
        diff_x = coords[0] + 100
        diff_y = coords[1] + 100
        iterations = 0

        while abs(diff_x) > accuracy and abs(diff_y) > accuracy and iterations < self.__max_iterations:
            iterations += 1
            # print(f"{dyn_cords[0]}   {dyn_cords[1]}")
            new_x = func_of_x.of_x(dyn_cords[0], dyn_cords[1])
            new_y = func_of_y.value(dyn_cords[0])
            diff_x = dyn_cords[0] - new_x
            diff_y = dyn_cords[1] - new_y
            dyn_cords[0] = new_x
            dyn_cords[1] = new_y
        return dyn_cords, iterations

    def __str__(self):
        return "Метод простых итераций"
