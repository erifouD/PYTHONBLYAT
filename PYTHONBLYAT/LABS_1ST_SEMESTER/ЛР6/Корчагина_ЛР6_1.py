my_list=[2,-1,9,8,-6,-8,1,9,3,4]
odd_numbers=[num for num in my_list if num %2 != 0]
if odd_numbers:
    min_odd=min(odd_numbers)
    print("Наименьший нечетный элемент:", min_odd)
else:
    print("В списке нет нечетных элементов.")
