# test_19_is_palindrome.py

import pytest
from tasks.task_19_is_palindrome import is_palindrome

def test_is_palindrome():
    assert is_palindrome("radar")
    assert not is_palindrome("hello")
    assert is_palindrome("a")
    assert is_palindrome("")

