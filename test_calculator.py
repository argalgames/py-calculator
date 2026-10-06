from calculator import add, subtract, multiply, divide, power, format_result
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

def test_subtract_two_positive_numbers():
  assert subtract(10, 4) == 6

def test_subtract_result_below_zero():
  assert subtract(3, 5) == -2

def test_subtract_two_negative_numbers():
  assert subtract(-2, -7) == 5

def test_subtract_negative_positive_numbers():
  assert subtract(-3, 5) == -8

def test_subtract_positive_negative_numbers():
  assert subtract(5, -8) == 13

def test_subtract_decimal_positive_numbers():
  assert subtract(5.5, 3) == 2.5

def test_subtract_decimal_negative_numbers():
  assert subtract(5.5, -3) == 8.5

def test_subtract_decimal_precision():
  assert subtract(0.2, 0.3) == pytest.approx(-0.1)

def test_multiply_normal():
  assert multiply(4, 5) == 20

def test_multiply_by_zero():
  assert multiply(7, 0) == 0

def test_mutiply_negative_positive_numbers():
  assert multiply(-3, 5) == -15

def test_multiply_negative_numbers():
  assert multiply(-3, -4) == 12

def test_multiply_decimal_precision():
  assert multiply(0.2, 0.3) == pytest.approx(0.06)

def test_divide_normal():
  assert divide(6, 2) == 3

def test_divide_negative_positive_numbers():
  assert divide(-10, 5) == -2

def test_divide_negative_numbers():
  assert divide(-10, -2) == 5

def test_divide_decimal_precision():
  assert divide(2, 3) == pytest.approx(0.6666667)

def test_divide_by_zero_raises_error():
  with pytest.raises(ZeroDivisionError):
    divide(5, 0)

def test_power_normal():
  assert power(2, 3) == 8

def test_power_to_zero():
  assert power(5, 0) == 1

def test_power_positive_negative():
  assert power(2, -1) == 0.5

def test_power_positive_fraction():
  assert power(9, 0.5) == 3

def test_power_negative_base_fractional_exponent_raises_error():
  with pytest.raises(ValueError):
    power(-8, 0.5)

def test_positive_format_result():
  assert format_result(5.0) == "5"

def test_decimal_format_result():
  assert format_result(3.5) == "3.5"

def test_negative_format_result():
  assert format_result(-2.0) == "-2"