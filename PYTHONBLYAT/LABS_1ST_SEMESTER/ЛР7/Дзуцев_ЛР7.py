def input_data():
    firstname = str(input("Введите имя: "))
    lastname = str(input("Введите фамилию: "))
    age = int(input("Введите возраст: "))
    user = dict(firstname = firstname, lastname = lastname, age = age)
    return user

def add_user(user):
    users.append(user)

users = []

for i in range(5):
    add_user(input_data())
print(users)
