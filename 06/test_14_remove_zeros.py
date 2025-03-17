# test_14_remove_zeros.py

import pytest
from tasks.task_14_remove_zeros import remove_zeros

def test_remove_zeros():
    assert remove_zeros([0, 1, 0, 2]) == [1, 2]
    assert remove_zeros([0, 0, 0]) == []
    assert remove_zeros([5, 6, 7]) == [5, 6, 7]

