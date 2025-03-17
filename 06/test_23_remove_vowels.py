# test_23_remove_vowels.py

import pytest
from tasks.task_23_remove_vowels import remove_vowels

def test_remove_vowels():
    assert remove_vowels("hello") == "hll"
    assert remove_vowels("AEIOU") == ""
    assert remove_vowels("python") == "pythn"

