import math
x=int(input("Введите переменную x:"))
y=float(input("Введите переменную y:"))
z=float(input("Введите переменную z:"))
x=math.fabs(x)
S=(math.sqrt( x ** y + y ** z + z ** x + (math.exp(x) + math.log(math.fabs(math.sin(y))))/(z ** 4 * 0.87)))
print("S={0:.2f}".format(S))
