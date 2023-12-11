a = int(input("Введите цену: "))
if a > 1000:
    print("Стоимость: ", a*0.95)
elif a > 500:
    print("Стоимость: ", a*0.97)
else:
    print("Стоимость: ", a)
