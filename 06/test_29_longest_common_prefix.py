# test_29_longest_common_prefix.py

import pytest
from tasks.task_29_longest_common_prefix import longest_common_prefix

def test_longest_common_prefix():
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
    assert longest_common_prefix(["dog", "racecar", "car"]) == ""
    assert longest_common_prefix(["interspace", "interstellar", "interstate"]) == "inters"
    assert longest_common_prefix(["throne", "throne"]) == "throne"
    assert longest_common_prefix(["prefix", "pre", "presume", "presentation"]) == "pre"
    assert longest_common_prefix(["a"]) == "a"
    assert longest_common_prefix([]) == ""
    assert longest_common_prefix(["abc", "abcde", "abcdef"]) == "abc"
    assert longest_common_prefix(["", "abc"]) == ""
    assert longest_common_prefix(["aaa", "aa", "aaa", "aaaaa"]) == "aa"

