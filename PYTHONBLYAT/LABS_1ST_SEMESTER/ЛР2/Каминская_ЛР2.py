import math
a = float(input("Введите переменную a:"))
b = float(input("Введите переменную b:"))
c = float(input("Введите переменную c:"))
t = ((a**(-1)+b**(-2)+c**(-3))/(math.pi*math.fabs(a*b)-c))+((math.exp(c)+math.cos(b))/math.cos(c))
print("t= {0:.2f}".format(t))
