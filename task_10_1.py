class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, _list_)) for _list_ in self.matrix])

    def __add__(self, other):
        return [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
                for i in range(len(self.matrix))]


a = Matrix([[3, 5, 5], [2, 9, -9], [1, 4, 99]])
print(a)
b = Matrix([[0, 5, 2], [2, 1, 9], [1, 7, -93]])
print(b)
print(a + b)
