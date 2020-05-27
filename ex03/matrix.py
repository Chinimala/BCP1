import sys
import copy
from numbers import Number
sys.path.append('../ex02/')
from vector import Vector  # noqa: E402


class Matrix:
    def __init__(self, arg1, arg2=None):
        if isinstance(arg1, list):
            valid = True
            if not (all(isinstance(lst, list) for lst in arg1)):
                valid = False
            if valid and len(arg1) > 0:
                row_length = len(arg1[0])
                for lst in arg1:
                    if not (len(lst) == row_length
                            and all(isinstance(n, float) for n in lst)):
                        valid = False
            elif len(arg1) == 0:
                row_length = 0
            if not valid:
                raise ValueError("list must contains lists of floats"
                                 " of same size")

            self.data = arg1
            self.shape = (len(arg1), row_length)

            if arg2 is not None:
                if not (isinstance(arg2, tuple)
                        and len(arg2) == 2
                        and all(isinstance(n, int) for n in arg2)):
                    raise ValueError("second argument must a tuple of 2 int")
                if arg2 != self.shape:
                    raise ValueError("matrix shape doesn't match tuple")

        elif isinstance(arg1, tuple):
            if not (len(arg1) == 2 and all(isinstance(n, int) for n in arg1)):
                raise ValueError("The tuple must contain only 2 int")
            self.data = [[float(0) for j in range(arg1[1])]
                         for i in range(arg1[0])]
            self.shape = arg1
        else:
            raise TypeError("Matrix can only take a list or a tuple")

    def __str__(self):
        # return "(Matrix {})".format(self.data)
        res = '\n('
        res += '\n '.join(' '.join(str(x) for x in line) for line in self.data)
        res += ')'
        return res

    def __repr__(self):
        # return "(Matrix {})".format(self.data)
        return str(self)

    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.shape != other.shape:
                raise ValueError("Matrices must have same shape to add")
            res = [[x + y for x, y in zip(self_line, other_line)]
                   for self_line, other_line in zip(self.data, other.data)]
            return Matrix(res)
        elif isinstance(other, Vector):
            if self.shape[1] != 1:
                raise ValueError("matrix must have one column to add vector")
            elif other.size != self.shape[0]:
                raise ValueError("vector must have n lines to add "
                                 "to a n-line matrix")
            else:
                return self + Matrix([[x] for x in other.values])
        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, Matrix):
            if self.shape != other.shape:
                raise ValueError("Matrices must have same shape to sub")
            data = [[x - y for x, y in zip(self_line, other_line)]
                    for self_line, other_line in zip(self.data, other.data)]
            return Matrix(data)
        elif isinstance(other, Vector):
            if self.shape[1] != 1:
                raise ValueError("matrix must have one column to sub vector")
            elif other.size != self.shape[0]:
                raise ValueError("vector must have n lines to sub "
                                 "a n-line matrix")
            else:
                return self + Matrix([[x] for x in other.values])
        else:
            return NotImplemented

    def __rsub__(self, other):
        return self - other

    def __truediv__(self, other):
        if isinstance(other, Number):
            data = [[float(x / other) for x in line] for line in self.data]
            return Matrix(data)
        else:
            return NotImplemented

    def __rtrudiv__(self, other):
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.shape[1] != other.shape[0]:
                raise ValueError("Incompatible shapes to mult")
            data = []
            for self_line in self.data:
                data_line = []
                for column in range(other.shape[1]):
                    nb = 0
                    for i in range(self.shape[1]):
                        nb += self_line[i] * other.data[i][column]
                    data_line.append(nb)
                data.append(data_line)
            return Matrix(data)
        elif isinstance(other, Number):
            data = [[float(x * other) for x in line] for line in self.data]
            return Matrix(data)
        elif isinstance(other, Vector):
            if self.shape[1] != other.size:
                raise ValueError("matrix shape not matching with vector")
            values = []
            for self_line in self.data:
                nb = 0
                for i in range(other.size):
                    nb += self_line[i] * other.values[i]
                values.append(nb)
            return Vector(values)
        else:
            return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, Matrix):
            return self * other
        elif isinstance(other, Vector):
            if self.shape[0] != 1:
                raise ValueError("matrix shape not matching with vector")
            data = []
            for n_other in other.values:
                data_line = []
                for n_self in self.data[0]:
                    data_line.append(n_other * n_self)
                data.append(data_line)
            return Matrix(data)
        elif isinstance(other, Number):
            return self * other
        else:
            return NotImplemented
