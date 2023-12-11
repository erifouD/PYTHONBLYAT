a=[1, 2, 4, 5, 7, 8, 25, 15, 666, 6, 10]
b=[]
for i in range(len(a)):
    if (a[i]%2==0) and (a[i] <10):
        b.append(a[i])
if len(b)==0:
    print('Таких чисел нет')
b.sort()
print(b)
