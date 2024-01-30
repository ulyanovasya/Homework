mark = [int(x) for x in input('Введите оценки через пробел: ').split(' ')]
print('У вас', mark.count(5), 'оценок "5"')
print('У вас', mark.count(5)*100/len(mark), 'процентов "5"')