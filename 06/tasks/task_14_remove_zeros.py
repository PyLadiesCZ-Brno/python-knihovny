# task_14_remove_zeros.py
def remove_zeros(lst: list[int]) -> list[int]:
    """
    Vrátí seznam bez nulových hodnot.
    """
    for _ in range(lst.count(0)):
        lst.remove(0)
    return lst
