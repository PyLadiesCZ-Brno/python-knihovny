# test_31_reverse_words.py

import pytest
from tasks.task_31_reverse_words import reverse_words

def test_reverse_words():
    assert reverse_words("hello world") == "world hello"
    assert reverse_words("one two three") == "three two one"
    assert reverse_words("single") == "single"
    assert reverse_words("a b c d") == "d c b a"
    assert reverse_words("   spaced   words  test ") == "test words spaced"
    assert reverse_words("") == ""

