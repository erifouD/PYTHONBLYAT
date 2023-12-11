n = int(input('Введите размер списка: '))
x = []
for i in range(n):
    print('Введите', i+1, 'элемент: ')
    x.append(float(input()))
a = sum(x)
b = 1
for item in x:
    b *= item
print('Сумма равна: ',  a)
print('Произведение равно: ', b)
    
