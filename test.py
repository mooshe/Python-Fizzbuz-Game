import pytest


def fizz_buzz(number):
    if number %3 == 0:
        return "fizz"
    return str(number)


def test_answer():
    check(1, "1")
    check(2, "2")
    check(3, "fizz")


def check(number, expected_result):
    assert fizz_buzz(number) == expected_result



