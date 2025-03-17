# test_27_group_anagrams.py

import pytest
from tasks.task_27_group_anagrams import group_anagrams

def test_group_anagrams():
    assert group_anagrams(["bat", "cat", "tab", "act"]) == [["act", "cat"], ["bat", "tab"]]
    assert group_anagrams(["google", "silent", "gogole", "listen", "enlist"]) == [["enlist", "listen", "silent"], ["gogole", "google"]]
    assert group_anagrams([]) == []
    assert group_anagrams(["abc"]) == [["abc"]]
    assert group_anagrams(["cab", "xyz", "abc", "zyx", "bca"]) == [["abc", "bca", "cab"], ["xyz", "zyx"]]
    assert group_anagrams(["rat", "tar", "art", "star", "tars", "cheese"]) == [["art", "rat", "tar"], ["cheese"], ["star", "tars"]]

