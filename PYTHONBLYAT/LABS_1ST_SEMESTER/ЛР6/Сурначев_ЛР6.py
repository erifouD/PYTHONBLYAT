N = int(input('Введите количество элементов в списке '))
y = 100000000000
x = [ int(input('Введите список')) for i in range(N) ]
for i in range(N):
    if x[i] % 2 > 0:
        y = x[i]
print('Наименьшее нечетное число в списке ', y)
        
    
