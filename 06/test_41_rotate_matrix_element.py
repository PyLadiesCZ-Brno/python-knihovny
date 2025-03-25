# test_41_rotate_matrix_element.py

import pytest
from tasks.task_41_rotate_matrix_element import rotate_matrix

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
        [4, 1, 2],
        [7, 5, 3],
        [8, 9, 6]
    ]

    assert rotate_matrix([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10,11,12],
        [13,14,15,16]
    ]) == [
        [5, 1, 2, 3],
        [9, 10, 6, 4],
        [13, 11, 7, 8],
        [14, 15, 16, 12]
    ]

    assert rotate_matrix([
        [0, 1],
        [2, 3]
    ]) == [
        [2, 0],
        [3, 1]
    ]
