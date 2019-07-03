"""
Паша очень любит кататься на общественном транспорте, а получая билет, сразу проверяет, счастливый ли ему попался.
Билет считается счастливым, если сумма первых трех цифр совпадает с суммой последних трех цифр номера билета.

Однако Паша очень плохо считает в уме, поэтому попросил вас написать программу,
которая проверит равенство сумм и выведет "Счастливый", если суммы совпадают, и "Обычный", если суммы различны.

На вход программе подаётся строка из шести цифр.

Выводить нужно только слово "Счастливый" или "Обычный", с большой буквы.

Sample Input 1: 090234
Sample Output 1: Счастливый

Sample Input 2: 123456
Sample Output 2: Обычный
"""

num = input()
n0, n1, n2, n3, n4, n5 = int(num[0]), int(num[1]), int(num[2]), int(num[3]), int(num[4]), int(num[5])

if n0 + n1 + n2 == n3 + n4 + n5:
    print('Счастливый')
else:
    print('Обычный')