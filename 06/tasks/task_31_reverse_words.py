# task_31_reverse_words.py

def reverse_words(s: str) -> str:
    """
    Otočí pořadí slov ve větě.
    """
    words = s.split()
    words.reverse()
    return " ".join(words)
