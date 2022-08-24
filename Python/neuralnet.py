import random
from matrix import Matrix


def ReLU(m: Matrix):
    return Matrix(
        [[max(0, x) for x in row] for row in m.rows]
    )


class NeuralNetwork:
    def __init__(self, layers: list, biases: list):
        self.layers: list = layers
        self.biases: list = biases

    def get_output(self, input_layer: Matrix) -> Matrix:
        cur_layer: Matrix = input_layer

        for i, layer in enumerate(self.layers):
            cur_layer = ReLU(layer * cur_layer + self.biases[i])

        return cur_layer

    def get_cost(self, input_layer: Matrix, desired_output: Matrix):
        output: Matrix = self.get_output(input_layer)
        cost = sum(
            map(
                (lambda i, j: (i - j) ** 2),
                output.get_transposed()[0],
                desired_output.get_transposed()[0]
            )
        )
        return cost
