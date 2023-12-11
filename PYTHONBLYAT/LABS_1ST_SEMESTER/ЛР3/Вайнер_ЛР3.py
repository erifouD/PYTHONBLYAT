'''a = int(input('Введите целое число \n'))
b = int(input('Введите целое число \n'))
c = int(input('Введите целое число \n'))
if 1 <= a <= 3:
    print('число, принадлежащие отрезку',a)

if 1 <= b <= 3:
    print('число, принадлежащие отрезку',b)

if 1 <= c <= 3:
    print('число, принадлежащие отрезку',c)
'''
print('1 - кг','2 - мг','3 - гр','4 - т','5 - цт', sep = '\n')
num = int(input('Введите номер'))
if 1 <= num <= 5:
    mass = int(input('Введите массу'))
    if num == 1:
        print(mass, 'кг')
        
    elif num == 2:
        print(mass / 10**6,'кг')

    elif num == 3:
        print(mass / 10**3,'кг')

    elif num == 4:
        print(mass *10**3,'кг')

    elif num == 5:
        print(mass * 10**2,'кг')

else:
    print('нужно число от 1 до 5')

