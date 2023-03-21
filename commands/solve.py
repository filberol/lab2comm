from commands.command import Command
from solver import half_split, newton


class SolveFunction(Command):
    def __init__(self, manager):
        Command.__init__(self, manager)

    def __str__(self):
        return "Найти ноль функции"

    __def_accuracy = 0.00001

    # args:
    # 1 - function number
    # 2 - borders left:right
    # 3 - accuracy
    def execute(self, args):
        if len(args) < 3:
            print("Использование: -> решить <функция> <граница>:<граница>(половины) <приближение>(касат.) <точность>")
            return
        if int(args[0]) > len(self.service.get_functions()) or int(args[0]) <= 0:
            print("Такой функции нет")
            return

        try:
            methods = [half_split.HalfSplitMethod(), newton.NewtonMethod()]
            borders = list(map(lambda x: float(x), args[1].split(":")))
            start_v = float(args[2])
            function = self.service.get_functions()[int(args[0]) - 1]
            accuracy = float(args[3]) if len(args) > 3 else self.__def_accuracy
        except ValueError:
            print("Неправильные аргументы")
            return

        try:
            answer = methods[0].solve(function, borders, accuracy)
            print(f"{methods[0]}: {answer[0]}, точность {accuracy}, {answer[1]} итераций")
            answer = methods[1].solve(function, start_v, accuracy)
            print(f"{methods[1]}: {answer[0]}, точность {accuracy}, {answer[1]} итераций")
        except ValueError:
            print("Нет пересечений на интервале")
