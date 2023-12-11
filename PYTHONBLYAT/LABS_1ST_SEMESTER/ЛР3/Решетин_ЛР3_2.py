a, b =int(input('Введите первое число: ')),int(input('Введите второе число: '))
if ((a>0) and (b>0)) or ((a<=0) and (b<=0)):
    print((a*b)**0.5)
else:
    print((a+b)/2)
