"""
Представьте, что сумма за пользование услугами такси складывается из
базового тарифа в размере $4,00 плюс $0,25 за каждые 140 м поездки.
Напишите функцию, принимающую в качестве единственного параметра
расстояние поездки в километрах и возвращающую итоговую сумму опла-
ты такси.
"""


def cost(lenght):
    fin_cost = 4.00 + 0.25 * (lenght * 1000 // 140)
    print('заплати вот столько: ', fin_cost)


cost(float((input(print('сколько проехал? ')))))
