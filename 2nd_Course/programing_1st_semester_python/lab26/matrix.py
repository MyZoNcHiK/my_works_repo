class MatrixOperation:
    def __init__(self, matrix):
        self.matrix = matrix

    def __getitem__(self, index):
        row, column = index
        return self.matrix[row][column]

    def __setitem__(self, index, value):
        row, column = index
        self.matrix[row][column] = value

    def __bool__(self):
        for row in self.matrix:
            for value in row:
                if isinstance(value, bool):
                    return True
        return False

    def show(self):
        for row in self.matrix:
            print(row)


matrix = MatrixOperation([
    [1, 2, 3],
    [4, True, 6],
    [7, 8, 9]
])

matrix.show()

print(matrix[1, 1])

matrix[0, 0] = 100
matrix.show()

print(bool(matrix))

print("__bases__:", MatrixOperation.__bases__)
print("__dict__:", MatrixOperation.__dict__)
print("__doc__:", MatrixOperation.__doc__)
print("__module__:", MatrixOperation.__module__)
print("__mro__:", MatrixOperation.__mro__)
print("__name__:", MatrixOperation.__name__)
print("__qualname__:", MatrixOperation.__qualname__)

print("__dict__:", matrix.__dict__)
print("__class__:", matrix.__class__)

