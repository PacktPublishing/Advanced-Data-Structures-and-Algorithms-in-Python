class Matrix:

    def __init__(self, rows, cols):
        self.mat = []
        self.rows = rows
        self.cols = cols
        for i in range(rows):
            self.mat.append([0] * cols)

    def __mul__(self, other):
        assert self.cols == other.rows
        result = Matrix(self.rows, other.cols)
        for k in range(other.rows):
            for i in range(self.rows):
                for j in range(other.cols):
                    result.mat[i][j] += self.mat[i][k] * other.mat[k][j]
        return result

    def __mod__(self, mod):
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in  range(self.cols):
                result.mat[i][j] = self.mat[i][j] % mod
        return result

    def __pow__(self, power, modulo=666013):
        assert self.rows == self.cols
        if power == 0:
            ret = Matrix(self.rows, self.cols)
            for i in range(self.cols):
                ret.mat[i][i] = 1
            return ret

        half_power = self ** (power // 2)
        if power % 2 == 0:
            return (half_power * half_power) % modulo
        return (half_power * half_power * self) % modulo

    def __str__(self):
        result = ''
        for i in range(self.rows):
            for j in range(self.cols):
                result += str(self.mat[i][j]) + '\t'
            result += '\n'
        return result


mat = Matrix(2, 2)
mat.mat = [[1, 1], [1, 0]]
print(mat)
print(mat * mat)
print(mat * mat * mat)
print(mat * mat * mat * mat)
print(mat ** 1000000000000000000) # 10 ** 18, instant execution time
