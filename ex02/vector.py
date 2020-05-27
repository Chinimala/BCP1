import numbers


class Vector:
    def __init__(self, arg):
        if isinstance(arg, int):
            self.values = [float(x) for x in range(0, arg)]
        elif isinstance(arg, list)\
                and all([isinstance(n, float) for n in arg]):
            self.values = arg
        elif isinstance(arg, range):
            self.values = [float(x) for x in arg]
        elif isinstance(arg, tuple) and len(arg) == 2\
                and all([isinstance(n, int) for n in arg]):
            self.values = [float(x) for x in range(*arg)]
        else:
            raise TypeError("argument must be int, range, tuple of 2 int"
                            "or list of floats")
        self.size = len(self.values)

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
        raise NotImplementedError("Can only div vector by number")

    def __mul__(self, other):
        if isinstance(other, numbers.Number):
            return Vector([x * other for x in self.values])
        elif isinstance(other, Vector):
            if self.size != other.size:
                raise ValueError("Can only mult same size vectors")
            return sum([x * y for x, y in zip(self.values, other.values)])
        raise TypeError("Can only mult vector with number or vector")

    def __rmul__(self, other):
        return self * other
