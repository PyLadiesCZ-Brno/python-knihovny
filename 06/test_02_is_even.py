# test_02_is_even.py

import pytest
from tasks.task_02_is_even import is_even

def test_is_even():
    assert is_even(2)
    assert not is_even(3)
    assert is_even(0)

