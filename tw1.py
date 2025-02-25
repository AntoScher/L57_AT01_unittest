import pytest
from main import check

def test_check():
   assert check(6) == True

def test_check2():
   assert check(3) == False

@pytest.mark.parametrize("number, expected", [
   (2, True),
   (5, False),
   (0, True),
   (56, True),
   (-3, True)

])
def test_check_with_param(number, expected):
   assert check(number) == expected


