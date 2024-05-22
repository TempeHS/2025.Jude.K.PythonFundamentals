class Object:
    def __init__(self, colour, x, y, z):
        self.colour = colour
        self.x = x
        self.y = y
        self.z = z


class Square:
    def __init__(self, l, w, h):
        self.l = l
        self.w = w
        self.h = h

    def square_calc(l, w, h):
        Square.parameter = (l * 2) + (w * 2)
        Square.area = l * w
        Square.volume = l * w * h


class Circle:
    def __init__(self, pi, r):
        self.pi = int(3.14)
        self.r = r

    def circlecalc(pi, r):
        Circle.cirum = 2 * pi * r
        Circle.area = pi * r * 2
        Circle.volume = (4 / 3) * pi * r * 3
        Circle.volume3d = 4 * pi * r * 2


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def trianglecalc(a, b, c, h):
        Triangle.Height = (a * 3**3) / 2
        Triangle.area = (1 / 2) * b * h
        Triangle.pyrovolume = (1 / 3) * Triangle.area * h
