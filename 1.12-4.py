"""
task link: https://stepik.org/lesson/5047/step/4?thread=solutions&unit=1086
"""

fig = input()
if fig == 'треугольник':
    a, b, c = float(input()), float(input()),  float(input())
    p = ((a+b+c)/2)
    s = ((p * (p - a) * (p - b) * (p - c))**0.5)
    print(s)
elif fig == 'прямоугольник':
    a, b = float(input()), float(input())
    print(a*b)
elif fig == 'круг':
    r = float(input())
    print(3.14*r*r)
else:
    print('Неизвестная фигура')
