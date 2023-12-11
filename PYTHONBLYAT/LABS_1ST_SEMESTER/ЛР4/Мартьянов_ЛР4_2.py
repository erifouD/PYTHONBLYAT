MIN=int(input("Минимум функции: "))
MAX=int(input("Максимум функции: "))
M=float(input("Шаг: "))
while MIN <= MAX:
    print("x = ", MIN, ", y = ", (-0.5 * MIN + MIN))
    MIN += M
