# test_32_decode_string.py

import pytest
from tasks.task_32_decode_string import decode_string

def test_decode_string():
    assert decode_string("3[a]2[bc]") == "aaabcbc"
    assert decode_string("2[abc]3[cd]ef") == "abcabccdcdcdef"
    assert decode_string("3[a2[c]]") == "accaccacc"
    assert decode_string("2[2[b]3[a]]") == "bbaaabbaaa"
    assert decode_string("10[a]") == "aaaaaaaaaa"
    assert decode_string("3[z]2[2[y]pq4[2[jk]e1[f]]]ef") == "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"
    assert decode_string("abc3[cd]xyz") == "abccdcdcdxyz"
    assert decode_string("2[ab3[c]]") == "abcccabccc"
    assert decode_string("100[code]") == "code" * 100
    assert decode_string("0[abc]") == ""

