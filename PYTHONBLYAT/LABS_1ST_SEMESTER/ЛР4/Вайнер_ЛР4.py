'''a = float(input('Введите цену 1 кг конфет \n'))

for i in range(1,11):
    cost = a * i
    print(cost,'руб','за',i,'кг конфет')

'''

a = int(input('введите число,  которого начинается отсчёт'))
i = int(input('шаг последовательности'))
co  = 0
total =0
while a >= 0:
    total += a
    a -= i
    co += 1

print(co,total)
