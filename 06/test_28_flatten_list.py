# test_28_flatten_list.py

import pytest
from tasks.task_28_flatten_list import flatten_list

def test_flatten_list():
    assert flatten_list([[1, 2], [3, 4]]) == [1, 2, 3, 4]
    assert flatten_list([[], [1], [], [2, 3]]) == [1, 2, 3]
    assert flatten_list([]) == []
    assert flatten_list([[1]]) == [1]
    assert flatten_list([[1, 2, 3], [], [4], [5, 6]]) == [1, 2, 3, 4, 5, 6]
    assert flatten_list([[0], [0, 0]]) == [0, 0, 0]
    assert flatten_list([[10, 20], [30], [], [40, 50, 60]]) == [10, 20, 30, 40, 50, 60]
    assert flatten_list([[1], [], [], [], [2]]) == [1, 2]
    assert flatten_list([[[1]], 2, [3, [4]]]) == [1, 2, 3, 4]
    assert flatten_list([0, [0, [0]]]) == [0, 0, 0]
    assert flatten_list([10, [20, [30, [40]]]]) == [10, 20, 30, 40]
    assert flatten_list([1, [2], 3, [4, [5, [6]]]]) == [1, 2, 3, 4, 5, 6]

