r=[]
n = int(input("Введите кол-во элементов в массиве: "))
for i in range(n):
    r.append(input('Введите число: '))
 
print('максимальный элемент: ' + str(max(r)))
print('обратный порядок: ' + str(list(reversed(r))))

##A = []
##B = []
##
##for i in range(10):
##    A.append(input('Введите число для массива (A): '))
##for j in range(10):
##    B.append(input('Введите число для массива (B): '))
##
##x = A
##A = B
##B = x
##
##print('A: ', A)
##print("B: ", B)
