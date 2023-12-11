n=int(input('количество элементов массива: '))
a=[]
for i in range(n):
    print('введите', i, 'элемент')
    a.append(int(input()))
print('исходный массив:', a)
q=[]
for i in range(n):
    if a[i]>0:
        q.append(a[i])
print('массив положительных чисел', q)
z=[]
for i in range(n):
    if a[i]<=0:
        z.append(a[i])
print('массив неположительных чисел', z)
