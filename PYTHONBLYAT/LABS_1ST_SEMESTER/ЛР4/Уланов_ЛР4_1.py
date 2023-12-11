print("Введите наименьшее чило диапазона")
a=int(input())
print("Введите наибольшее число диапазона")
b=int(input())
sum = 0
for i in range (a,b+1):
    sum=sum+i
print("Сумма ряда:",sum)
