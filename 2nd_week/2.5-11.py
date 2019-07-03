"""
Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения,
которые повторяются в нём более одного раза.

Для решения задачи может пригодиться метод sort списка.

Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.

Sample Input 1: 4 8 0 3 4 2 0 3
Sample Output 1: 0 3 4

Sample Input 2: 10
Sample Output 2:

Sample Input 3: 1 1 2 2 3 3
Sample Output 3: 1 2 3

Sample Input 4: 1 1 1 1 1 2 2 2
Sample Output 4: 1 2
"""

s = [int(i) for i in input().split(' ')]
for i in range(len(s)):
    s[i] = int(s[i])
s.sort()
c = 0
lst = []
for j in range(len(s)):
    if s.count(s[j]) > 1:
        if (s[j] in lst) == 0:
            lst.append(s[j])
for k in lst:
    print(k, end=' ')


# Укороченный вариант:
a, lst = [int(i) for i in input().split()], []
for i in a:
    if a.count(i) > 1 and lst.count(i) == 0:
        lst.append(i)
for i in lst:
    print(i, end=' ')

# совсем компактно С функцией set:
ls = input().split()
print(*(i for i in set(s) if s.count(i) > 1))
