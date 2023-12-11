
massiv = [1,13,12,15,167,164,125,65,64,89,90,91]
new_massiv = [x for x in massiv if x % 2 != 0]
if len(new_massiv) == 0:
    print("В первоначальном массиве нету нечетных чисел")
else:
    new_massiv.sort(reverse = True)
    print("Новый массив из нечетных чисел в порядке убывания",new_massiv)
