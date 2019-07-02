"""
link task: https://stepik.org/lesson/5047/step/1?unit=1086
"""

from math import sqrt


a, b, c = int(input()), int(input()), int(input())


def halfp(a, b, c):
    p = (a + b + c) / 2
    return p


P = halfp(a, b, c)
print(sqrt(P * ((P - a) * (P - b) * (P - c))))
