# test_17_capitalize_words.py

import pytest
from tasks.task_17_capitalize_words import capitalize_words

def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"
    assert capitalize_words("") == ""
    assert capitalize_words("python programming") == "Python Programming"

