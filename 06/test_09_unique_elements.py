# test_09_unique_elements.py

import pytest
from tasks.task_09_unique_elements import unique_elements

def test_unique_elements():
    assert unique_elements([1, 2, 2, 3]) == [1, 2, 3]
    assert unique_elements([]) == []
    assert unique_elements([4, 4, 4, 4]) == [4]

