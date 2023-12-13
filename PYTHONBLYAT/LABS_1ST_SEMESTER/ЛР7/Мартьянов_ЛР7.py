from tkinter import FALSE


fruits_data = {
    "Абрикос": [1, 30, 120],
    "Авокадо": [1, 19, 90],
    "Алыча": [1, 32, 67],
    "Апельсин": [1, 67, 129],
    "Арбуз": [1, 129, 19],
    "Гранат": [2, 36, 56],
    "Грейпфрут": [2, 23, 78],
    "Груша": [2, 57, 20],
    "Дыня": [2, 48, 45],
    "Инжир": [2, 12, 54],
    "Кешью": [2, 31, 73]}

#Объявление списка заявки. Нулевой индекс будет общим весом и ценой, первый - список фруктов в заявке. Их название, вес и цена
application = [{"Weight": 0, "Price" : 0}, {}]

def input_fruit(i):
    
    print(f"Фрукт №{i + 1}") #Указание номера фрукта при вводе
    fruit_name = str(input("Введите название фрукта с большой буквы: "))
    fruit_amount = int(input("Введите количество фрукта: "))
    print() #Делаю дополнительный отступ, чтобы визуально разделить вводимые данные
    return (fruit_name, fruit_amount) #Возвращение кортежа 


#1. Апельсины, 4 кг
#2. Груша, 3 кг
#3. Арбуз, 23 кг
#4. Авокадо, 2 кг
#5. Дыня, 9 кг

for i in range(5):
    # Создание новой заявки
    #new_application[0] - название текущего фрукта, new_application[1] - его вес
    new_application = input_fruit(i)

    #Множитель цены. По умолчанию два.
    price_multiply = 2

    #Если текущий фрукт не облагается двойным тарифом, меняем множитель на 1
    if(new_application[0] == "Авокадо" or new_application[0] == "Груша"): price_multiply = 1 

    #Вычитаем со склада запрошенный вес текущего фрукта
    fruits_data[new_application[0]][1] -= new_application[1]

    #Добавляем общий вес
    application[0]["Weight"] += new_application[1]
    #Добавляем общую цену
    application[0]["Price"] += new_application[1] * fruits_data[new_application[0]][2] * price_multiply

    #Добавляем в список заявки введенный фрукт в виде словарной пары {string : int[2]} - {Название: [Вес, Цена за указанный вес]}
    application[1][new_application[0]] = [new_application[1], new_application[1] * fruits_data[new_application[0]][2] * price_multiply]


#Вывод данных заявки: 
print(f"Данные заявки:\nОбщий вес заявки - {application[0]['Weight']}кг\nОбщая цена заявки - {application[0]['Price']}р.")
#Итерируемся по словарю фруктов в заявке
for key, value in application[1].items():
    print(f"{key} - {value[0]}кг, цена - {value[1]}р.")

#Вывод остатков на складе:
print("\nОстатки на складе: ")
for key, value in fruits_data.items():
    #Вывод данных о фрукте
    print(f"{key} - {value[1]}кг")
