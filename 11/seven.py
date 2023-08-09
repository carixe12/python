class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0] * columns for _ in range(rows)]

    def __str__(self):
        matrix_str = ""
        for row in self.data:
            matrix_str += " ".join(str(element) for element in row)
            matrix_str += "\n"
        return matrix_str

    def add(self, other_matrix):
        if self.rows != other_matrix.rows or self.columns != other_matrix.columns:
            raise ValueError("Matrix dimensions must be the same for addition.")

        result = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                result.data[i][j] = self.data[i][j] + other_matrix.data[i][j]

        return result

    def subtract(self, other_matrix):
        if self.rows != other_matrix.rows or self.columns != other_matrix.columns:
            raise ValueError("Matrix dimensions must be the same for subtraction.")

        result = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                result.data[i][j] = self.data[i][j] - other_matrix.data[i][j]

        return result

    def multiply(self, other_matrix):
        if self.columns != other_matrix.rows:
            raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix.")

        result = Matrix(self.rows, other_matrix.columns)
        for i in range(self.rows):
            for j in range(other_matrix.columns):
                for k in range(self.columns):
                    result.data[i][j] += self.data[i][k] * other_matrix.data[k][j]

        return result

    def transpose(self):
        result = Matrix(self.columns, self.rows)
        for i in range(self.rows):
            for j in range(self.columns):
                result.data[j][i] = self.data[i][j]

        return result
    
m1 = Matrix(2, 3)
m1.data = [[1, 2, 3], [4, 5, 6]]

m2 = Matrix(2, 3)
m2.data = [[7, 8, 9], [10, 11, 12]]

print("Matrix 1:")
print(m1)

print("Matrix 2:")
print(m2)

print("Matrix addition:")
print(m1.add(m2))

print("Matrix subtraction:")
print(m1.subtract(m2))

m3 = Matrix(3, 2)
m3.data = [[1, 2], [3, 4], [5, 6]]

print("Matrix multiplication:")
print(m1.multiply(m3))

print("Transpose of matrix 1:")
print(m1.transpose())   