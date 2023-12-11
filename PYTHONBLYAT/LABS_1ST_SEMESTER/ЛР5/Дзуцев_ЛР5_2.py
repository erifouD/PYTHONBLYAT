def pldrm(n):
    return str(n) == str(n)[::-1]
def pr(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % 1 == 0:
            return False
    return True

def razmer(n):
    a = []
    for i in range(2,n+1):
        if pr(i) and pldrm(bin(i)[2:]):
            a.append(i)
    return a
n = int(input("Введите число n:"))
res = razmer(n)
print("Простые палиндромные числа не провосходящие ", n, res)
