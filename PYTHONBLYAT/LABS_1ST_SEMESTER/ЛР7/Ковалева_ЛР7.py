sklad_1={'Абрикос':50,'Авокадо':50, 'Алыча':50,'Апельсин':50, 'Арбуз':50}
sklad_2={'Гранат':20,'Грейпфрут':4, 'Груша':10,'Дыня':10, 'Инжир':20, "Кешью":100}
zakaz={}

count = 0
while count < 4:
    nazvanie = input('Введите название фрукта: ')
    kolichestvo = int(input('Введите количество фруктов: '))

    if nazvanie in sklad_1:
        if kolichestvo <= sklad_1[nazvanie]:
            sklad_1[nazvanie]-=kolichestvo
            zakaz[nazvanie]=kolichestvo
            count+=1
        else:
            print('На складе осталось только', sklad_1[nazvanie], 'фруктов',nazvanie)

    elif nazvanie in sklad_2:
        if kolichestvo <= sklad_2[nazvanie]:
            sklad_2[nazvanie]-=kolichestvo
            zakaz[nazvanie]=kolichestvo
            count+=1
        else:
            print('На складе осталось только', sklad_2[nazvanie], 'фруктов',nazvanie)
    else:
        print('Фрукт', nazvanie, 'не найден на складе')

print('Склад 1:')
print('Исходное количество на складе:', sklad_1)
print('Остаток на складе', sklad_1)
print('Заказ:', zakaz)

print('Склад 2:')
print('Исходное количество на складе:', sklad_2)
print('Остаток на складе', sklad_2)
print('Заказ:', zakaz)
