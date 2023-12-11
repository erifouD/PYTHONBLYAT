from random import*
arr=[randint(5,30) for i in range(15)]
print(arr)
for i in range(len(arr)):
    if arr[i]<10:
        arr[i]=0
    if arr[i]>20:
        arr[i]=1
print(arr)
