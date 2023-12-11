from math import sqrt

#Функция создания вектора как массива
def CreateVector(var):
    A =[]
    for i in range (2):
        A.append(int(input(f"Введите точку {var}{i + 1}: ")))
    A.append(var) #нужно для сохранения названия вектора
    return A

#Функция нахождения расстояния между двумя точками. Рассчитывается по формуле
def Distance(A = [], B = []):
    Value =  sqrt((B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2)
    return [Value, A[2], B[2]] #Возвращение расстояния и имен векторов, между которыми это расстояние





X = CreateVector("X")
Y = CreateVector("Y")
Z = CreateVector("Z")
P = CreateVector("P")


#запись расстояний в массив
D = []
D.append(Distance(X, Y))
D.append(Distance(X, Z))
D.append(Distance(X, P))
D.append(Distance(Y, Z))
D.append(Distance(Y, P))
D.append(Distance(Z, P))
ANSR = max(D)
print(f"Максимальное  расстояние между векторами {ANSR[1]} и {ANSR[2]} и составляет {ANSR[0]}")
#=======================================
