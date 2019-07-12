"""
link task: https://stepik.org/lesson/3373/step/7?unit=956
"""

# Считайте, что функция f(x) уже определена выше. Определять её отдельно не требуется.
n = int(input())

dic = {}

for n in range(0, n):
    n = int(input())
    if dic.get(n) == None:
        dic.setdefault(n, f(n))
    print(dic[n])
