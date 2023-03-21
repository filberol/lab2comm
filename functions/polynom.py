import math

from functions.function import Function


class PolFunction(Function):

    def value(self, x):
        return x**3 - 2 * x**2 + 0.5

    def derivative(self, x):
        return 3 * x**2 - 4 * x

    def __str__(self):
        return f"x^3 - 2x^2 + 0.5"
