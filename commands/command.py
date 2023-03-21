class Command:
    def __init__(self, service=None):
        self.service = service

    def __str__(self):
        return "Интерфейс команды"

    def execute(self, args):
        print("Команда еще не реализована")
        print(self.service)
