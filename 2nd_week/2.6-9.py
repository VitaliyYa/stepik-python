"""
Напишите программу, которая считывает список чисел lst из первой строки и число x из второй строки,
которая выводит все позиции, на которых встречается число x в переданном списке lst.

Позиции нумеруются с нуля, если число x не встречается в списке,
вывести строку "Отсутствует" (без кавычек, с большой буквы).

Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.

Sample Input 1:
5 8 2 7 8 8 2 4
8
Sample Output 1:
1 4 5

Sample Input 2:
5 8 2 7 8 8 2 4
10
Sample Output 2: Отсутствует
"""

lst = [int(i) for i in input().split()]
x = int(input())
count = 0
for i in range(len(lst)):
    if lst[i] == x:
        print(i, end=' ')
        count += 1
if count < 1:
    print('Отсутствует')


# Или с использованием list comprehensions:

l, n = [int(i) for i in input().split()], int(input())
print(*[x for x in range(len(l)) if l[x] == n] if n in l else ['Отсутствует'])
