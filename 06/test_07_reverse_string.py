# test_07_reverse_string.py

import pytest
from tasks.task_07_reverse_string import reverse_string

def test_reverse_string():
    assert reverse_string("abc") == "cba"
    assert reverse_string("") == ""
    assert reverse_string("racecar") == "racecar"

