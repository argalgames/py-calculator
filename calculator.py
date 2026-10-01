def add(a, b):
  """Return the sum of a and b.

  Works with ints and floats, e.g. add(2, 3) -> 5.
  """
  return a + b

def subtract(a, b):
  """Return a minus b (order matters: b is taken away from a).

  Works with ints and floats, e.g. subtract(10, 4) -> 6.
  """
  return a - b

def multiply(a, b):
  """Return the product of a and b.

  Works with ints and floats, e.g. multiply(4, 5) -> 20.
  """
  return a * b

def divide(a, b):
  """Return a divided by b (order matters: a is split by b).

  Works with ints and floats, e.g. divide(10, 4) -> 2.5.
  Raises ZeroDivisionError if b is 0.
  """
  return a / b

def get_number(prompt):
  """Keep asking until the user enters a valid number."""
  while True:
    try:
      return float(input(prompt))
    except ValueError:
      print("Please enter a valid number")

def get_operator():
  """Keep asking until the user enters +, -, *, or /."""
  while True:
    operator = input("Operator (+, -, *, or /): ").strip()
    if operator in ("+", "-", "*", "/"):
      return operator
    print("Please enter +, -, *, or /")

def format_result(value):
  """Return value as text, without a trailing .0 for whole numbers."""
  value = round(value, 10)
  if value.is_integer():
    return str(int(value))
  else:
    return str(value)

def main():
  """Run the calculator: read two numbers and print their sum or difference."""
  a = get_number("Enter first number: ")
  operator = get_operator()
  b = get_number("Enter second number: ")

  try:
    if operator == "+":
      result = add(a, b)
    elif operator == "-":
      result = subtract(a, b)
    elif operator == "*":
      result = multiply(a, b)
    elif operator == "/":
      result = divide(a, b)
    print(format_result(result))
  except ZeroDivisionError:
    print("Cannot divide by zero")

if __name__ == "__main__":
  main()