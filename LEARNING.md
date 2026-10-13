# Learning notes: py-calculator

What I learned while building this calculator, step by step, and the mistakes I made along the way. To pick the project up again, read **Quick reference** and **Ideas for next time** at the bottom.

## Step by step

### 1. Functions (`add`)
- `def name(params):` defines a function. **`return`** hands a value back to the caller; `print` only shows it on screen.
- Prefer returning: a returned value can be tested, reused, and printed later.
- `int` and `float` mix freely: `add(2.5, 0.5)` → `3.0`.

### 2. Docstrings and comments
- A **docstring** (`"""..."""` as the first line inside a function) explains *what* the function does. It shows up in `help(add)` and on hover in VS Code.
- A **`#` comment** explains *why* a particular line does something. Python ignores it.
- A `"""string"""` in the middle of a file is **not** a docstring, just an unused string. Use `#` for section labels.
- PEP 8 style uses **4-space** indentation. This project uses 2; what matters is being consistent.

### 3. User input and type conversion
- `input()` **always returns a string**, so `"2" + "3"` → `"23"`.
- Convert first: `float(input(...))`. Use `float` rather than `int`, because `int("2.5")` fails.
- `int(3.5)` → `3`: it **truncates** (chops off the decimals), it does not round.
- `value.is_integer()` checks whether a float has no decimal part.

### 4. Handling bad input
- `try:` / `except ValueError:` catches the error from `float("abc")` instead of crashing.
- Catch **specific** errors. A bare `except:` hides bugs and even blocks Ctrl+C.
- `while True:` + `return` keeps asking until the input is valid, as in `get_number(prompt)`.

### 5. `if __name__ == "__main__":`
- **Importing a file runs all of it.** Without the guard, `from calculator import add` started the program.
- `__name__` is `"__main__"` when the file is run directly, and the module name when it's imported.
- Put the program in `main()` and call it under the guard.

### 6. Testing with pytest
- Files are named `test_*.py`, functions `test_*`. Check results with `assert`.
- Run: `python -m pytest`.
- Floats are imprecise: `0.1 + 0.2` → `0.30000000000000004`. Compare with `pytest.approx(0.3)`.
- `pytest.approx` allows only about one part in a million: `approx(0.67)` does **not** match `2/3`.
- Don't write `pytest.approx(2 / 3)`: it repeats the code's own calculation, so it proves nothing.
- A failing test can mean the **test** is wrong (`multiply(0.2, .03) == 0.6`). Check both.

### 7. Subtraction, choosing an operator, `format_result`
- **Test-driven development (TDD):** write the test first, see it fail (`ImportError`), then write the code.
- `if` / `elif` / `else` picks the operation.
- **One job per function:** math functions calculate; `format_result` only formats, and **returns text**.

### 8. Multiplication, division, dividing by zero
- `10 / 0` raises `ZeroDivisionError`. The math function lets the error happen; the code that talks to the user catches it.
- Test that an error is raised:
  ```python
  with pytest.raises(ZeroDivisionError):
      divide(5, 0)
  ```
- If the `try` fails, any variable it was supposed to set is never set. Code that uses it must not run afterwards.

### 9. Refactor with a dictionary + `power`
- **Functions are values:** `f = add` (no brackets), then `f(2, 3)` → `5`.
- `OPERATIONS = {"+": add, ...}` lists the operators in **one place**. Call with `OPERATIONS[operator](a, b)`.
- `", ".join(OPERATIONS)` → `"+, -, *, /, **"`. `join` is called on the **separator** string.
- **f-strings:** `f"Please enter one of: {', '.join(OPERATIONS)}"`.
- **Refactor** = new structure, same behaviour. Tests are the safety net.
- `raise ValueError("message")` raises your own error for input you don't allow.
- Catch several errors at once: `except (ValueError, OverflowError) as error:`, then use `{error}` in the message.
- Adding `**` needed **one line** in `OPERATIONS`. `main()` and `get_operator()` didn't change.

