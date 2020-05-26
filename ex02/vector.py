import numbers


class Vector:
    def __init__(self, arg):
        if isinstance(arg, int):
            self.size = arg
            self.values = [x * 1.0 for x in range(0, arg)]
        elif isinstance(arg, list):
            self.size = len(arg)
            self.values = arg
        elif isinstance(arg, range):
            self.size = len(arg)
            self.values = [x * 1.0 for x in arg]
        elif isinstance(arg, tuple) and len(arg) == 2:
            self.size = arg[1] - arg[0]
            self.values = [x * 1.0 for x in range(*arg)]
        else:
            raise TypeError("argument must be int, range, tuple(2) or list")

    def __str__(self):
        return "(Vector {})".format(self.values)

    def __repr__(self):
        return "(Vector {})".format(self.values)

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Can only add vector to vector")
        elif other.size != self.size:
            raise ValueError("Can only add same size vectors")
        values = [x + y for x, y in zip(self.values, other.values)]
        return Vector(values)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Can only sub vector to vector")
        elif other.size != self.size:
            raise ValueError("Can only sub to same size vector")
        values = [x - y for x, y in zip(self.values, other.values)]
        return Vector(values)

    def __rsub__(self, other):
        return self - other

    def __truediv__(self, other):
        if not isinstance(other, numbers.Number):
            raise TypeError("Can only div vector by number")
        return Vector([x / other for x in self.values])

    def __rtruediv__(self, other):
        raise TypeError("Can only div vector by number")

    def __mul__(self, other):
        if isinstance(other, numbers.Number):
            return Vector([x * other for x in self.values])
        elif isinstance(other, Vector):
            values = [x * y for x, y in zip(self.values, other.values)]
            return Vector(values)
        raise TypeError("Can only mult vector with number or vector")

    def __rmul__(self, other):
        return self * other
