import pytest

from toolkit.calculator import calc
from toolkit.errors import CalculatorError


def test_priority():
    assert calc("2+2*2") == 6.0


def test_negative_number():
    assert calc("-6*7") == -42.0


def test_empty_expression():
    with pytest.raises(CalculatorError):
        calc("")


def test_invalid_character():
    with pytest.raises(CalculatorError):
        calc("2+a")


def test_division_by_zero():
    with pytest.raises(CalculatorError):
        calc("5/0")
