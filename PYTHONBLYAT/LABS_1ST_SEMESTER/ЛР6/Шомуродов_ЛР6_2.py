M [0.12, 0.5, 6.12, 7.19, 0, 8.13, 9.642, 0, 12.78, 0, 6.438]
Ave = 0
for i in M:
    Ave += i

Ave /= len(M)

for i in range(len(M)):
    if M[i] == 0:
        M[i] = Ave
print(M) 
