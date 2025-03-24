# task_16_remove_duplicates.py

def remove_duplicates(lst: list[int]) -> list[int]:
    """
    Vrátí nový seznam bez duplicitních hodnot, zachová původní pořadí.
    """
    new_list = []
    for i in lst:
        if i not in new_list:
            new_list.append(i)
    return new_list
