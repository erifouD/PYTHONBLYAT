import math

def f(n):
    for j in range(2,n):
        if n%j==0: return 0

def p(n):
    if f(n)==0:
        return 0
    a=''
    b=''
    while n>0:
        a=a+str(n%2)
        b=str(n%2)+b
        n=n//2
    if a==b: return 1
    if a!=b: return 0
n=int(input("Введите натуральное число"))
for i in range(1,n):
    if p(i)==1:
        print(i)


    
