# task_20_second_largest.py

def second_largest(lst: list[int]) -> int:
    """
    Vrátí druhé největší číslo v seznamu.
    """
    lst = sorted(lst, reverse=True)
    for finder in lst:
        if finder < lst[0]:
            numero = finder
            break

    return numero
