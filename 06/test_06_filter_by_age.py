# test_06_filter_by_age.py

import pytest
from tasks.task_06_filter_by_age import filter_by_age

def test_filter_by_age():
    # Test pro seznam osob, kde některé mají věk nad 18
    people = [
        {"name": "Alice", "age": 20},
        {"name": "Bob", "age": 17},
        {"name": "Charlie", "age": 22},
        {"name": "David", "age": 18}
    ]
    result = filter_by_age(people)
    assert result == [
        {"name": "Alice", "age": 20},
        {"name": "Charlie", "age": 22}
    ]

    # Test pro prázdný seznam
    assert filter_by_age([]) == []

    # Test pro všechny osoby mladší než 18
    people = [
        {"name": "Eve", "age": 17},
        {"name": "Frank", "age": 16}
    ]
    assert filter_by_age(people) == []

    # Test pro všechny osoby starší než 18
    people = [
        {"name": "Grace", "age": 25},
        {"name": "Hank", "age": 30}
    ]
    assert filter_by_age(people) == people

