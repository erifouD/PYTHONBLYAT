a = int(input("Введите число, меньше чем 50: "))
sum = 0
for i in range(a, 51):
    sum += i ** 2
    print(sum)
