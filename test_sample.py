import pytest

def FizzBuss(num):
    if num % 5 and num % 3 == 0:
        return "FizzBuzz"

def test_FizzBuzz():
    assert FizzBuss(15) == "Fizzbuzz"