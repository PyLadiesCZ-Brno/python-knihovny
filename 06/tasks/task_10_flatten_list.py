# task_10_flatten_list.py

def flatten_list(nested: list[list[int]]) -> list[int]:
    """
    Zploští dvourozměrný seznam do jednoho seznamu.
    """
    return [item for sublist in nested for item in sublist]
