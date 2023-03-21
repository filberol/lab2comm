from commands.command import Command


class ShowCommands(Command):
    def __str__(self):
        return "Вывести команды с описанием"

    def execute(self, args):
        print("Доступные команды:")
        commands = self.service.get_commands()
        for command in commands.keys():
            print(f'"{command}" - {commands[command]}')
