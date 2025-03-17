# test_12_even_numbers.py

import pytest
from tasks.task_12_even_numbers import even_numbers

def test_even_numbers():
    assert even_numbers([1, 2, 3, 4, 5]) == [2, 4]
    assert even_numbers([1, 3, 5]) == []
    assert even_numbers([2, 4, 6]) == [2, 4, 6]

