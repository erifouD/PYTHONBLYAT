a = [1, -3, -7, 6, -6, 1, 7, -5, -7, 4]

for i in range(len(a) - 1):
    if a[i] < 0 and a[i + 1] < 0:
        print(a[i], a[i+1])

#End

#Next
b = [1, 6, 1, 7, 8, 9, 1, 5, 7, 8]
for i in range(len(b)):
    if i >= len(b): 
        break
    if b.count(b[i]) > 1: 
        b.pop(i)
        i -= 1
print(b)