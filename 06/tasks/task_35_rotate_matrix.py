# task_35_rotate_matrix.py

def rotate_matrix(matrix: list[list[int]]) -> list[list[int]]:
    """
    Otočí čtvercovou matici o 90 stupňů ve směru hodinových ručiček.
    """
    return [list(i) for i in list(zip(*matrix[::-1]))]
