print('Введите с() и в скобках через запятую величины катетов ')
def h():
    a1 = int(input('Введите 1 катет 1 треугольника '))
    b1 = int(input('Введите 2 катет 1 треугольника '))
    a2 = int(input('Введите 1 катет 2 треугольника '))
    b2 = int(input('Введите 2 катет 2 треугольника '))
    c1 = (a1**2 + b1**2)**0.5
    c2 = (a2**2 + b2**2)**0.5
    return c1, c2
c1, c2 = h()
print('Наибольшая из гипотенуз 2 треугольников равна',max(c1,c2),
      '\n Наименьшая из гипотенуз 2 треугольников равна',min(c1,c2))

    
    


    
