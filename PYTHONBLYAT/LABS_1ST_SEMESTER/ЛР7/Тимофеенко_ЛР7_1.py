def get_user_data():
    name = input("Введите ваше имя:")
    surname = input("Введите вашу фамилию:")
    age = int(input("Введите ваш возраст:"))
    user_data = {
        "имя":name,
        "фамилия":surname,
        "возраст":age
        }
    return user_data
print (get_user_data()) 
