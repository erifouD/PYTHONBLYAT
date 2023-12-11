def input_data():
    fn=input('Enter your firstname: ')#имя
    ln=input('Enter your lastname: ')#фамилия
    age=input('Enter your age: ')
    return {'firstname': fn,'lastname': ln, 'age': age}
def add_user(ud):# ud-данные ul-список с данными
    ul.append(ud)
ul=[]
for i in range(5):
    if i==3:
        break
    ud=input_data()
    add_user(ud)
print("список:",ul)
    
