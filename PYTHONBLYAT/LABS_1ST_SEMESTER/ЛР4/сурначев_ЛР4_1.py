n = int(input('Введите количество элементов последовательности '))
summ = 0
while n != 0:
    y = int(input('Введите член последовательности, но так чтобы первый был четным '))
    n = n - 1
    while y % 2 == 0:
        summ = summ + y
        y = y + 1
print(summ)
    
    
    
