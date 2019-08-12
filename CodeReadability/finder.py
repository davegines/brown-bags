class Finder:
    def find(self, x):
        i = 0
        o = None

        if x is None:
            return None
        if len(x) == 1:
            return x[0]

        o = x[len(x) - 1]
        while i < len(x) - 1:
            if x[i].age > x[i + 1].age:
                o = x[i]
            i += 1

        return o


class P:
    def __init__(self, name, age):
        self.name = name
        self.age = age
