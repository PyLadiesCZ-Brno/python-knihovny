# test_30_remove_duplicates.py

import pytest
from tasks.task_30_remove_duplicates import remove_duplicates

def test_remove_duplicates():
    assert remove_duplicates([1,2,2,3,1]) == [1,2,3]
    assert remove_duplicates([]) == []
    assert remove_duplicates([1,1,1,1]) == [1]
    assert remove_duplicates([3,2,1,2,3]) == [3,2,1]

