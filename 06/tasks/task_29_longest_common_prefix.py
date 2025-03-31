# task_29_longest_common_prefix.py

def longest_common_prefix(strings: list[str]) -> str:
    """
    Vrátí nejdelší společný prefix v seznamu řetězců.
    """

    if not strings:  # in case when list of strings is empty
        return ""

# set first word in "strings" as prefix
    prefix = strings[0]
    for word in strings[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix
