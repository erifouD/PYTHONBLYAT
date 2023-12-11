'''
def data():

    name = input('введите своё имя:')
    sname = input('введите свою фамилию:')
    age = int(input('введите свой возраст:'))
    return name,sname,age 




print(*data())
'''
def users():
    
    name = input('введите своё имя:')
    sname = input('введите свою фамилию:')
    age = int(input('введите свой возраст:'))
    user = dict(имя=name,фамилия=sname,возраст=age)

    return user

arr = []

for i in range(3):
    arr.append(users())

print(arr)


