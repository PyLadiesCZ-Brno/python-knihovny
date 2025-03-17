# test_08_is_prime.py

import pytest
from tasks.task_08_is_prime import is_prime

def test_is_prime():
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(4)
    assert is_prime(13)

