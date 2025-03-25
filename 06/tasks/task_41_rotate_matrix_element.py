# task_41_rotate_matrix_element.py
# alternativa k špatně pochpenému úkolu:
# task_35_rotate_matrix.py

from copy import deepcopy


def rotate_matrix(matrix: list[list[int]]) -> list[list[int]]:
    """
    Rotates square matrix clockwise by one element.

    Args:
    matrix (list[list[int]]): Input square matrix.

    Returns:
    list[list[int]]: Rotated matrix.

    Example:
    1 2 3       4 1 2
    4 5 6  -->  7 5 3
    7 8 9       8 9 6
    """

    rotated_matrix = deepcopy(matrix)
    matrix_size = len(matrix)

    if matrix_size <= 1:
        return rotated_matrix

    num_layers = matrix_size // 2

    for layer in range(num_layers):

        layer_size = matrix_size - layer * 2

        north_row = matrix[0 + layer][layer:-1 - layer]
        east_col = [matrix[i + layer][-1 - layer]
                    for i in range(layer_size)][:-1]
        south_row = matrix[-1 - layer][-1 - layer:layer:-1]
        west_col = [matrix[i + layer][layer]
                    for i in range(layer_size)][::-1][:-1]

        border_layer = north_row + east_col + south_row + west_col
        rotated_border = [border_layer[-1]] + border_layer[:-1]
        north_end = layer_size
        east_end = north_end + layer_size - 1
        south_end = east_end + layer_size - 1

        # north_row
        for i in range(matrix_size - layer * 2):
            rotated_matrix[layer][i + layer] = rotated_border[i]
        # east_col
        for i in range(1, matrix_size - layer * 2):

            rotated_matrix[i + layer][-1 -
                                      layer] = rotated_border[north_end + i - 1]
        # south_row
        for i in range(1, matrix_size - layer * 2):
            rotated_matrix[-1 - layer][matrix_size - layer - i -
                                       1] = rotated_border[east_end + i - 1]
        # west_col
        for i in range(1, matrix_size - layer * 2 - 1):
            rotated_matrix[matrix_size -
                           layer -
                           i -
                           1][layer] = rotated_border[south_end + i - 1]

    return rotated_matrix


A = [[1, 2, 3, 4, 5],
     [6, 7, 8, 9, 10],
     [11, 12, 13, 14, 15],
     [16, 17, 18, 19, 20],
     [21, 22, 23, 24, 25]]

B = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

C = [[1]]

matrix_rotated = rotate_matrix(B)

# pretty matrix print
for row in matrix_rotated:
    print(row)
