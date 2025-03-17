# test_13_max_in_list.py

import pytest
from tasks.task_13_max_in_list import max_in_list

def test_max_in_list():
    assert max_in_list([1, 2, 3]) == 3
    assert max_in_list([-1, -2, -3]) == -1
    assert max_in_list([10]) == 10

