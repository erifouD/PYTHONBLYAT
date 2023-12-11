import math
x = float(input("Введите X: "))
if x >= 0:
    print(0.5 - abs(x) ** 0.25)
else:
    print((math.sin(x**2) ** 2 ) / (abs(x + 1)))
