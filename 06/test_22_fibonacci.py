# test_22_fibonacci.py

import pytest
from tasks.task_22_fibonacci import fibonacci

def test_fibonacci():
    assert fibonacci(0) == []
    assert fibonacci(1) == [0]
    assert fibonacci(5) == [0, 1, 1, 2, 3]

