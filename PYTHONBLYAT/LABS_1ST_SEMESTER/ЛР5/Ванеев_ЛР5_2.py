def st(a,b):
	return(a*b)
A=[]
for i in range(3):
    print('введите стороны ', i+1 ,' треугольника')
    a=int(input('a:'))
    b=int(input('b:'))
    A.append(st(a,b))
for i in range(3):
    print('Площадь прямоугольника ', i+1, '=', round(A[i]))  
