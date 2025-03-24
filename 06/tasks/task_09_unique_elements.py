# task_09_unique_elements.py

def unique_elements(lst: list[int]) -> list[int]:
    """
    Vrátí seznam bez duplicitních prvků, zachová původní pořadí.
    """
    new = []
    for element in lst:
        if element not in new:
            new.append(element)

    return new
