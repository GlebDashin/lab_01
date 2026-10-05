import pytest

from toolkit.converter import convert
from toolkit.errors import ConverterError


def test_length():
    assert convert(2.0, "KM", "m") == 2000.0


def test_temperature():
    assert convert(0.0, "c", "f") == pytest.approx(32.0)


def test_unknown_unit():
    with pytest.raises(ConverterError):
        convert(1.0, "xyz", "m")


def test_incompatible_units():
    with pytest.raises(ConverterError):
        convert(1.0, "kg", "m")


def test_absolute_zero():
    assert convert(-273.15, "c", "k") == pytest.approx(0.0)
