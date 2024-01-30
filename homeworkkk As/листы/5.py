m = [int(x) for x in input('введите числа через пробел: ').split()]
for i in m:
    if len(m) > 1:
        if m[i+2]==m[i+1]:
            continue
        else:
            print('нет')
    else:
        print('нет')
print('Да')