A = [5, 13, 1, 6, 8, 5, 8, 1, 6, 3]
Sum = 0
Mul = 1
for i in A:
    Sum += i
    Mul *= i

print("Sum = ", Sum, "Mul = ", Mul)

#Next
M = [0.12, 0.5, 6.12, 7.19, 0, 8.13, 9.642, 0, 12.78, 0, 6.438]
Ave = 0
for i in M:
    Ave += i

Ave /= len(M)

for i in range(len(M)):
    if M[i] == 0:
        M[i] = Ave
print(M)