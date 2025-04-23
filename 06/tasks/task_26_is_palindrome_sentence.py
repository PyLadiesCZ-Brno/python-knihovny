# task_26_is_palindrome_sentence.py

def is_palindrome_sentence(s: str) -> bool:
    """
    Vrátí True, pokud je věta palindrom (ignoruje mezery, interpunkci a velikost písmen).
    """
# creates a list consisting only of lowercase letters of the original string
    s_list = [char.lower() for char in s if char.isalpha()]

    return s_list == s_list[::-1]
