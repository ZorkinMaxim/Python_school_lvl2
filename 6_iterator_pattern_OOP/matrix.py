class Matrix:
    def __init__(self, matrix2d):
        self.matrix2d = matrix2d
        if len(self.matrix2d) != 2:
            raise ValueError("I can work only with 2d matrix")

    def __str__(self):
        out = "["
        for row in self.matrix2d:
            for val in row:
                out += f"{val:4}, "
            out += "\n"
        out += "]"

    def __iter__(self):
        return MItarator(self)


class MItarator:
    def __init__(self, m):
        self.m = m
        self.index = 0

    def __next__(self):
        if self.index >= len(self.m.matrix2d):
            raise StopIteration
        n = self.m.matrix2d[self.index]
        self.index += 1
        return n

