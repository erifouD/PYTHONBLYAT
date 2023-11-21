from math import sqrt
def T1(): 
    N = int(input("Enter the end value of the sequence: "))
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))
    for i in range(100, N+1):
        if i == a * 100 + b * 10 + c: print(i)
        if i == a * 100 + c * 10 + b: print(i)
        if i == b * 100 + a * 10 + c: print(i)
        if i == b * 100 + c * 10 + a: print(i)
        if i == c * 100 + b * 10 + a: print(i)
        if i == c * 100 + a * 10 + b: print(i)


def T2():
    S1 = int(input("Enter the first side: "))
    S2 = int(input("Enter the second side: "))
    S3 = int(input("Enter the third side: "))
    S4 = int(input("Enter the fourth side: "))
    D = int(input("Enter the diagonal side: "))
    p1 = (S1 + S2 + D) / 2
    p2 = (S3 + S4 + D) / 2
    SQ1 = sqrt(p1 * (p1 - S1) * (p1 - S2) * (p1 - D))
    SQ2 = sqrt(p2 * (p2 - S3) * (p2 - S4) * (p2 - D))
    print(SQ1 + SQ2)