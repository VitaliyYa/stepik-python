"""
Link task: https://stepik.org/lesson/3373/step/6?unit=956
"""

FullString = [str(i).lower() for i in input().split()]
Set = set(FullString)
Counter = 0
for i in Set:
    Counter = FullString.count(i)
    print(str(i), str(Counter))
