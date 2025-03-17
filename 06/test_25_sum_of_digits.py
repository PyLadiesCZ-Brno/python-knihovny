# test_25_sum_of_digits.py

import pytest
from tasks.task_25_sum_of_digits import sum_of_digits

def test_sum_of_digits():
    assert sum_of_digits(123) == 6
    assert sum_of_digits(0) == 0
    assert sum_of_digits(-456) == 15

