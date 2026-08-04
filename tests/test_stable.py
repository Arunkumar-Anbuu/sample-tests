"""
Stable tests — deterministic, always pass.

TRUE FLAKINESS RATE: 0%  (ground truth you control)

These are the clean negatives in your dataset: tests that never flip.
A good flaky-detector must NOT flag these.
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from src import Calculator as calc


def test_add():
    assert calc.add(2, 3) == 5


def test_subtract():
    assert calc.subtract(10, 4) == 6


def test_multiply():
    assert calc.multiply(3, 7) == 21


def test_divide():
    assert calc.divide(10, 2) == 5


def test_divide_by_zero():
    try:
        calc.divide(1, 0)
        assert False, "should have raised"
    except ValueError:
        assert True