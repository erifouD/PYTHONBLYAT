n=int(input("Введите длину массива"))
a=[]
for i in range(n):
    print("Введите", i , "элемент:")
    a.append(int(input()))
print("Исходный массив:",a)
sum=0
for num in a:
    sum+=num
arg=sum/len(a)
print("Среднее арифмитическое:",arg)
for i in range(n):
    if a[i]>arg:
        a[i]=1
print("Полученный массив:", a)
    
