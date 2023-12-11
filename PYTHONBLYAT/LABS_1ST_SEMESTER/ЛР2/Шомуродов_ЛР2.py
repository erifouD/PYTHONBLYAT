import math

x = int(input("Введите переменную x:"))
y = float(input("Введите переменную y:"))
z = float(input("Введите переменную z:"))

S1 = -1 ** y + z + z ** x

S2 = (math.exp(x) + math.log(abs(math.sin(y))))/((z ** 4) * 0.87)

S = math.sqrt(S1 + S2)
print("S = {0:.2f}".format(S))
