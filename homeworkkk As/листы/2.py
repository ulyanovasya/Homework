mark = [int(x) for x in input('Введите оценки через пробел: ').split(' ')]
print(mark)
print('Количество оценок: ', len(mark))
print('Успеваемость: ', (sum(mark)/len(mark)*100))