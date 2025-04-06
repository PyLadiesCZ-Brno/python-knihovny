# task_33_valid_parentheses.py

def erase_brackets(s, par):
    if par not in s:
        return s
    pos = s.index(par)
    s = s[:pos] + s[pos + 2:]
    return s


def valid_parentheses(s: str) -> bool:
    """
    Zjistí, zda má řetězec validní závorky.
    """
    while '()' in s or '[]' in s or '{}' in s:
        for par in '()', '[]', '{}':
            s = erase_brackets(s, par)
    return s == ''
