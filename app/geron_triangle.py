from math import sqrt


def geron_triangle(a, b, c):
    p = (float(a) + float(b) + float(c)) / 2
    return sqrt(float(p) * (float(p) - float(a)) * (float(p) - float(b)) * (float(p) - float(c)))