### 10. Loop and `calculate()`
- Moved the calculation out of `main()` into `calculate(a, operator, b)`, which returns text and has no `input`/`print`. Now the full path through `OPERATIONS` is tested.
- `.strip().lower()` cleans up the user's answer. `not in ("y", "yes")` checks it against several values.
- Ctrl+C raises `KeyboardInterrupt`; end of input (Ctrl+Z then Enter on Windows) raises `EOFError`. Catch both **around the whole loop** so every prompt is covered.
- **Descriptive test names**, e.g. `test_calculate_divide_by_zero_returns_error_message`. When one fails, the name tells you what broke.

### 11. Virtual environment + `requirements.txt`
- A venv gives the project its own Python and packages. It prevents "installed in one Python, VS Code uses another" (the `ModuleNotFoundError: pytest` from Step 6).
- `python -m pip freeze > requirements.txt` pins the exact versions.
- **PowerShell 5.1 saves `>` output as UTF-16.** Re-save as UTF-8 (Ctrl+Shift+P → *Change File Encoding* → *Save with Encoding* → *UTF-8*).
- `.venv/` is ignored by Git. `requirements.txt` is what gets shared.

## Bugs I hit (and how to recognise them)

| Symptom | Cause | Fix |
|---|---|---|
| `2 + 3` gives `23` | `input()` returns strings | `float(input(...))` |
| Loop never ends | `operator != "+" or "-"` is always true | `operator not in ("+", "-")` |
| Program asks for input but prints nothing | function **returns** a value, but nothing prints it | `print(format_result(...))` |
| Extra `None` printed | `print(main())`, and `main()` returns nothing | call `main()` on its own; print inside it |
| `TypeError: 'str' object is not callable` | called the symbol `"+"` instead of the function | `OPERATIONS[operator](a, b)` |
| `UnboundLocalError` after `5 / 0` | `result` was never set because the `try` failed | put the `print` inside the `try` |
| `TypeError: complex doesn't define __round__` | `(-8) ** 0.5` returns a **complex** number; the crash shows up later | check inputs in `power` and `raise ValueError` |
| `OverflowError: Result too large` | `10.0 ** 1000` is too big for a float | catch `OverflowError` |
| Empty function → `SyntaxError` | a function body can't be empty | write `pass` as a placeholder |
| All tests pass but the program crashes | tests didn't cover `main()` | move logic into testable functions like `calculate()` |

## Git workflow

```powershell
# start a feature
git checkout main
git pull
git checkout -b my-feature

# save work
git status
git add <files>
git commit -m "Verb-first summary of the change"
git push -u origin my-feature
# open a PR on GitHub (base: main) and merge it

# clean up after merging
git checkout main
git pull
git branch -d my-feature
git fetch --prune
```

- One branch per feature, and delete it after merging.
- `git branch -d` is the safe delete (it refuses unmerged work). `-D` forces it.
- `.gitignore` covers `__pycache__/`, `.pytest_cache/`, `.venv/`, and `.vscode/` (personal editor settings).
- GitHub links commits to your profile by **exact** email address, dots included.

## Quick reference

```powershell
.venv\Scripts\Activate.ps1          # activate the venv (prompt shows (.venv))
python calculator.py                # run the app
python -m pytest                    # run the tests
python -m pip install -r requirements.txt
```

In VS Code: Ctrl+Shift+P → **Python: Select Interpreter** → pick the `.venv` one.

## Ideas for next time

- **Type hints** (`def add(a: float, b: float) -> float:`) and checking them with `mypy`
- **GitHub Actions** to run the tests on every PR
- **Memory and history** (`m+`, `mr`, a list of past calculations)
- **A `tkinter` GUI** that reuses `calculate()` unchanged
- **Parsing a full expression** like `2 + 3 * 4` (operator precedence)
