#Вариант 7. Задание 1
import math
def s(X,Y,Z,T):
    l=(X*Y)/2
    s=(Z*T)+l
    return s
A=[]
print("Введите стороны четырёхугольника:")
X=int(input("X:"))
Y=int(input("Y:"))
Z=int(input("Z:"))
T=int(input("T:"))
A.append(s(X,Y,Z,T))
print("Площадь четырёхугольника {:.2f}".format(A[0]))
print()
print()
print()
#Вариант 7. Задание 2
k=int(input("Введите неотрицательно целое число:"))
print(k)
def g(n):
    w=""
    while n!=0:
        w=str(n%8)+w
        n//=8
    return("{0:0>10}".format(w))
print(g(k))
