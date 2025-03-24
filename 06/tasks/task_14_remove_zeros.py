# task_14_remove_zeros.py

def remove_zeros(lst: list[int]) -> list[int]:
    """
    Vrátí seznam bez nulových hodnot.
    """

    no_zero_list = lst.copy()

    while True:
        if 0 in no_zero_list:
            no_zero_list.remove(0)
        else:
            break
    return no_zero_list
