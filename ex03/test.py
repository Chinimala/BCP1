from matrix import Matrix
import sys
sys.path.append('../ex02/')
from vector import Vector  # noqa: E402

matrix = Matrix([])
print(matrix)
# matrix = Matrix(1.0)
# matrix = Matrix([1.0])
matrix = Matrix([[1.0]])
print(matrix)
# matrix = Matrix([[1]])
matrix = Matrix([[1.0, 2.0]])
print(matrix)
matrix = Matrix([[1.0], [2.0]])
print(matrix)
matrix = Matrix([[1.0, 2.0], [2.0, 3.5]])
print(matrix)
# matrix = Matrix([[1.0], [2.0, 3.5]])
matrix = Matrix([[1.0]], (1, 1))
# matrix = Matrix([[1.0]], (1, 2))
matrix = Matrix((2, 3))
matrix1 = Matrix([[6.5, 0.0, 1.5], [2.5, 3.0, 1.5]], (2, 3))
print("matrix1 =", matrix1)
matrix2 = Matrix([[1.0, 2.5, 3.5], [2.0, 1.0, 1.0]], (2, 3))
print("matrix2 =", matrix2)
matrix3 = Matrix([[1.0], [2.5], [3.5]])
print("matrix3 =", matrix3)
matrix4 = Matrix([[1.0, 2.0], [1.0, 3.0], [2.0, -1.0]])
print("matrix4 =", matrix4)
# matrix = Matrix((2, 3, 4))
# print(matrix1 + 2)
# print(matrix3 + Vector([1.0, 2.0]))
# print(matrix1 + Vector([1.0, 2.0, 3.0]))
print(matrix3 + Vector([1.0, 2.0, 3.0]))
print(Vector([1.0, 2.0, 3.0]) + matrix3)
# print(matrix1 + matrix3)
print(matrix1 + matrix2)
# print(Vector([1.0, 2.0]) + matrix3)
print(matrix1 - matrix2)
print(matrix3 - Vector([1.0, 2.0, 3.0]))
print(Vector([1.0, 2.0, 3.0]) - matrix3)
print(matrix1 / 2)
# print(matrix1 / matrix2)
# print(matrix1 * matrix2)
print(matrix1 * matrix4)
print(matrix4 * 3)
print(3 * matrix4)
# print(matrix4 * Vector([1.0, 2.0, 3.0]))
print(matrix4 * Vector([1.0, 2.0]))
# print(Vector([1.0, 2.0]) * matrix4)
# idée de tripouille
print(Vector([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0])
      * Matrix([[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]]))
