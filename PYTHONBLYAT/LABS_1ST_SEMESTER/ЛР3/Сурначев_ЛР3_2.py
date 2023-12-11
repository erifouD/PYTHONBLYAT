import math
x = int(input('Введите первое значение угла '))
y = int(input('Введите второе значение угла '))
z = int(input('Введите третье значение угла '))
k = int(input('Введите четвертое значение угла '))
if x < 0 or y < 0 or z < 0 or k < 0:
    print('Угол не может быть отрицательным!')
elif x <= y and x <= z and x <= k:
    print('Косинус минимаьного из этих углов равен ',math.cos(x))
elif y <= x and y <= z and y <= k:
    print('Косинус минимаьного из этих углов равен ',math.cos(y))
elif z <= y and z <= x and z <= k:
    print('Косинус минимаьного из этих углов равен ',math.cos(z))
elif k <= y and k <= x and k <= z:
    print('Косинус минимаьного из этих углов равен ',math.cos(k))


 



