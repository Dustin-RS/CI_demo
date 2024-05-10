import pytest


def add(x, y):
    return x+y


def test_capital_case():
    assert add(2, 2) == 4