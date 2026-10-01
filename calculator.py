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

def get_number(prompt):
  """Keep asking until the user enters a valid number."""
  while True:
    try:
      return float(input(prompt))
    except ValueError:
      print("Please enter a valid number")

def get_operator():
  """Keep asking until the user enters + or -."""
  while True:
    operator = input("Operator (+ or -): ").strip()
    if operator in ("+", "-"):
      return operator
    print("Please enter + or -")

def format_result(value):
  """Return value as text, without a trailing .0 for the whole numbers."""
  if value.is_integer():
    return str(int(value))
  else:
    return str(value)

def main():
  """Run the calculator: read two numbers and print their sum or difference."""
  a = get_number("Enter first number: ")
  operator = get_operator()
  b = get_number("Enter second number: ")

  if operator == "+":
    result = add(a, b)
  elif operator == "-":
    result = subtract(a, b)
      
  print(format_result(result))

if __name__ == "__main__":
  main()