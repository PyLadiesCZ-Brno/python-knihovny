# test_03_max_of_three.py

import pytest
from tasks.task_03_max_of_three import max_of_three

def test_max_of_three():
    assert max_of_three(1, 2, 3) == 3
    assert max_of_three(9, 3, 6) == 9
    assert max_of_three(-1, -5, -3) == -1

