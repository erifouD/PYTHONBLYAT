from math import sqrt
def T2():
    S1 = int(input("Enter the first side:"))
    S2 = int(input("Enter the second side:"))
    S3 = int(input("Enter the third side:"))
    S4 = int(input("Enter the fourth side:"))
    D = int(input("Enter the diagonal side:"))
    p1 = (S1 + S2 + D) / 2
    p2 = (S3 + S4 + D) / 2
    SQ1 = sqrt(p1 * (p1 - S1) * (p1 - S2) * (p1 - D))
    SQ2 = sqrt(p2 * (p2 - S3) * (p2 - S4) * (p2 - D))
    print(SQ1 + SQ2)
