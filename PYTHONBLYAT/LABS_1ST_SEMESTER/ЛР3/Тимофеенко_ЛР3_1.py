import math
x=float(input("Введите первое число: "))
y=float(input("Введите второе число: "))
z=float(input("Введите третье число: "))
if x > y and x > z:
    print("синус максимального из 3 заданных чисел = ", math.sin(x))
elif y > z and y > x:
    print("синус максимального из 3 заданных чисел = ", math.sin(y))
else:
    print("синус максимального из 3 заданных чисел = ", math.sin(z))
