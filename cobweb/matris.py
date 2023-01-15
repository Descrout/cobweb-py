import random

class Matrix():
    def __init__(self, rows, cols, fn = None) -> None:
        self.rows = rows
        self.cols = cols

        if fn == None:
            fn = lambda i, j: random.random() / (cols ** 0.5)

        self.data = [[fn(i, j) for j in range(cols)] for i in range(rows)]

    def __add__(self, n):
        result = self.copy()
        if isinstance(n, Matrix):
            result.data = [[self.data[i][j] + n.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        else:
            result.data = [[self.data[i][j] + n for j in range(self.cols)] for i in range(self.rows)]
        return result

    def add(self, n):
        if isinstance(n, Matrix):
            self.data = [[self.data[i][j] + n.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        else:
            self.data = [[self.data[i][j] + n for j in range(self.cols)] for i in range(self.rows)]
    
    def __sub__(self, n):
        result = self.copy()
        if isinstance(n, Matrix):
            result.data = [[self.data[i][j] - n.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        else:
            result.data = [[self.data[i][j] - n for j in range(self.cols)] for i in range(self.rows)]
        return result

    def sub(self, n):
        if isinstance(n, Matrix):
            self.data = [[self.data[i][j] - n.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        else:
            self.data = [[self.data[i][j] - n for j in range(self.cols)] for i in range(self.rows)]

    def __mul__(self, n):
        result = self.copy()
        if isinstance(n, Matrix):
            result.data = [[self.data[i][j] * n.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        else:
            result.data = [[self.data[i][j] * n for j in range(self.cols)] for i in range(self.rows)]
        return result

    def mul(self, n):
        if isinstance(n, Matrix):
            self.data = [[self.data[i][j] * n.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        else:
            self.data = [[self.data[i][j] * n for j in range(self.cols)] for i in range(self.rows)]
    
    def __truediv__(self, n):
        result = self.copy()
        if isinstance(n, Matrix):
            result.data = [[self.data[i][j] / n.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        else:
            result.data = [[self.data[i][j] / n for j in range(self.cols)] for i in range(self.rows)]
        return result

    def div(self, n):
        if isinstance(n, Matrix):
            self.data = [[self.data[i][j] / n.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        else:
            self.data = [[self.data[i][j] / n for j in range(self.cols)] for i in range(self.rows)]

    def __pow__(self, n):
        result = self.copy()
        if isinstance(n, Matrix):
            result.data = [[self.data[i][j] ** n.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        else:
            result.data = [[self.data[i][j] ** n for j in range(self.cols)] for i in range(self.rows)]
        return result
    
    def pow(self, n):
        if isinstance(n, Matrix):
            self.data = [[self.data[i][j] ** n.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        else:
            self.data = [[self.data[i][j] ** n for j in range(self.cols)] for i in range(self.rows)]

    def matmul(self, other):
        if self.cols != other.rows:
            raise Exception("left matrix columns must match right matrix rows")
        n = self.cols
        result = Matrix(self.rows, other.cols)

        for i in range(self.rows):
            for j in range(other.cols):
                sum = 0
                for k in range(n):
                    sum += self.data[i][k] * other.data[k][j]
                result.data[i][j] = sum
        return result
    
    def copy(self):
        result = Matrix(self.rows, self.cols)
        result.data = [[self.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return result

    def transpose(self):
        result = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[j][i] = self.data[i][j]
        return result

    def map(self, fn):
        self.data = [[fn(self.data[i][j]) for j in range(self.cols)] for i in range(self.rows)]
    
    def shape(self):
        return (self.rows, self.cols)

    def flatten(self):
        result = []
        for i in range(self.rows):
            for j in range(self.cols):
                result.append(self.data[i][j])
        return result

    def print(self):
        for i in range(self.rows):
            print(self.data[i])
        print("")

    @staticmethod
    def From1DList(arr):
        ln = len(arr)
        result = Matrix(ln, 1)
        for i in range(ln):
            result.data[i][0] = arr[i]
        return result

    @staticmethod
    def From2DList(arr):
        rows = len(arr)
        cols = len(arr[0])
        result = Matrix(rows, cols)
        result.data = [[arr[i][j] for j in range(result.cols)] for i in range(result.rows)]
        return result

    @staticmethod
    def Map(m, fn):
        matrix = Matrix(m.rows, m.cols)
        matrix.data = [[fn(m.data[i][j]) for j in range(m.cols)] for i in range(m.rows)]
        return matrix