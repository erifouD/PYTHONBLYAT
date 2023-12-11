from math import sqrt

def divs_amount(X):
    counter = 0
    for i in range(1, X + 1):
        if X % i == 0:
            counter += 1
    return counter

def max_divs(M, N):
    max_divss = 0
    number = 0
    for i in range(M, N + 1):
        if divs_amount(i) >= max_divss:
            max_divss = divs_amount(i)
            number = i
    print("Число ", number, " имеет максимальное количество делителей - ", max_divss)

def STriangle(s1, s2, d):
    p = (s1 + s2 + d) / 2
    return sqrt(p * (p - s1) * (p - s2) * (p - d))



M = int(input("Начало интервала: "))
N = int(input("Конец интервала: "))
max_divs(M, N)

s1 = int(input("Введите 1-ю сторону: "))
s2 = int(input("Введите 2-ю сторону: "))
s3 = int(input("Введите 3-ю сторону: "))
s4 = int(input("Введите 4-ю сторону: "))
d = int(input("Введите диагональ: "))
print("Площадь четырехугольника равна ", STriangle(s1, s2, d) + STriangle(s3, s4, d))
