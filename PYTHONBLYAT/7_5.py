UsersList = []

def input_data():
    UserData = {
        "name" : str(input("Введите имя: ")),
        "surname" : str(input("Введите фамилию: ")),
        "age" : int(input("Введите возраст: ")),
        }
    return UserData

def add_user(UserData):
    UsersList.append(UserData)


for i in range (6):
    add_user(input_data())

MaxAge = {"name" : "none", "surname": "none", "age" : 0}
for i in UsersList:
    if i.get("age") > MaxAge.get("age"):
        MaxAge = i

print("Пользователь с наибольшим возрастом:\n")
for key, value in MaxAge.items():
    print(f"{key}: {value}")