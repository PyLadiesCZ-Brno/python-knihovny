# task_29_longest_common_prefix.py

def longest_common_prefix(strings: list[str]) -> str:
    """
    Vrátí nejdelší společný prefix v seznamu řetězců.
    """

    if not strings:
        return ""

    shortest_word = min(strings, key=len)
    number_of_iteration = len(shortest_word)
    prefix = ""

    for i in range(number_of_iteration):
        for word in strings:
            if word[i] != shortest_word[i]:
                return prefix

        prefix += shortest_word[i]

    return prefix
