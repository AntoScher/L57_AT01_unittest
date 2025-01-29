import pytest
from main import count_vowels

def test_count_vowels_empty_string():
    assert count_vowels("") == 0

def test_count_vowels_only_consonants():
    assert count_vowels("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ") == 0

def test_count_vowels_mixed_case():
    assert count_vowels("AaEeIiOoUu") == 10

def test_count_vowels_with_spaces():
    assert count_vowels("This is a test sentence") == 6

def test_count_vowels_russian_vowels():
    assert count_vowels("АЕЁИОУЫЭЮЯаеёиоуыэюя") == 20

def test_count_vowels_mixed_languages():
    assert count_vowels("Hello Привет") == 5  # 2 English vowels + 3 Russian vowels

def test_count_vowels_with_punctuation():
    assert count_vowels("Hello, world!") == 3

def test_count_vowels_numbers_and_symbols():
    assert count_vowels("1234567890!@#$%^&*()") == 0

if __name__ == "__main__":
    pytest.main()
