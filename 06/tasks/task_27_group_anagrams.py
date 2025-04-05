# task_27_group_anagrams.py

def group_anagrams(words: list[str]) -> list[list[str]]:
    """
    Skupiny anagramů v seznamu slov. Seznamy musí být seřazené. Anagramy v seznamech také seřazené.
    """
    words.sort()
    anagrams = []
    sorted_anagrams = []
    for word in words:
        if sorted(word) in sorted_anagrams:
            anagrams[sorted_anagrams.index(sorted(word))].append(word)
        else:
            sorted_anagrams.append(sorted(word))
            anagrams.append([word])
    return anagrams
