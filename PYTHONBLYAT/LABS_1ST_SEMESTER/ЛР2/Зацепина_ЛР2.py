import math
x=float(input("Введите переменную x:"))
y=float(input("Введите переменную y:"))
z=(((math.fabs(math.pow((math.sin(2*x)),2)))-(math.fabs(math.pow((math.cos(3*y)),4))))/(math.pow(math.pi,4))+3.97)+(((math.pow(math.e,-x*y))+10*x*y)/(1.34*math.pow(y,4)))
print("z = {0:.5f}".format(z))
