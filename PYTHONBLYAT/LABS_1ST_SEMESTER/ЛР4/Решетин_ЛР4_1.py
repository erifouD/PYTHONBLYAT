a=int(input("Введите первое число:\n"))
b=int(input("Введите второе число больше первого:\n"))
n=b-a+1
s=0
for i in range(n):
    s+=a
    a+=1
print("Сумма чисел:\n",s)
