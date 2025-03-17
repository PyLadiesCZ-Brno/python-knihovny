# test_11_count_words.py

import pytest
from tasks.task_11_count_words import count_words

def test_count_words():
    assert count_words("hello world") == 2
    assert count_words("one") == 1
    assert count_words("") == 0
    assert count_words("this is a test") == 4

