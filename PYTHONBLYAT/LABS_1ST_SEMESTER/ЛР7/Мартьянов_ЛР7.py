
FruitsData = {
    "Абрикос" : [1, 30, 120],
    "Авокадо" : [1, 19, 90],
    "Алыча" : [1, 32, 67],
    "Апельсин" : [1, 67, 129],
    "Арбуз" : [1, 129, 19],
    "Гранат" : [2, 36, 56],
    "Грейпфрут" : [2, 23, 78],
    "Груша" : [2, 57, 20],
    "Дыня" : [2, 48, 45],
    "Инжир" : [2, 12, 54],
    "Кешью" : [2, 31, 73]
}


def InputFruit(Name, Amount):
    FruitsData[Name][1] -= Amount
    return (Name, Amount)

Price = 0
TotalWeight = 0
ApplicationList = []
PriceApplications = []

for i in range(5):
    Name = str(input("Введите название: "))
    Amount = int(input("Введите количество: "))
    Name = Name[0].capitalize() + Name.lower()[1:]
    TotalWeight += Amount
    ApplicationList.append(InputFruit(Name, Amount))
    

#Debug Stuff=====================================

'''ApplicationList = [
        InputFruit("Апельсин", 4),
        InputFruit("Груша", 3),
        InputFruit("Арбуз", 23),
        InputFruit("Авокадо", 2),
        InputFruit("Дыня", 2)
        ]
TotalWeight = 34'''
'''user.price(1) = {"price of one amount fruit":"129 руб."}
user.price(2) = {"price of one amount  fruit": "20 руб."}
user.price(3) = {"price of one amount  fruit": "19 руб."}
user.price(4) = {"price of one amount  fruit": "90 руб."}
user.price(5) = {"price of one amount  fruit": "45 руб."}'''

TotalPrice1 = InputFruit("Апельсин", 4)*user.price(1)*2
TotalPrice2 = InputFruit("Груша", 3)*user.price(2)
TotalPrice3 = InputFruit("Арбуз", 23)*user.price(3)*2
TotalPrice4 = InputFruit("Авокадо", 2)*user.price(4)
TotalPrice5 = InputFruit("Дыня", 2)*user.price(5)*2

TotalPrice = TotalPrice1 + TotalPrice2 + TotalPrice3 + TotalPrice4 + TotalPrice5

print("TotalPrice", "Цена  заказа")







print("\nОстатки на складе:\nНаименование\t№Склада\tВес\tСтоимость за кг")
for Key, Value in FruitsData.items():
    tabulation = "\t" * (2 - (len(Key)//8))
    print(f"{Key}{tabulation}{Value[0]}\t{Value[1]}\t{Value[2]}")
    

















