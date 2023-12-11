a=int(input("Введите число А: "))
x=0
K=1
while x<a:
    x+=1/K
    K+=1
K-=1
x-=1/K
print("Наибольшее К: ", K)
print("Сумма: ",x)
