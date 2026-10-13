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

def power(a, b):
  """Return a raised to the power of b (order matters: b is the exponent).

  Works with ints and floats, e.g. power(2, 3) -> 8.
  Raises ValueError if a is negative and b is not a whole number,
  because the result would not be a real number.
  Raises OverflowError if the result is too large to store.
  """
  if a < 0 and not float(b).is_integer():
    raise ValueError("a negative number can't be raised to a fractional power")
  return a ** b

OPERATIONS = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
  "**": power
}

def get_number(prompt):
  """Keep asking until the user enters a valid number."""
  while True:
    try:
      return float(input(prompt))
    except ValueError:
      print("Please enter a valid number")

def get_operator():
  """Keep asking until the user enters an operator listed in OPERATIONS."""
  while True:
    operator = input(f"Operator {', '.join(OPERATIONS)}: ").strip()
    if operator in OPERATIONS:
      return operator
    print(f"Please enter one of: {', '.join(OPERATIONS)}")

def format_result(value):
  """Return value as text, without a trailing .0 for whole numbers."""
  value = round(value, 10)
  if value.is_integer():
    return str(int(value))
  else:
    return str(value)

def calculate(a, operator, b):
  """Return the result of 'a operator b' as text, e.g. calculate(4, "*", 5) -> "20".

  If the calculation fails (division by zero, invalid power, or a result
  too large), return a "Cannot calculate: ..." message instead of raising.
  """
  try:
    return format_result(OPERATIONS[operator](a, b))
  except (ZeroDivisionError, ValueError, OverflowError) as error:
    return f"Cannot calculate: {error}"

def main():
  """Run the calculator in a loop until the user chooses to stop.

  Each round reads two numbers and an operator, then prints the result.
  Answering anything other than y/yes to "Another calculation?" quits.
  Ctrl+C or end of input (Ctrl+Z then Enter on Windows) exits cleanly
  at any prompt.
  """
  try:
    while True:
      a = get_number("Enter first number: ")
      operator = get_operator()
      b = get_number("Enter second number: ")
      print(calculate(a, operator, b))

      again = input("Another calculation? (y/n): ").strip().lower()
      if again not in ("y", "yes"):
        print("Goodbye!")
        break
  except (KeyboardInterrupt, EOFError):
    print()
    print("Goodbye!")

if __name__ == "__main__":
  main()