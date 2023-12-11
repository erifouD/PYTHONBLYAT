def find_max_el(matrix):
    max_el=matrix[0]
    max_index=0

    for i in range (len(matrix)):
        if matrix[i] > max_el:
            max_el= matrix[i]
            max_index=i
    return max_index

matrix_A=[1,2,3,4,10,5]
matrix_B=[6,7,8,9,3,2]
    
max_el_A_index=find_max_el(matrix_A)
max_el_B_index=find_max_el(matrix_B)

matrix_A[max_el_A_index],matrix_B[max_el_B_index]=matrix_B[max_el_B_index],matrix_A[max_el_A_index]



matrix_B[max_el_B_index]

print('Матрица А: ')
print(matrix_A)

print('Матрица В: ')
print(matrix_B)
    



