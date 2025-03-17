# test_35_rotate_matrix.py

import pytest
from tasks.task_35_rotate_matrix import rotate_matrix

def test_rotate_matrix():
    assert rotate_matrix([[1]]) == [[1]]

    assert rotate_matrix([
        [1, 2],
        [3, 4]
    ]) == [
        [3, 1],
        [4, 2]
    ]

    assert rotate_matrix([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]) == [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ]

    assert rotate_matrix([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10,11,12],
        [13,14,15,16]
    ]) == [
        [13, 9, 5, 1],
        [14,10, 6, 2],
        [15,11, 7, 3],
        [16,12, 8, 4]
    ]

    assert rotate_matrix([
        [0, 1],
        [2, 3]
    ]) == [
        [2, 0],
        [3, 1]
    ]


