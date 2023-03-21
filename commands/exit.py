from commands.command import Command


class Exit(Command):
    def __str__(self):
        return "Выйти из программы"

    def execute(self, args):
        exit(0)
