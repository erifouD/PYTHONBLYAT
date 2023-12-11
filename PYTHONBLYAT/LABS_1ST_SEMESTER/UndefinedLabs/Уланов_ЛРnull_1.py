def reverse_words(string):
    words=string.split()
    words.reverse()
    return" ".join(words)
input_string=input("Введите строку:")
reversed_string=reverse_words(input_string)
print("Строка с обратным порядком:",reversed_string)

