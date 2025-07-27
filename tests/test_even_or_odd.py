# tests/test_even_or_odd.py
from assignmen.Even_or_odd import is_even

def test_even():
    assert is_even(4) == True

def test_odd():
    assert is_even(5) == False
