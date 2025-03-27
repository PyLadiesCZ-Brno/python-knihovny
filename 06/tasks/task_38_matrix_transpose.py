# task_38_matrix_transpose.py

def matrix_transpose(matrix: list[list[int]]) -> list[list[int]]:
    """
    Vrátí transponovanou matici.
    """
    return [list(i) for i in list(zip(*matrix))]
