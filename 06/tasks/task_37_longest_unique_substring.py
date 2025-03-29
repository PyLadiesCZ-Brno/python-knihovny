# task_37_longest_unique_substring.py

def longest_unique_substring(s: str) -> int:
    """
    Vrátí délku nejdelší podposloupnosti bez opakujících se znaků.
    """
    substr = ''
    longest_substring = 0
    for (pos, letter) in enumerate(s):
        if letter in substr:
            len_substr = len(substr)
            pos_duplicate = s.index(letter, pos - len_substr)
            substr = s[pos_duplicate + 1: pos + 1]
            if longest_substring < len_substr:
                longest_substring = len_substr
        else:
            substr += letter
    if longest_substring < len(substr):
        longest_substring = len(substr)

    return longest_substring
