a=[1, 3, 5, 7, 8, 23, 15, 666, 999]
b=[]
for i in range(len(a)):
    if a[i]%2==0:
        b.append(a[i])
print(max(b))
