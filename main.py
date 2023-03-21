from commands import *
from functions import *
from service import StateManager

if __name__ == '__main__':
    functions = [
        cubic.CubicFunction(),
        sinus.SinusFunction(),
        exponent.ExpFunction(),
        polynom.PolFunction()
    ]
    manager = StateManager(functions)
    commands = {
        "выход": exit.Exit(),
        "функции": list.ListFunctions(manager),
        "помощь": comm_list.ShowCommands(manager),
        "решить": solve.SolveFunction(manager),
        "пересечь": cross.CrossFunctions(manager)
    }
    manager.set_commands(commands)

    while True:
        input_line = input("~ ").split(" ")
        command_line = input_line.pop(0)
        try:
            commands[command_line].execute(input_line)
        except KeyError:
            print("Неизвестная команда")
