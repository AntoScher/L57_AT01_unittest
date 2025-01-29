main.py


def is_palindrome(s):
   return s == s[::-1]


test.py

import pytest
from main import is_palindrome  # замените my_module на имя вашего модуля

def test_is_palindrome_true():
   assert is_palindrome("madam") == True

def test_is_palindrome_false():
   assert is_palindrome("hello") == False

@pytest.mark.parametrize("s, expected", [
   ("racecar", True),
   ("python", False),
   ("level", True),
   ("", True),  # Пустая строка является палиндромом
])
def test_is_palindrome_parametrized(s, expected):
   assert is_palindrome(s) == expected



main.py

def sort_list(numbers):
   return sorted(numbers)


test.py

import pytest
from main import sort_list  # замените my_module на имя вашего модуля

def test_sort_list_ascending():
   assert sort_list([3, 1, 2, 5, 4]) == [1, 2, 3, 4, 5]

def test_sort_list_descending():
   assert sort_list([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_sort_list_mixed():
   assert sort_list([-1, 3, 0, -2, 2]) == [-2, -1, 0, 2, 3]

@pytest.mark.parametrize("numbers, expected", [
   ([7, 2, 5, 3], [2, 3, 5, 7]),
   ([10, -10, 0], [-10, 0, 10]),
   ([], []),
   ([1], [1])
])
def test_sort_list_parametrized(numbers, expected):
   assert sort_list(numbers) == expected

