def getSum(value):
    res=1
    for i in range(2, int(value**0.5)+1):
        if value%i==0:
            res+=i+value//i
    return res
    
for i in range(10, 10000):
        sum1=getSum(i)
        sum2=getSum(sum1)
        if sum2==i and sum1 != sum2:
            print(i, sum1)
