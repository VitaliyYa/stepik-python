"""
task link: https://stepik.org/lesson/5047/step/6?thread=solutions&unit=1086
"""


num = int(input())
val = num%100
if 10 < val < 20:
    print(num, 'программистов')
else:
    val = num % 10
    if val == 1:
        print(num, 'программист')
    elif 1 < val < 5:
        print(num, 'программиста')
    else:
        print(num, 'программистов')
