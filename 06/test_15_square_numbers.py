# test_15_square_numbers.py

import pytest
from tasks.task_15_square_numbers import square_numbers

def test_square_numbers():
    assert square_numbers([1, 2, 3]) == [1, 4, 9]
    assert square_numbers([-1, -2]) == [1, 4]
    assert square_numbers([]) == []

