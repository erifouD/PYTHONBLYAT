#массив списка пользователей
users_list = []

#функция ввода данных пользователя
def input_data():
    #ввод имени (строковый формат)
    firstname = str(input("Введите имя: "))
    #ввод фамилии (строковый формат)
    lastname = str(input("Введите фамилию: "))
    #ввод возраста (целочисленный формат)
    age = int(input("Введите возраст: "))

   #возвращение словаря с данными пользователя
    return dict(firstname = firstname, lastname = lastname, age = age)

def add_user(user):
    #добавление в массив нового пользователя
    users_list.append(user)

#Начало программы

#заполнение списка с пользователями
for i in range (6):
    add_user(input_data())

#список людей, чьи имена/фамилии совпадают
no_matches = True
#поиск людей с одинаковыми именами/фамилиями
for i in range(6):
    #вложненный цикл. такая конструкция будет сравнивать i-того пользователя с j-тым
    for j in range(i + 1, 6):
        #если имя или фамилия i-того и j-того пользователя совпадают, то он выводит их данные в консоль
        if users_list[i]["firstname"] == users_list[j]["firstname"] or users_list[i]["lastname"] == users_list[j]["lastname"]:
            #выключение флага отсутствия совпадений, так как совпадения найдены
            no_matches = False
            #вывод данных i-того пользователя
            print(f'{users_list[i]["firstname"]} {users_list[i]["lastname"]} - {users_list[i]["age"]} лет')
            #вывод данных j-того пользователя
            print(f'{users_list[j]["firstname"]} {users_list[j]["lastname"]} - {users_list[j]["age"]} лет\n')

#Если no_matches останется true, то выведется сообщение "Совпадений не найдено"
if(no_matches):
    print("Совпадений не найдено.")