# task_19_is_palindrome.py

def is_palindrome(s: str) -> bool:
    """
    Vrátí True, pokud je řetězec palindrom.
    """
# checks the front and back halves of the word
    return s[:(len(s) // 2)] == s[:-((len(s) // 2) + 1):-1]
