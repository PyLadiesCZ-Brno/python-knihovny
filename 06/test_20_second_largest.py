# test_20_second_largest.py

import pytest
from tasks.task_20_second_largest import second_largest

def test_second_largest():
    assert second_largest([1, 2, 3]) == 2
    assert second_largest([10, 20, 30, 30]) == 20
    assert second_largest([5, 1]) == 1

