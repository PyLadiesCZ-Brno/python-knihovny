# task_25_sum_of_digits.py

def sum_of_digits(n: int) -> int:
    """
    Vrátí součet číslic čísla.
    """
    soucet = 0
    for cislice in str(abs(n)):
        soucet += int(cislice)
    return soucet
