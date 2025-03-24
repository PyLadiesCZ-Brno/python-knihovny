# task_18_factorial.py

def factorial(n: int) -> int:
    """
    Vrátí faktoriál čísla n (n!).
    """
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact
