'''Программа должна:
Запрашивать категорию товара.
Если покупатель ввёл "продукты", то запросить ввод цены.
 2.1 Если цена до 100 руб, то вывести "Попробуйте нашу выпечку!"
 2.2 Если цена от 100 руб (включительно) до 500, то вывести "Как насчёт орехов в шоколаде?"
 2.3 Если цена от 500 руб (включительно), то вывести "Попробуйте экзотические фрукты!"
3. Для всех остальных категорий сразу вывести: "Загляните в товары для дома!" '''

cat = input('Укажите категорию продуктов: ').lower()
if cat == 'продукты':
    cen = int(input('Введите цену товара:'))
    if cen < 100:
        print("Попробуйте нашу выпечку!")
    elif cen > 100 and cen < 500:
        print("Как насчёт орехов в шоколаде?")
    elif cen > 500:
        print("Попробуйте экзотические фрукты!")
else:
    print("Загляните в товары для дома!")
