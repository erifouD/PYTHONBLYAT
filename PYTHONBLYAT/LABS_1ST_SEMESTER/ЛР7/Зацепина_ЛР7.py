#Вариант 7.
def input_fruit():
    a=input("Введите название фрукта:")#название фрукта
    b=int(input("Введите количество фруктов:"))#количество фруктов
    return(a, b)
fruit_dict={}
while True:
    fruit, b=input_fruit()
    if fruit in fruit_dict:
        fruit_dict[fruit]+=b
    else:
        fruit_dict[fruit]=b
    apple_fruit=fruit_dict.get("яблоко", 0)
    if apple_fruit >=10:
        break
print(fruit_dict)
