"""
Создайте функцию которая принимает на вход 3 именованных параметра, выведите на печать значения этих параметров,
но только в том случае если они не равны None.
"""


def tri(p1 = None, p2 = None, p3 = None):
    if p1:
        print('first:', p1)
    if p2:
        print('second:', p2)
    if p3:
        print('third:', p3)


tri(input(), input(), input())
