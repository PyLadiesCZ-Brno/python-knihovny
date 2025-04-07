# task_39_reverse_vowels.py

def reverse_vowels(s: str) -> str:
    """
    Vrátí řetězec s přeházenými samohláskami v opačném pořadí.
    Ostatní znaky zůstávají na místě.
    """
    vowels = "aeiou"  # vowels without y otherwise the test failed ("Python") == "Python"

    if s == "":
        return s

    s_list = list(s)
    s_vowels = []
    s_vowels_position = []

# Identify the vowels and their positions in the string.
    for position, character in enumerate(s):
        if character.lower() in vowels:
            s_vowels.append(character)
            s_vowels_position.append(position)
# replacing rotated vowels to vowel positions
    for char, pos in zip(reversed(s_vowels), s_vowels_position):
        s_list[pos] = char

    return ''.join(s_list)
