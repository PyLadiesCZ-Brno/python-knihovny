#!/bin/bash
# generate_tasks.sh
#
# Tento soubor obsahuje 25 ukázkových úkolů z Pythonu a jejich testy v pytest.
# Každý úkol má samostatné zadání a testovací soubor.
#
# Níže najdeš vygenerovaný bashový skript pro vytvoření všech souborů i s jejich obsahem.

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

# Zadání a testy pro každou úlohu

write_task_and_test "01" "sum_two_numbers" '
def sum_two_numbers(a: int, b: int) -> int:
    """
    Vrátí součet dvou čísel.
    """
' '
import pytest
from tasks.task_01_sum_two_numbers import sum_two_numbers

def test_sum_two_numbers():
    assert sum_two_numbers(1, 2) == 3
    assert sum_two_numbers(-1, 1) == 0
    assert sum_two_numbers(0, 0) == 0
'

write_task_and_test "02" "is_even" '
def is_even(n: int) -> bool:
    """
    Vrátí True, pokud je číslo sudé.
    """
' '
import pytest
from tasks.task_02_is_even import is_even

def test_is_even():
    assert is_even(2)
    assert not is_even(3)
    assert is_even(0)
'

write_task_and_test "03" "max_of_three" '
def max_of_three(a: int, b: int, c: int) -> int:
    """
    Vrátí největší ze tří čísel.
    """
' '
import pytest
from tasks.task_03_max_of_three import max_of_three

def test_max_of_three():
    assert max_of_three(1, 2, 3) == 3
    assert max_of_three(9, 3, 6) == 9
    assert max_of_three(-1, -5, -3) == -1
'

write_task_and_test "04" "factorial" '
def factorial(n: int) -> int:
    """
    Vrátí faktoriál čísla n.
    """
' '
import pytest
from tasks.task_04_factorial import factorial

def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120
    assert factorial(3) == 6
'

write_task_and_test "05" "count_vowels" '
def count_vowels(s: str) -> int:
    """
    Vrátí počet samohlásek v řetězci.
    """
' '
import pytest
from tasks.task_05_count_vowels import count_vowels

def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("xyz") == 0
    assert count_vowels("AEIOU") == 5
'

write_task_and_test "06" "filter_by_age" '
def filter_by_age(people: dict):
    """
    Napiš funkci filter_by_age, která vezme seznam slovníků, kde každý slovník
    představuje osobu (s klíči name a age), a vrátí seznam osob, které jsou
    starší než 18 let.
    """
' '
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
        {"name": "Charlie", "age": 22},
        {"name": "David", "age": 18}
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
'

write_task_and_test "07" "reverse_string" '
def reverse_string(s: str) -> str:
    """
    Vrátí obrácený řetězec.
    """
' '
import pytest
from tasks.task_07_reverse_string import reverse_string

def test_reverse_string():
    assert reverse_string("abc") == "cba"
    assert reverse_string("") == ""
    assert reverse_string("racecar") == "racecar"
'

write_task_and_test "08" "is_prime" '
def is_prime(n: int) -> bool:
    """
    Vrátí True, pokud je číslo prvočíslo.
    """
' '
import pytest
from tasks.task_08_is_prime import is_prime

def test_is_prime():
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(4)
    assert is_prime(13)
'

write_task_and_test "09" "unique_elements" '
def unique_elements(lst: list[int]) -> list[int]:
    """
    Vrátí seznam bez duplicitních prvků, zachová původní pořadí.
    """
' '
import pytest
from tasks.task_09_unique_elements import unique_elements

def test_unique_elements():
    assert unique_elements([1, 2, 2, 3]) == [1, 2, 3]
    assert unique_elements([]) == []
    assert unique_elements([4, 4, 4, 4]) == [4]
'

write_task_and_test "10" "flatten_list" '
def flatten_list(nested: list[list[int]]) -> list[int]:
    """
    Zploští dvourozměrný seznam do jednoho seznamu.
    """
' '
import pytest
from tasks.task_10_flatten_list import flatten_list

def test_flatten_list():
    assert flatten_list([[1, 2], [3, 4]]) == [1, 2, 3, 4]
    assert flatten_list([[], [1], []]) == [1]
    assert flatten_list([]) == []
'


write_task_and_test "11" "count_words" '
def count_words(s: str) -> int:
    """
    Vrátí počet slov v řetězci oddělených mezerami.
    """
' '
import pytest
from tasks.task_11_count_words import count_words

def test_count_words():
    assert count_words("hello world") == 2
    assert count_words("one") == 1
    assert count_words("") == 0
    assert count_words("this is a test") == 4
'

write_task_and_test "12" "even_numbers" '
def even_numbers(lst: list[int]) -> list[int]:
    """
    Vrátí seznam pouze sudých čísel.
    """
' '
import pytest
from tasks.task_12_even_numbers import even_numbers

def test_even_numbers():
    assert even_numbers([1, 2, 3, 4, 5]) == [2, 4]
    assert even_numbers([1, 3, 5]) == []
    assert even_numbers([2, 4, 6]) == [2, 4, 6]
'

write_task_and_test "13" "max_in_list" '
def max_in_list(lst: list[int]) -> int:
    """
    Vrátí největší číslo v seznamu.
    """
' '
import pytest
from tasks.task_13_max_in_list import max_in_list

