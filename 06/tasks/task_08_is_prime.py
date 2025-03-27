# task_08_is_prime.py

def is_prime(n: int) -> bool:
    """
    Vrátí True, pokud je číslo prvočíslo.
    """
    if n < 2:
        return False
    elif n == 2:
        return True
    for i in range (2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        return True

print(is_prime(15))
print(is_prime(2))
