##def f(n):
##    s = 0
##    while n>0:
##        s += n%10
##        n = n//10
##    return s
##c =int(input("Введите число: "))
##k = 0
##while c > 0:
##    c -= f(c)
##    k += 1
##    
##print("Через " + str(k) + " действий")

for i in range(3):
    m = []
    s=1
    q=0
    i=1
    x = int(input("Введите кол-во элементов в списке: "))
    for i in range(x):
        m.append(int(input("Введите целое число для списка: ")))
    for i in range(x):
        s *= m[i]
        q += m[i]
    print("Произведение элементов списка равна: ", s)
    print("Среднее арифметическое списка равно",(q/x))













