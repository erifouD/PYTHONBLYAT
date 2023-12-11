from math import cos
a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))
c = int(input("Введите третье число:"))
d = int(input("Введите четвертое число:"))

if a < b and a < c and a < d:
    print("Косинус минимального числа: ", cos(a))

elif b < a and b < c and b < d:
    print("Косинус минимального числа: ", cos(b))

elif c < b and c < a and c < d:
    print("Косинус минимального числа: ", cos(c))

else:
    print("Косинус минимального числа: ", cos(d))
