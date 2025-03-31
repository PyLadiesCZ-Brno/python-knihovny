# task_15_square_numbers.py

def square_numbers(lst: list[int]) -> list[int]:
    """
    Vrátí seznam čtverců čísel ze vstupního seznamu.
    """
    lst_squared = []
    for number in lst:
        lst_squared.append(number ** 2)
    return lst_squared
