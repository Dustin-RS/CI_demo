import pytest


def add(x, y):
    return x+y


def test_capital_case():
    assert add(2, 2) == 4

def test_capital_cas2e():
    assert add(2, -1) == 1