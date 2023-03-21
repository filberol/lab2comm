from commands.command import Command
from solver import iterations
from functions.sinus import SinusFunction
from functions.exponent import ExpFunction
from functions.polynom import PolFunction


class CrossFunctions(Command):
    def __init__(self, manager):
        Command.__init__(self, manager)

    def __str__(self):
        return "Найти пересечения функций"

    __accuracy = 0.000001

    # аргумемнты:
    # 1, 2 - функции
    # 3 - начальное приближение x_0:y_0
    # 4 - точность
    def execute(self, args):
        if len(args) < 2:
            print("Варианты систем:\t1: 2, 4\t2: 2, 3")
            print("Использование: -> пересечь <вариант> <x_0>:<y_0> <точность)>")
            return

        match int(args[0]):
            case 1:
                func_of_x = SinusFunction()
                func_of_y = PolFunction()
                print("Пример несходящейся системы!")
            case 2:
                func_of_x = SinusFunction()
                func_of_y = ExpFunction()
            case _:
                print("Неправильный вариант системы")
                return
        try:
            cords = list(map(lambda x: float(x), args[1].split(":")))
            accuracy = float(args[2]) if len(args) > 2 else self.__accuracy
        except ValueError:
            print("Неправильные аргументы")
            return

        try:
            method = iterations.IterationMethod()
            answer = method.solve(func_of_x, func_of_y, cords, accuracy)
            print(f"{method}: x={answer[0][0]} y={answer[0][1]}, точность {accuracy}, {answer[1]} итераций")
        except ValueError:
            print("Нет пересечений на интервале или ошибка вычислений")
