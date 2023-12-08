from math import sqrt

def Task7():
    print("Задание 7")
    a = []
    b = []
    for i in range(3):
        a.append(float(input(f"Введите {i+1}-ю сторону первого треугольника: ")))
    for i in range(3):
        b.append(float(input(f"Введите {i+1}-ю сторону второго треугольника: ")))

    #дальнейшие вычисления производятся по формуле Герона
    p1 = (a[0] + a[1] + a[2]) / 2
    S1 = sqrt(p1 * (p1 - a[0]) * (p1 - a[1]) * (p1 - a[2]))

    p2 = (b[0] + b[1] + b[2]) / 2
    S2 = sqrt(p2 * (p2 - b[0]) * (p2 - b[1]) * (p2 - b[2]))

    if S1 == S2:
        print("Площади треугольников равны")
    else:
        print("Площади треугольников не равны")



def Task13():
    print("Задание 13")
    a = []
    #ввод значений
    for i in range(3):
        a.append(float(input(f"Введите {i+1}-ю сторону треугольника: ")))
    max_index = 0 #индекс гипотенузы в массиве
    max_val = max(a) #длина гипотенузы
    
    for i in range(3):
        if a[i] == max_val:
            max_index == i
            a.pop(i)
            break

    if (a[0] ** 2 + a[1] ** 2) == max_val ** 2:
        print("Площадь треугольника: ", a[0] * a[1] / 2)
    else:
        print("Периметр: ", a[0] + a[1] + max_val)


Task7()
print("=====================================================================")
Task13()
