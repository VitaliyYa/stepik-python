"""
task link: https://stepik.org/lesson/5047/step/3?thread=solutions&unit=1086

Напишите простой калькулятор, который считывает с пользовательского ввода три строки:
первое число, второе число и операцию, после чего применяет операцию к введённым числам
("первое число" "операция" "второе число") и выводит результат на экран.

Поддерживаемые операции: +, -, /, *, mod, pow, div, где
mod — это взятие остатка от деления,
pow — возведение в степень,
div — целочисленное деление.

Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".

Обратите внимание, что на вход программе приходят вещественные числа.
"""

a, b = float(input()), float(input())
operation = input()

if operation == "mod":
    if b != 0:
        print(a % b)
    else:
        print('Деление на 0!')
elif operation == "pow":
    print(a ** b)
elif operation == "div":
    if b != 0:
        print(a // b)
    else:
        print('Деление на 0!')
elif operation == "+":
    print(a + b)
elif operation == "-":
    print(a - b)
elif operation == "/":
    if b != 0:
        print(a / b)
    else:
        print('Деление на 0!')
elif operation == "*":
    print(a * b)
