# test_26_is_palindrome_sentence.py

import pytest
from tasks.task_26_is_palindrome_sentence import is_palindrome_sentence

def test_is_palindrome_sentence():
    assert is_palindrome_sentence("A man, a plan, a canal: Panama")
    assert is_palindrome_sentence("No lemon, no melon")
    assert is_palindrome_sentence("Eva, can I see bees in a cave?")
    assert is_palindrome_sentence("Was it a car or a cat I saw?")
    assert not is_palindrome_sentence("This is not a palindrome")
    assert not is_palindrome_sentence("And this also not")

