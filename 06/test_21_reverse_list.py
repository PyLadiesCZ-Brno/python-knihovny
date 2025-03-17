# test_21_reverse_list.py

import pytest
from tasks.task_21_reverse_list import reverse_list

def test_reverse_list():
    assert reverse_list([1, 2, 3]) == [3, 2, 1]
    assert reverse_list([]) == []
    assert reverse_list([42]) == [42]

