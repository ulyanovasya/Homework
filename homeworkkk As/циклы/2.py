start = input().lower()
if start == 'game':
    print('Угадай число')
    pop = input()
    i = 1
    while pop != 'off':
        pop = input()
        if int(pop) != 5 and i != 3:
            i += 1
        print('Вы выиграли!')