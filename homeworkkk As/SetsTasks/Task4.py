"""
Вася давно мечтает выиграть олимпиаду по информатике.
У него всего три слабых места: циклы, массивы и строки.
Перед сегодняшним турниром Вася провёл интенсивную подготовку, в ходе которой он решил A задач на циклы,
B задач на массивы и C задач на строки.
Впоследствии выяснилось, что из решённых задач D были и на циклы, и на массивы, E – на циклы и на строки,
F – на строки и на массивы. И даже было G задач, которые включали и циклы, и строки, и массивы.
Помогите Васе вычислить, сколько всего различных задач он решил.
Введите результат для всех 3 входных данных
"""
first = "0 0 0 0 0 0 0"  # Вывод должен быть 0
second = "1 1 1 0 0 0 0"  # Вывод должен быть 3
third = "1 1 1 1 1 1 1"  # Вывод должен быть 1


def TasksResult(list):
    flist = list.split()
    res = []
    for i in flist:
        res.append(int(i))
    print(res[0] + res[1] + res[2] - res[3] - res[4] - res[5] + res[6])


TasksResult(first)
TasksResult(second)
TasksResult(third)
