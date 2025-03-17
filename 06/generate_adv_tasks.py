#!/bin/bash

mkdir -p tasks

function write_task_and_test() {
  num=$1
  name=$2
  task_code=$3
  test_code=$4

  task_file="tasks/task_${num}_${name}.py"
  test_file="test_${num}_${name}.py"

  echo "# task_${num}_${name}.py" > "$task_file"
  echo -e "$task_code" >> "$task_file"

  echo "# test_${num}_${name}.py" > "$test_file"
  echo -e "$test_code" >> "$test_file"
}


write_task_and_test "26" "is_palindrome_sentence" '
def is_palindrome_sentence(s: str) -> bool:
    """
    Vrátí True, pokud je věta palindrom (ignoruje mezery, interpunkci a velikost písmen).
    """
' '
import pytest
from tasks.task_26_is_palindrome_sentence import is_palindrome_sentence

def test_is_palindrome_sentence():
    assert is_palindrome_sentence("A man, a plan, a canal: Panama")
    assert is_palindrome_sentence("No lemon, no melon")
    assert is_palindrome_sentence("Eva, can I see bees in a cave?")
    assert is_palindrome_sentence("Was it a car or a cat I saw?")
    assert not is_palindrome_sentence("This is not a palindrome")
    assert not is_palindrome_sentence("And this also not")
'


write_task_and_test "27" "group_anagrams" '
def group_anagrams(words: list[str]) -> list[list[str]]:
    """
    Skupiny anagramů v seznamu slov. Seznamy musí být seřazené. Anagramy v seznamech také seřazené.
    """
' '
import pytest
from tasks.task_27_group_anagrams import group_anagrams

def test_group_anagrams():
    assert group_anagrams(["bat", "cat", "tab", "act"]) == [["act", "cat"], ["bat", "tab"]]
    assert group_anagrams(["google", "silent", "gogole", "listen", "enlist"]) == [["enlist", "listen", "silent"], ["gogole", "google"]]
    assert group_anagrams([]) == []
    assert group_anagrams(["abc"]) == [["abc"]]
    assert group_anagrams(["cab", "xyz", "abc", "zyx", "bca"]) == [["abc", "bca", "cab"], ["xyz", "zyx"]]
    assert group_anagrams(["rat", "tar", "art", "star", "tars", "cheese"]) == [["art", "rat", "tar"], ["cheese"], ["star", "tars"]]
'


write_task_and_test "28" "flatten_list" '
def flatten_list(nested: list[list[int]]) -> list[int]:
    """
    Převede dvourozměrný seznam na jednorozměrný.
    """
' '
import pytest
from tasks.task_28_flatten_list import flatten_list

def test_flatten_list():
    assert flatten_list([[1, 2], [3, 4]]) == [1, 2, 3, 4]
    assert flatten_list([[], [1], [], [2, 3]]) == [1, 2, 3]
    assert flatten_list([]) == []
    assert flatten_list([[1]]) == [1]
    assert flatten_list([[1, 2, 3], [], [4], [5, 6]]) == [1, 2, 3, 4, 5, 6]
    assert flatten_list([[0], [0, 0]]) == [0, 0, 0]
    assert flatten_list([[10, 20], [30], [], [40, 50, 60]]) == [10, 20, 30, 40, 50, 60]
    assert flatten_list([[1], [], [], [], [2]]) == [1, 2]
'


write_task_and_test "29" "longest_common_prefix" '
def longest_common_prefix(strings: list[str]) -> str:
    """
    Vrátí nejdelší společný prefix v seznamu řetězců.
    """
' '
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
'


write_task_and_test "30" "remove_duplicates" '
def remove_duplicates(nums: list[int]) -> list[int]:
    """
    Odstraní duplikáty ze seznamu a zachová pořadí.
    """
' '
import pytest
from tasks.task_30_remove_duplicates import remove_duplicates

def test_remove_duplicates():
    assert remove_duplicates([1,2,2,3,1]) == [1,2,3]
    assert remove_duplicates([]) == []
    assert remove_duplicates([1,1,1,1]) == [1]
    assert remove_duplicates([3,2,1,2,3]) == [3,2,1]
'


write_task_and_test "31" "reverse_words" '
def reverse_words(s: str) -> str:
    """
    Otočí pořadí slov ve větě.
    """
' '
import pytest
from tasks.task_31_reverse_words import reverse_words

def test_reverse_words():
    assert reverse_words("hello world") == "world hello"
    assert reverse_words("one two three") == "three two one"
    assert reverse_words("single") == "single"
    assert reverse_words("a b c d") == "d c b a"
    assert reverse_words("   spaced   words  test ") == "test words spaced"
    assert reverse_words("") == ""
'


write_task_and_test "32" "decode_string" '
def decode_string(s: str) -> str:
    """
    Dekóduje zakódovaný řetězec ve formátu k[encoded_string],
    např. "3[a]2[bc]" → "aaabcbc".
    """
' '
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
'


write_task_and_test "33" "valid_parentheses" '
def valid_parentheses(s: str) -> bool:
    """
    Zjistí, zda má řetězec validní závorky.
    """
' '
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
'


write_task_and_test "34" "rotate_list" '
def rotate_list(lst: list[int], k: int) -> list[int]:
    """
    Posune prvky seznamu o k pozic doprava.
    """
' '
import pytest
from tasks.task_34_rotate_list import rotate_list

def test_rotate_list():
    assert rotate_list([1,2,3,4,5], 2) == [4,5,1,2,3]
    assert rotate_list([1,2,3], 1) == [3,1,2]
    assert rotate_list([1,2,3], 0) == [1,2,3]
    assert rotate_list([1,2,3], 3) == [1,2,3]
    assert rotate_list([], 2) == []
    assert rotate_list([1], 10) == [1]
'


write_task_and_test "35" "rotate_matrix" '
def rotate_matrix(matrix: list[list[int]]) -> list[list[int]]:
    """
    Otočí čtvercovou matici o 90 stupňů ve směru hodinových ručiček.
    """
' '
import pytest
from tasks.task_35_rotate_matrix import rotate_matrix

def test_rotate_matrix():
    assert rotate_matrix([[1]]) == [[1]]

    assert rotate_matrix([
        [1, 2],
        [3, 4]
    ]) == [
        [3, 1],
        [4, 2]
    ]

    assert rotate_matrix([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]) == [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ]

    assert rotate_matrix([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10,11,12],
        [13,14,15,16]
    ]) == [
        [13, 9, 5, 1],
        [14,10, 6, 2],
        [15,11, 7, 3],
        [16,12, 8, 4]
    ]

    assert rotate_matrix([
        [0, 1],
        [2, 3]
    ]) == [
        [2, 0],
        [3, 1]
    ]

'
