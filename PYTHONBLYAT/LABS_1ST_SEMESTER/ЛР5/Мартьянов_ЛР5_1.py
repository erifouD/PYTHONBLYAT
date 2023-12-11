def divs_amount(X):
    counter = 0
    for i in range(1, X + 1):
        if X % i == 0:
            counter += 1
    return counter

def max_divs(M, N):
    max_divss = 0
    number = 0
    for i in range(M, N + 1):
        if divs_amount(i) >= max_divss:
            max_divss = divs_amount(i)
            number = i
    print("Число ", number, " имеет максимальное количество делителей - ", max_divss)
    
M = int(input("Начало интервала: "))
N = int(input("Конец интервала: "))
max_divs(M, N)
