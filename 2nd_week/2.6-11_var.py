"""
Использованы только базовые операторы.﻿
Внутри цикла считаю квадратные контуры.
На каждом шаге цикла заполняю сразу два элемента матрицы
(сумма зеркально расположенных элементов контура одинакова).
с комментариями в коде
"""

n = int(input())

# Создаем нулевую квадратную матрицу заданной размерности
a = [[0 for i in range(n)] for j in range(n)]

# Определяем внутренние счетчики для цикла
i = 0  # строки
j = 0  # столбцы
x = 1  # текущее значение для заполнения ячейки
k = 0  # порядковый номер контура

while x <= n * n:
    a[i][j] = x  # заполняем ячейку текущим значением

    if i != j:  # Только если мы сейчас не на диагонали!
        # Сумма зеркально расположенных элементов одинакова для текущего контура.
        # Она равна нижнему правому значению в контуре, умноженному на 2.
        # Так что на каждом шаге цикла мы заполняем зеркальный элемент матрицы,
        # просто вычитая текущее x из этой суммы ;)
        a[j][i] = (a[k][k] + (n - k * 2) * 2) * 2 - 4 - x

    if j != n - k - 1:
        # если еще не уперлись в правую границу контура, двигаемся вправо
        j += 1

    elif i != n - k - 1:
        # если еще не уперлись в нижнюю границу контура, двигаемся вниз
        i += 1

    elif x != n * n:
        # Если вправо и вниз уже нельзя, значит мы закончили обход текущего контура!
        # Только не забываем проверить, что x не равен n*n, а то будет бо-бо.
        k += 1  # переходим к следующему контуру
        i = j = k  # обход следующего контура начнем с координат [k,k]
        x = a[k][k - 1]  # текущее значение равно наибольшему в старом контуре

    x += 1  # Ну, и не забываем прибавлять единичку в конце цикла, какое бы условие ни сработало.

# Выводим на печать
for i in a: print(*i)