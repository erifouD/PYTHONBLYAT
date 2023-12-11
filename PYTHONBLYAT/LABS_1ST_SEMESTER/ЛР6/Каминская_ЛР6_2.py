n = int(input('Введите размер списка: '))
x = []
for i in range(n):
    print('Введите ', i+1, 'элемент: ')
    x.append(float(input()))
a = sum(x)/n
for i in range(n):
    if x[i] == 0:
        x[i] = a
print(x)
