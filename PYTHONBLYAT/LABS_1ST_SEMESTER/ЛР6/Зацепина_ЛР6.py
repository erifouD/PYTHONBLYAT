#Вариант 7. 1 задание
from random import *
z=0
y=1
u=[randint(0, 100) for i in range(4, 10)]
for i in u:
    if i%2:
        y=y*i
    else:
        z=z+i
print(u)
print("Сумма чётных чисел:", z)
print("Произведение нечётных чисел:", y)
print()
print()
#2 задание
n=int(input("Введите длину массива:",))
f=[]
for i in range(n):
    print("Введите", i,"элемент:")
    f.append(float(input()))
print("Исходный массив:", f)
imin, imax=f.index(min(f)), f.index(max(f))
f[imin], f[imax]=f[imax], f[imin]
print("Полученный массив", f)
