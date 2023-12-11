import math
x = float(input("Введите первое число: "))
y = float(input("Введите второе число: "))
z = float(input("Введите третье число: "))
if x > y and x > z:
    print("Синус максимального из 3x чисел = ", math.sin(x))
elif y > x and y > z:
    print("Синус максимального из 3x чисел = ", math.sin(y))
else:
    print("Синус максимального из 3x чисел = ", math.sin(z))
    
##
##a = float(input("Введите число: "))
##if a >= 0:
##    print(0.5 - abs(a) ** 0.25)
##else:
##    print((math.sin(a**2) ** 2)/(abs(a+1)))
