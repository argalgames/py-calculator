from calculator import add
import pytest

def test_add_two_positive_numbers():
  assert add(2, 3) == 5

def test_add_two_negative_numbers():
  assert add(-2, -3) == -5

def test_add_positive_negative_numbers():
  assert add(-2, 3) == 1

def test_add_two_decimal_numbers():
  assert add(2.5, 0.5) == 3

def test_add_decimals_precision():
  assert add(0.1, 0.2) == pytest.approx(0.3)