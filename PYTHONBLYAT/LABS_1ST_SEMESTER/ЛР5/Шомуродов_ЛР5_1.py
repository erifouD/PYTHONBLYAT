from math import sqrt
def T1():
    N = int(input("Enter the end value of the sequence:"))
    a = int(input("Enter the first number:"))
    b = int(input("Enter the second number:"))
    c = int(input("Enter the third number:"))
    for i in range(100, N+1):
        if i == a * 100 + b * 10 + c: print(i)
        if i == a * 100 + c * 10 + b: print(i)
        if i == b * 100 + a * 10 + c: print(i)
        if i == b * 100 + c * 10 + a: print(i)
        if i == c * 100 + b * 10 + a: print(i)
        if i == c * 100 + a * 10 + b: print(i)
