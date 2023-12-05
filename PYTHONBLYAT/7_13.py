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

CourierNumber = 0
TotalWeight = 0
ApplicationList = []
CourierApplications = []

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

#End Debug Stuff=================================

if(TotalWeight % 9 == 0): CourierNumber = TotalWeight / 9
else: CourierNumber = TotalWeight // 9 + 1
print("============================================================")
for i in range(CourierNumber):
    #Итерация цикла - заполнение заявки для курьера

    #Переменная взятого веса курьером
    CourierApplicationWeight = 0

    #Словарь с тем, что берет текущий курьер. тип: TMap<FString, int32>
    CourierApplicationList = {}

    #Цикл, работающий пока заявка курьера не будет заполнена
    while (CourierApplicationWeight < 9):

        if(not len(ApplicationList)): break

        if(ApplicationList[0][1] + CourierApplicationWeight > 9): 
            #Если необходимый вес продукта + ассигнированный вес заявки больше 9

            #Вес, добавляемый курьеру для укомплектации
            AddWeight  = 9 - CourierApplicationWeight
            CourierApplicationWeight += AddWeight

            #Обновление списка с вычетом ассигнированого веса
            ApplicationList[0] = (ApplicationList[0][0], ApplicationList[0][1] - AddWeight)

            #Добавление товара в словарь заказа
            CourierApplicationList[ApplicationList[0][0]] = AddWeight

        elif(CourierApplicationWeight + ApplicationList[0][1] <= 9):
            #Если необходимый вес продукта + ассигнированный вес заявки <= 9

            #Добавить вес к переменной общего веса
            CourierApplicationWeight += ApplicationList[0][1]

            #Добавление товара в словарь заказа
            CourierApplicationList[ApplicationList[0][0]] = ApplicationList[0][1]

            #Удаление данных о товаре из нераспределенного списка, так как он нулевой
            ApplicationList.pop(0)
        
        #Добавление курьерской заявки в список
    CourierApplications.append(CourierApplicationList)

for i in CourierApplications:
    print(f"Заявка для {CourierApplications.index(i) + 1}-го курьера:")
    for Key, Value in i.items():
        print(f"\t {Key} - {Value}кг.")
    print("============================================================")

print("\nОстатки на складе:\nНаименование\t№Склада\tВес\tСтоимость за кг")
for Key, Value in FruitsData.items():
    tabulation = "\t" * (2 - (len(Key)//8))
    print(f"{Key}{tabulation}{Value[0]}\t{Value[1]}\t{Value[2]}")