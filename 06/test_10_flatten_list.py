# test_10_flatten_list.py

import pytest
from tasks.task_10_flatten_list import flatten_list

def test_flatten_list():
    assert flatten_list([[1, 2], [3, 4]]) == [1, 2, 3, 4]
    assert flatten_list([[], [1], []]) == [1]
    assert flatten_list([]) == []

