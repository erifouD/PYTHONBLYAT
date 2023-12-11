import math
def F (a):
    s=(a*((math.sqrt(3)/2)*a))/2
    return (s)
a=int(input("Введите сторону шестиугольника: "))
print('{:.3f}'.format(F(a)*6))
