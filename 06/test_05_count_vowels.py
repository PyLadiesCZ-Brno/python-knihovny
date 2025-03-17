# test_05_count_vowels.py

import pytest
from tasks.task_05_count_vowels import count_vowels

def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("xyz") == 0
    assert count_vowels("AEIOU") == 5

