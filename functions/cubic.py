from functions.function import Function


class CubicFunction(Function):

    def value(self, x):
        return x**3 / 2 - 0.5

    def derivative(self, x):
        return 3 / 2 * x**2

    def __str__(self):
        return "x^3 / 2 - 0.5"
