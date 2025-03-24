# task_18_factorial.py

def factorial(n: int) -> int:
    """
    Vrátí faktoriál čísla n (n!).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
