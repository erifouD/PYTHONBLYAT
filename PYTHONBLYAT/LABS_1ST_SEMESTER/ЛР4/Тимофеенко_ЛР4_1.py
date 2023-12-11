a = int(input("Введите число с клавиатуры"))
count = 0
total = 0
for i in range(a,201):
    count += 1
    total += i
print(total//count)
