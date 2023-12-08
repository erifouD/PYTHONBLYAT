import math

def F (x, y):
    numenator = math.cos(y) - math.sqrt(x * y ** 2)
    denumenator = math.log(y) + 0.5 ** 6 + math.cos(y) ** 2
    return (numenator / denumenator)


x = float(input("Введите переменную x:"))
y = float(input("Введите переменную y:")) 
print("z = {0:.2f}".format(F(x, y)))
