# task_05_count_vowels.py

def count_vowels(s: str) -> int:
    """
    Vrátí počet samohlásek v řetězci.
    """
    samohlasky = "AEIOU"
    s = s.upper()
    pocet_vyskytu = 0
    for pismeno in s:
        if pismeno in samohlasky:
            pocet_vyskytu += 1
    return pocet_vyskytu
