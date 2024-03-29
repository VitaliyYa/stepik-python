"""
Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк,
заканчивающихся строкой, содержащей только строку "end" (без кавычек)

Программа должна вывести матрицу того же размера,
у которой каждый элемент в позиции i, j равен сумме элементов первой матрицы на позициях
(i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент находится с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.

Sample Input 1:
9 5 3
0 7 -1
-5 2 9
end
Sample Output 1:
3 21 22
10 6 19
20 16 -1

Sample Input 2:
1
end
Sample Output 2:
4
"""

c = []
while True:
    a = [i for i in input().split()]
    if a == ['end']:
        break
    c.append(a)
n, m = len(c), len(c[0])
for i in range(n):
    for j in range(m):
        x = int(c[i][j - 1]) + int(c[i][j + 1 - m]) + int(c[i - 1][j]) + int(c[i + 1 - n][j])
        print(x, end=' ')
    print()


# Или не понятный дурдом:
string = m = []
while string != 'end':
    string = input()
    m.append(list(map(int, string.split(' ')))) if string != 'end' else None
li, lj = len(m), len(m[0])
new = [[sum([m[i - 1][j], m[(i + 1) % li][j], m[i][j - 1], m[i][(j + 1) % lj]]) for j in range(lj)] for i in range(li)]
[print(' '.join(map(str, row))) for row in new]
