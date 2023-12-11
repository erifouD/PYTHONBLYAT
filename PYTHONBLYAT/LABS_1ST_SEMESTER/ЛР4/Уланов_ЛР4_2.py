K = 1
N = int(input("Введите число "))
n = N
while N != 2:
    N /= 2
    K += 1
    
print(n, "это 2 в", K, "степени")
