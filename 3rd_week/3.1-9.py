"""
Link tak: https://stepik.org/lesson/3372/step/9?unit=955
"""


def modify_list(l):
    l[:] = [i // 2 for i in l if not i % 2]
