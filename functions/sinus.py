from functions.function import Function
import math


class SinusFunction(Function):

    def value(self, x):
        return math.sin(x / 1.1)

    def derivative(self, x):
        return 10 * math.cos(10 * x / 11) / 11

    def of_x(self, x, y):
        return math.asin(y) * 1.1

    def __str__(self):
        return "sin(x / 1.1)"
