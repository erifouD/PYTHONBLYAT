from math import sqrt, acos, degrees

#Функиця проверки числа, является ли оно числом Армстронга
def IsArmstrong (num):
    result = 0
    a = str(num)
    for i in a:
        result += int(i) ** len(a)
    if result == num: return True
    else: return False

#Функция получения угла между осью абсцисс и лучом
def GetAngle(A = []):
    Len1 = A[0] #X side
    Len2 = A[1] #Y side
    Len3 = sqrt(Len1 ** 2 + Len2 ** 2)
    Angle = Len1 / Len3
    return degrees(acos(Angle))

#функция создания вектора с координатами в двухмерном пространстве
def MakeVector2D(Name):
    Vec = []
    for i in range(2):
        Vec.append(int(input(f"Введите {Name}{i + 1}: ")))
    return Vec
        
#Функция нахождения минимального угла
def Coordinates():
    X = MakeVector2D("X")
    Y = MakeVector2D("Y")
    Z = MakeVector2D("Z")
    return min(GetAngle(X), GetAngle(Y), GetAngle(Z))


def main():
    a = int(input("Введите число: "))
    for i in range(1, a + 1):
        if IsArmstrong(i):
            print(i)

    print('Минимальный угол равен %.2f градусов' % Coordinates())
main()
