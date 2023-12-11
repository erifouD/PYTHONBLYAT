n=int(input('количество элементов массива: '))
a=[]
for i in range(n):
    print('введите', i, 'элемент')
    a.append(int(input()))
print('исходный массив:', a)
q=min(a)
print('индекс минимального элемента:', a.index(q))
    
             
             
