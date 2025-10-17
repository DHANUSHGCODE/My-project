import pytest

from main import add, _to_number


def test_add_integers():
    assert add(2, 3) == 5


def test_add_floats():
    assert add(1.5, 2.25) == pytest.approx(3.75)


def test_to_number_int():
    assert _to_number("10") == 10


def test_to_number_float():
    assert _to_number("3.14") == pytest.approx(3.14)


def test_to_number_invalid():
    with pytest.raises(ValueError):
        _to_number("abc")
