def FindNumbers(N,digits):
    k=0
    flag=1
    for i in range(100,N+1):
        for ch in str(i):
            if ch not in digits:
                flag=0
        if flag==1:
            k+=1
        flag=1
    return(k)
print("Введете N в пределах от 210 до 231:")
N=int(input())
print("Введите цифры a,b,c")
digits=input()
print("В диапазоне от 100 до ",N,"чисел состоящих из цифр ",digits," ровно: ",FindNumbers(N,digits))  
