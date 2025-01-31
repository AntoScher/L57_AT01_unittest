import pytest
from main import count_vowels

def test_count_vowels_empty_string():
    assert count_vowels("") == 0

def test_count_vowels_only_consonants():
    assert count_vowels("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ") == 0

def test_count_vowels_mixed_case():
    assert count_vowels("AaEeIiOoUu") == 10

def test_count_vowels_with_spaces():
    assert count_vowels("This is a test sentence") == 7

def test_count_vowels_russian_vowels():
    assert count_vowels("АЕЁИОУЫЭЮЯаеёиоуыэюя") == 20

def test_count_vowels_mixed_languages():
    assert count_vowels("Hello Привет") == 4  # 2 English vowels + 2 Russian vowels

def test_count_vowels_with_punctuation():
    assert count_vowels("Hello, world!") == 3

def test_count_vowels_numbers_and_symbols():
    assert count_vowels("1234567890!@#$%^&*()") == 0

def get_user_input():
    with open("input_string.txt", "r") as f:
        return f.read().strip()

def test_count_vowels_user_input():
    user_input = get_user_input()
    result = count_vowels(user_input)
    print(f"Строка: {user_input}")
    print(f"Количество гласных букв в строке: {result}")
    assert isinstance(result, int)  # Проверка, что результат является целым числом

if __name__ == "__main__":
    pytest.main()
