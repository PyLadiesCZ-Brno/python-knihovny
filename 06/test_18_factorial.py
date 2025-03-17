# test_18_factorial.py

import pytest
from tasks.task_18_factorial import factorial

def test_factorial():
    assert factorial(0) == 1
    assert factorial(3) == 6
    assert factorial(5) == 120

