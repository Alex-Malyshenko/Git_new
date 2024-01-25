# Напишите функцию для транспонирования матрицы transposed_matrix, принимает в аргументы matrix,
# и возвращает транспонированную матрицу.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(matrix)

# def transpose(matrix):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i]):
#             if i > j:
#                 matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#     return matrix
#
# print(transpose(matrix))

def transpose(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
        temp_matrix = []
        for j in range(len(matrix)):
             temp_matrix.append(matrix[j][i])
        new_matrix.append(temp_matrix)

    return new_matrix

print(transpose(matrix))
