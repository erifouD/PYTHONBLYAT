from math import sqrt

###Функция создания вектора как массива
def CreateVector(var):
    A =[]
    for i in range (3):
        A.append(int(input(f"Введите точку {var}{i + 1}: ")))
    A.append(var) #нужно для сохранения названия вектора
    return A
##
###Функция нахождения расстояния между двумя точками. Рассчитывается по формуле
def Distance(A = [], B = []):
    Value =  sqrt((B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2 + (B[2] - A[2]) ** 2)
    return [Value, A[3], B[3]] #Возвращение расстояния и имен векторов, между которыми это расстояние

#Функция для нахождения делителей
def Divs(X):
    for i in range(1, X + 1):
        if X % i == 0:
            print(i, end = " ")



X = CreateVector("X")
Y = CreateVector("Y")
Z = CreateVector("Z")
T = CreateVector("T")
           

#запись расстояний в массив
D = []
D.append(Distance(X, Y))
D.append(Distance(X, Z))
D.append(Distance(X, T))
D.append(Distance(Y, Z))
D.append(Distance(Y, T))
D.append(Distance(Z, T))
ANSR = min(D)
print(f"Минимальное расстояние между векторами {ANSR[1]} и {ANSR[2]} и составляет {ANSR[0]}")
#=======================================
G = int(input("Введите число: "))
Divs(G)
