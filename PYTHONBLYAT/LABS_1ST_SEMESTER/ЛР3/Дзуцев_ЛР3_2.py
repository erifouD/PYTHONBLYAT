import math
x = int(input("Введите первое число : "))
y = int(input("Введите второе число : "))
z = int(input("Введите третье число : "))
w = int(input("Введите четвертое число : "))
if x < y and x < z and x < w:
    print(math.cos(x))
elif y < x and y < z and y < w:
    print(math.cos(y))
elif z < y and z < x and z < w:
    print(math.cos(z))
elif w < y and w < z and w < x:
    print(math.cos(w))
    
    


