# test_34_rotate_list.py

import pytest
from tasks.task_34_rotate_list import rotate_list

def test_rotate_list():
    assert rotate_list([1,2,3,4,5], 2) == [4,5,1,2,3]
    assert rotate_list([1,2,3], 1) == [3,1,2]
    assert rotate_list([1,2,3], 0) == [1,2,3]
    assert rotate_list([1,2,3], 3) == [1,2,3]
    assert rotate_list([], 2) == []
    assert rotate_list([1], 10) == [1]

