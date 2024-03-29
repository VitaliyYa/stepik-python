"""
Узнав, что ДНК не является случайной строкой, только что поступившие в Институт биоинформатики
студенты группы информатиков предложили использовать алгоритм сжатия, который сжимает повторяющиеся символы в строке.

Кодирование осуществляется следующим образом:
s = 'aaaabbсaa' преобразуется в 'a4b2с1a2',
то есть группы одинаковых символов исходной строки заменяются на этот символ
и количество его повторений в этой позиции строки.

Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом
и выводит закодированную последовательность на стандартный вывод. Кодирование должно учитывать регистр символов.

Sample Input 1: aaaabbcaa
Sample Output 1: a4b2c1a2

Sample Input 2: abc
Sample Output 2: a1b1c1
"""

dna = input()
code_dna = ""
i = 1
j = 1
while i <= len(dna):
    count = 1
    while (i <= len(dna) - 1) and (dna[i] == dna[i - 1]):
        count = count + 1
        i += 1
    code_dna = code_dna + dna[i - 1] + str(count)
    i += 1
print(code_dna)
