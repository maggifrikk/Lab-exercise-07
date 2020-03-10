import pytest

def FizzBuss(num):
    if num % 5 and num % 3 == 0:
        return "FizzBuzz"
    elif num % 5 == 0 and num % 3 != 0:
        return "Buzz"
    elif num % 5 != 0 and num % 3 == 0:
        return "Fizz"
    else:
        return num

def test_FizzBuzz():
    assert FizzBuss(19) == 19