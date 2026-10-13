# py-calculator

A simple command-line calculator written in Python. It reads two numbers and an operator, prints the result, and keeps going until you choose to stop.

## Features

- Five operations: addition, subtraction, multiplication, division, and powers
- Asks again when a number or operator is invalid, instead of crashing
- Shows friendly messages for division by zero, invalid powers (such as `-8 ** 0.5`), and results that are too large
- Clean output: whole numbers are shown without a trailing `.0`, and floating-point noise is rounded away (`0.1 + 0.2` shows `0.3`)
- Runs several calculations in a row; exits cleanly with `n`, Ctrl+C, or end of input

## Requirements

- Python 3.12 or newer
- [pytest](https://docs.pytest.org/), only needed to run the tests

## Usage

```bash
python calculator.py
```

Example session:

```text
Enter first number: 10
Operator +, -, *, /, **: /
Enter second number: 4
2.5
Another calculation? (y/n): y
Enter first number: abc
Please enter a valid number
Enter first number: 2
Operator +, -, *, /, **: %
Please enter one of: +, -, *, /, **
Operator +, -, *, /, **: **
Enter second number: 10
1024
Another calculation? (y/n): y
Enter first number: 5
Operator +, -, *, /, **: /
Enter second number: 0
Cannot calculate: division by zero
Another calculation? (y/n): n
Goodbye!
```

### Supported operators

| Operator | Operation | Example | Result |
|---|---|---|---|
| `+` | Addition | `2 + 3` | `5` |
| `-` | Subtraction | `10 - 4` | `6` |
| `*` | Multiplication | `4 * 5` | `20` |
| `/` | Division | `10 / 4` | `2.5` |
| `**` | Power | `2 ** 10` | `1024` |

## Running the tests

```bash
python -m pip install pytest
python -m pytest
```

The tests in `test_calculator.py` cover each operation, result formatting, and the error cases.

## How it works

All the code lives in `calculator.py`:

- **Math functions:** `add`, `subtract`, `multiply`, `divide`, and `power` only do the calculation. `divide` and `power` raise an error for invalid input instead of printing anything.
- **`OPERATIONS`:** a dictionary that maps each operator symbol to its function. It is the single place where operators are defined; the prompt and the input validation are built from it.
- **`calculate(a, operator, b)`:** looks up the operation, runs it, and returns the result as text, or a `Cannot calculate: ...` message if the operation raised an error.
- **`get_number` / `get_operator`:** keep asking until the input is valid.
- **`main()`:** runs the input → calculate → print loop.

### Adding a new operation

1. Write a function that takes two numbers and returns the result.
2. Add it to `OPERATIONS`, for example `"%": modulo`.
3. Add tests for it in `test_calculator.py`.

The prompt and input validation pick up the new operator automatically, so `main()` and `get_operator()` don't need any changes.
