import math
a=float(input('введите переменную а: ', ))
b=float(input('введите переменную b: ', ))
c=float(input('введите переменную c: ', ))
t=((math.log(abs(a**2-b**a-c))/math.sin(a)+16.9**3/math.pi))**2
print('t={0:.2f}'.format(t))
