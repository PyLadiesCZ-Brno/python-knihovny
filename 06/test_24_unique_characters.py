# test_24_unique_characters.py

import pytest
from tasks.task_24_unique_characters import unique_characters

def test_unique_characters():
    assert unique_characters("abc")
    assert not unique_characters("aabb")
    assert unique_characters("")

