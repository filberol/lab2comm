from commands.command import Command


class ListFunctions(Command):
    def __init__(self, manager):
        Command.__init__(self, manager)

    def execute(self, args):
        print("Доступные функции:")
        for index, func in enumerate(self.service.get_functions()):
            print(f"{index + 1}. f(x) = {func}")

    def __str__(self):
        return "Вывести доступные функции"