def test_max_in_list():
    assert max_in_list([1, 2, 3]) == 3
    assert max_in_list([-1, -2, -3]) == -1
    assert max_in_list([10]) == 10
'

write_task_and_test "14" "remove_zeros" '
def remove_zeros(lst: list[int]) -> list[int]:
    """
    Vrátí seznam bez nulových hodnot.
    """
' '
import pytest
from tasks.task_14_remove_zeros import remove_zeros

def test_remove_zeros():
    assert remove_zeros([0, 1, 0, 2]) == [1, 2]
    assert remove_zeros([0, 0, 0]) == []
    assert remove_zeros([5, 6, 7]) == [5, 6, 7]
'

write_task_and_test "15" "square_numbers" '
def square_numbers(lst: list[int]) -> list[int]:
    """
    Vrátí seznam čtverců čísel ze vstupního seznamu.
    """
' '
import pytest
from tasks.task_15_square_numbers import square_numbers

def test_square_numbers():
    assert square_numbers([1, 2, 3]) == [1, 4, 9]
    assert square_numbers([-1, -2]) == [1, 4]
    assert square_numbers([]) == []
'


write_task_and_test "16" "remove_duplicates" '
def remove_duplicates(lst: list[int]) -> list[int]:
    """
    Vrátí nový seznam bez duplicitních hodnot, zachová původní pořadí.
    """
' '
import pytest
from tasks.task_16_remove_duplicates import remove_duplicates

def test_remove_duplicates():
    assert remove_duplicates([1, 2, 2, 3]) == [1, 2, 3]
    assert remove_duplicates([1, 1, 1]) == [1]
    assert remove_duplicates([]) == []
'

write_task_and_test "17" "capitalize_words" '
def capitalize_words(s: str) -> str:
    """
    Vrátí řetězec, kde každé slovo začíná velkým písmenem.
    """
' '
import pytest
from tasks.task_17_capitalize_words import capitalize_words

def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"
    assert capitalize_words("") == ""
    assert capitalize_words("python programming") == "Python Programming"
'

write_task_and_test "18" "factorial" '
def factorial(n: int) -> int:
    """
    Vrátí faktoriál čísla n (n!).
    """
' '
import pytest
from tasks.task_18_factorial import factorial

def test_factorial():
    assert factorial(0) == 1
    assert factorial(3) == 6
    assert factorial(5) == 120
'

write_task_and_test "19" "is_palindrome" '
def is_palindrome(s: str) -> bool:
    """
    Vrátí True, pokud je řetězec palindrom.
    """
' '
import pytest
from tasks.task_19_is_palindrome import is_palindrome

def test_is_palindrome():
    assert is_palindrome("radar")
    assert not is_palindrome("hello")
    assert is_palindrome("a")
    assert is_palindrome("")
'

write_task_and_test "20" "second_largest" '
def second_largest(lst: list[int]) -> int:
    """
    Vrátí druhé největší číslo v seznamu.
    """
' '
import pytest
from tasks.task_20_second_largest import second_largest

def test_second_largest():
    assert second_largest([1, 2, 3]) == 2
    assert second_largest([10, 20, 30, 30]) == 20
    assert second_largest([5, 1]) == 1
'

write_task_and_test "21" "reverse_list" '
def reverse_list(lst: list[int]) -> list[int]:
    """
    Vrátí seznam v opačném pořadí.
    """
' '
import pytest
from tasks.task_21_reverse_list import reverse_list

def test_reverse_list():
    assert reverse_list([1, 2, 3]) == [3, 2, 1]
    assert reverse_list([]) == []
    assert reverse_list([42]) == [42]
'

write_task_and_test "22" "fibonacci" '
def fibonacci(n: int) -> list[int]:
    """
    Vrátí prvních n členů Fibonacciho posloupnosti.
    """
' '
import pytest
from tasks.task_22_fibonacci import fibonacci

def test_fibonacci():
    assert fibonacci(0) == []
    assert fibonacci(1) == [0]
    assert fibonacci(5) == [0, 1, 1, 2, 3]
'

write_task_and_test "23" "remove_vowels" '
def remove_vowels(s: str) -> str:
    """
    Vrátí řetězec bez samohlásek (a, e, i, o, u).
    """
' '
import pytest
from tasks.task_23_remove_vowels import remove_vowels

def test_remove_vowels():
    assert remove_vowels("hello") == "hll"
    assert remove_vowels("AEIOU") == ""
    assert remove_vowels("python") == "pythn"
'

write_task_and_test "24" "unique_characters" '
def unique_characters(s: str) -> bool:
    """
    Vrátí True, pokud řetězec obsahuje pouze unikátní znaky.
    """
' '
import pytest
from tasks.task_24_unique_characters import unique_characters

def test_unique_characters():
    assert unique_characters("abc")
    assert not unique_characters("aabb")
    assert unique_characters("")
'

write_task_and_test "25" "sum_of_digits" '
def sum_of_digits(n: int) -> int:
    """
    Vrátí součet číslic čísla.
    """
' '
import pytest
from tasks.task_25_sum_of_digits import sum_of_digits

def test_sum_of_digits():
    assert sum_of_digits(123) == 6
    assert sum_of_digits(0) == 0
    assert sum_of_digits(-456) == 15
'
