def add(a, b):
  """Return the sum of a and b.

  Works with ints and floats, e.g. add(2, 3) -> 5.
  """
  return a + b

def get_number(prompt):
  """Keep asking until the user enters a valid number."""
  while True:
    try:
      return float(input(prompt))
    except ValueError:
      print("Please enter a valid number")

def main():
  """Run the calculator: read two numbers and print their sum."""
  a = get_number("Enter first number: ")
  b = get_number("Enter second number: ")

  result = add(a, b)

  if result.is_integer():
    print(int(result))
  else:
    print(result)

if __name__ == "__main__":
  main()