def exc(i):
    try:
        First = int(input("Введите первое число: "))
        Second = int(input("Введите второе число: "))
        return [f"{First}+{Second}={First+Second}", 1]
    except:
        attempt = ""
        if(i == 3): attempt = "попытка"
        else: attempt = "попытки"
        return [f"Некорректные данные. Осталось {5 - 1 - i} {attempt}\n", 0]


for i in range(5):
    Data = exc(i)
    if(i == 4 and not Data[1]): 
        print("Ввод не удался")
        break
    print(Data[0])
    if(Data[1]): break