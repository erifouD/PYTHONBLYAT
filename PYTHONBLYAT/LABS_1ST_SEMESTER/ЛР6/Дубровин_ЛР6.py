m = [9,2,7,1,6,3,8,6,5,2]
maxi = max(m)
count_min = 0
count_max = 0

for i in m:
    if i > maxi:
        count_max += 1
    if i < maxi:
        count_min += 1

print("Min count: ", count_min, "\nMax count: ", count_max)

#second task
g = []
summa = 0
for i in range(10):
    g.append(int(input()))
    if g[i] > 5: summa += g[i]
print(summa)    
