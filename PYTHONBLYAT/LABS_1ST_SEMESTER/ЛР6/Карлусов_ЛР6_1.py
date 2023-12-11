A=[10,6,9,78,78,10,3,5,9,]
arr=[]
for i in A:
    f=A.count(i)
    if f>1:
        arr.append(i)
if len(arr)==0:
    print("повторяющихся элементов нет")

else:
    print(arr)
