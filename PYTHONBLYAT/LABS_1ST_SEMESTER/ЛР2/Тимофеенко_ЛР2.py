import math
a = float(input("Введите переменную a:"))
b = float(input("Введите переменную b:"))
d = ((math.pow(math.pi,2)*math.sqrt((a**3)-(b**3)))-((math.pow(math.e,0.5))+math.log10(math.fabs(a*b)))/(math.pow(0.5,8)))
print("d={0:.2f}".format(d))
            


