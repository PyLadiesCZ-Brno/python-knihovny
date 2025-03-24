# task_19_is_palindrome.py

def is_palindrome(s: str) -> bool:
    """
    Vrátí True, pokud je řetězec palindrom.
    """

    return s == s[::-1]
