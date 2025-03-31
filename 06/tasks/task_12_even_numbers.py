# task_12_even_numbers.py

def even_numbers(lst: list[int]) -> list[int]:
    """
    Vrátí seznam pouze sudých čísel.
    """
    suda_cisla = []
    for cislo in lst:
        if cislo % 2 == 0:
            suda_cisla.append(cislo)
    return suda_cisla
