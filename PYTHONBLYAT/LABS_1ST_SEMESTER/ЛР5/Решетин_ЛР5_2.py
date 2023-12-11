def F(a,b):
    s=a*b
    return (s)
A=[]
for i in range(3):
    print('Введите стороны', i+1,'-ого прямоугольника')
    a=int(input('a:',))
    b=int(input('b:',))
    A.append(F(a,b))
for i in range(3):
    print('Площадь', i+1,'-ого прямоугольника', A[i])
