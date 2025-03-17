# test_01_sum_two_numbers.py

import pytest
from tasks.task_01_sum_two_numbers import sum_two_numbers

def test_sum_two_numbers():
    assert sum_two_numbers(1, 2) == 3
    assert sum_two_numbers(-1, 1) == 0
    assert sum_two_numbers(0, 0) == 0

