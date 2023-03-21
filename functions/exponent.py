from functions.function import Function
import math


class ExpFunction(Function):

    def value(self, x):
        if x == 0:
            return -0.2
        return math.exp(-1 * abs(1 / (2 * x))) - 0.2

    def derivative(self, x):
        return 1 / (2 * math.exp(1 / (2 * abs(x))) * x * abs(x))

    def __str__(self):
        return "e^(-|1/2x|)"
