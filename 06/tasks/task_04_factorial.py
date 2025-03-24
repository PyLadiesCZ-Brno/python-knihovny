# task_04_factorial.py

def factorial(n: int) -> int:
    """
    Vrátí faktoriál čísla n.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


