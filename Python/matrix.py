from typing import Union


def count_inverses(seq) -> int:
    count = 0
    for i, v in enumerate(seq):
        for j in seq[i:]:
            if v > j:
                count += 1
    return count


def rearrange(n: int, c: int, tup: tuple = tuple()) -> tuple:
    if c > 0:
        for i in range(n):
            if i in tup:
                continue
            yield from rearrange(n, c - 1, (*tup, i))
    else:
        yield tup


class Matrix:
    def __init__(self, rows: list):
        if not isinstance(rows, list):
            raise TypeError
        elif any((not isinstance(cols, list) for cols in rows)):
            raise TypeError
        self.rows = rows

    def __getitem__(self, key: Union[int, tuple]) -> Union[list, float, int]:
        if isinstance(key, int):
            return self.rows[key]
        elif isinstance(key, tuple):
            i, j = key
            return self.rows[i][j]
        else:
            raise TypeError

    def __setitem__(self, key, value):
        if not isinstance(key, tuple):
            raise TypeError
        i, j = key
        self.rows[i][j] = value

    def __iter__(self):
        return self.rows.__iter__()

    def __len__(self):
        return self.rows.__len__()

    def __str__(self):
        return "\n".join([f'[{" ".join(map(str, row))}]' for row in self])

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Matrix([[col * other for col in row] for row in self])
        elif isinstance(other, Matrix):
            if self.width != other.height:
                raise ValueError

            matrix: Matrix = Matrix(
                [[0 for _ in range(other.width)] for _ in range(other.height)]
            )

            for row in range(matrix.height):
                for col in range(matrix.width):
                    matrix[row, col] = sum(map((lambda x, y: x * y),
                                               self[row], other.get_transposed()[col]))
            return matrix
        else:
            raise TypeError

    def __pow__(self, power):
        matrix = self
        for i in range(power - 1):
            matrix = matrix * self
        return matrix

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError
        elif self.size != other.size:
            raise ValueError

        matrix: Matrix = Matrix(
            [[0 for _ in range(other.width)] for _ in range(other.height)]
        )

        for row in range(matrix.height):
            for col in range(matrix.width):
                matrix[row, col] = self[row, col] + other[row, col]

        return matrix

    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError
        elif self.size != other.size:
            raise ValueError

        matrix: Matrix = Matrix(
            [[0 for _ in range(other.width)] for _ in range(other.height)]
        )

        for row in range(matrix.height):
            for col in range(matrix.width):
                matrix[row, col] = self[row, col] - other[row, col]

        return matrix

    def get_transposed(self):
        return Matrix(
            [[row[i] for row in self] for i in range(self.width)]
        )

    @property
    def height(self):
        return len(self)

    @property
    def width(self):
        return len(self.rows[0])

    @property
    def size(self):
        return self.height, self.width

    @property
    def is_square(self):
        return self.height == self.width

    @property
    def determinant(self):
        if not self.is_square:
            raise ValueError

        det: float = 0.0

        for p in rearrange(self.height, self.height):
            prod: int = 1
            for i in map((lambda *a: a), p, range(self.height)):
                prod *= self[i]
            det += ((-1) ** count_inverses(p)) * prod

        return det
