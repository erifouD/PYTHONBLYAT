import math
x = float(input("Первое число: "))
y = float(input("Второе число: "))
if x>0:
    if y>0:
        print("Среднее геометрическое: ", math.sqrt(x*y))
    else:
        print("Среднее арифметическое: ", (x+y)/2)    
elif x<0:
    if y<0:
        print("Среднее геометрическое: ", math.sqrt(x*y))
    else:
        print("Среднее арифметическое: ", (x+y)/2)
else:
    print("Среднее арифметическое: ", (x+y)/2)
