"""Создайте словарь с количеством элементов не менее 5-ти.
Поменяйте местами первый и последний элемент объекта.
Удалите второй элемент. Добавьте в конец ключ «new_key» со значением «new_value».
Выведите на печать итоговый словарь. Важно, чтобы словарь остался тем же (имел тот же адрес в памяти).
"""

numb = {}
for i in range(1, 6):
    numb [i] = i
numb[1], numb[5] = numb[5], numb[1]
del numb [2]
numb['new key'] = 'new_value'
print(numb)
