# task_38_matrix_transpose.py

def matrix_transpose(matrix: list[list[int]]) -> list[list[int]]:
    """
    Vrátí transponovanou matici.
    """
    if matrix == []:
        return []
    else:
        return [[radek[j] for radek in matrix] for j in range(len(matrix[0]))]
