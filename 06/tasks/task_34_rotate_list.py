# task_34_rotate_list.py

def rotate_list(lst: list[int], k: int) -> list[int]:
    """
    Posune prvky seznamu o k pozic doprava.
    """
    pos = len(lst) - k
    new_list = lst[pos:]
    new_list.extend(lst[:pos])
    return new_list
