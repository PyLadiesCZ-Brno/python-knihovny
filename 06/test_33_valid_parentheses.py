# test_33_valid_parentheses.py

import pytest
from tasks.task_33_valid_parentheses import valid_parentheses

def test_valid_parentheses():
    assert valid_parentheses("()")
    assert valid_parentheses("()[]{}")
    assert not valid_parentheses("(]")
    assert not valid_parentheses("([)]")
    assert valid_parentheses("{[]}")
    assert not valid_parentheses("(")
    assert not valid_parentheses("(()")
    assert not valid_parentheses(")(")
    assert valid_parentheses("((()))")
    assert valid_parentheses("{[()]}[]({})")
    assert not valid_parentheses("{[}]")
    assert valid_parentheses("")

