# task_28_flatten_list.py

def flatten_list(nested: list[list[int]]) -> list[int]:
    """
    Převede dvourozměrný seznam na jednorozměrný.
    """

    return [digit for sublist in nested for digit in sublist]
