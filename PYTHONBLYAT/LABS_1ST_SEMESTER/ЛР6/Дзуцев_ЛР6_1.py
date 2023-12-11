def nayti_max_element(arr):
    max_element = arr[0]
    number = 0

    for i in range(1,len(arr)):
        if arr[i] > max_element:
            max_element = arr[i]
            number = i


    return max_element, number

massiv = [5,8,20,43,68,11,12,98,100]
max_element, number = nayti_max_element(massiv)
print(f"Максимальный элемент массива: {max_element}")
print(f"Порядковый номер массива: {number}")
