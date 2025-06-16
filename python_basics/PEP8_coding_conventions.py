#Below are some of the PEP 8 coding conventions for Python:
# 1. **Indentation**: Use 4 spaces per indentation level. No tabs.
# 2. **Line Length**: Limit all lines to a maximum of 79 characters.
# 3. **Blank Lines**: Use blank lines to separate functions and classes, and larger blocks of code
# inside functions.
# 4. **Imports**: Imports should usually be on separate lines and grouped in the following order:
#    - Standard library imports Example: `import os`, `import sys`
#    - Related third-party imports Example: `import requests`, `import numpy`
#    - Local application/library-specific imports Example: `from mymodule import myfunction`
#    Each group should be separated by a blank line.
# 5. **Whitespace**: Avoid extraneous whitespace in expressions and statements. For example:
#    - Avoid spaces around the `=` sign when used to indicate a keyword argument or a default parameter value.
#    Example: `def func(arg1, arg2=default_value):`
#    - Avoid spaces immediately inside parentheses, brackets, or braces.
#    Example: `my_list = [1, 2, 3]` (not `my_list = [ 1, 2, 3 ]`)
# 6. **Naming Conventions**:
#    - Use `CamelCase` for class names.
#    - Use `snake_case` for function and variable names. Example: `my_function`, `my_variable`.
#    - Use `UPPERCASE_WITH_UNDERSCORES` for constants.
#    - Use `UPPERCASE` for constants.
# 7. **Comments**: Use comments to explain code, but avoid obvious comments. Use inline comments sparingly
# and only when necessary.
# 8. **Docstrings**: Use docstrings to describe modules, classes, and functions.
# Docstrings should be enclosed in triple quotes.

# 9. **Function and Method Definitions**: Use a single blank line to separate methods within a class.
# 10. **Trailing Commas**: Use trailing commas in tuples, lists, and dictionaries to make it easier to add new items.
# 11. **Boolean Values**: Use `is` or `is not` to compare with `None`, and use `==` or `!=` for other comparisons.
# 12. **Type Hints**: Use type hints to indicate the expected types of function arguments and return values.
# 13. **Avoiding Global Variables**: Avoid using global variables unless absolutely necessary.
# 14. **Error Handling**: Use exceptions for error handling, and avoid using bare `except` clauses.
# 15. **Version Control**: Use version control systems like Git to manage changes to your codebase.
# 16. **Testing**: Write tests for your code to ensure correctness and maintainability.
# 17. **Code Formatting**: Use tools like `black` or `autopep8` to automatically format your code according to PEP 8 standards.
# 18. **Avoiding Long Lines**: If a line is too long, break it into multiple lines using parentheses, brackets, or backslashes.
# 19. **Avoiding Magic Numbers**: Use named constants instead of magic numbers to improve code readability.
# 20. **Avoiding Deep Nesting**: Try to avoid deep nesting of code blocks, as it can make the code harder to read and maintain.
# 21. **Using `__main__`**: Use the `if __name__ == "__main__":` construct to allow or prevent parts of code from being
# run when the modules are imported.
# 22. **Avoiding Side Effects**: Functions should not have side effects that affect the global state unless explicitly intended.
# 23. **Using `with` Statements**: Use `with` statements for resource management (like file handling) to ensure proper cleanup.
# 24. **Avoiding Redundant Code**: Avoid duplicating code; instead, use functions or classes to encapsulate reusable logic.
# 25. **Using `assert` Statements**: Use `assert` statements for debugging purposes, but avoid using them for runtime checks.
# 26. **Using `enumerate`**: Use `enumerate()` when you need both the index and the value from a list or iterable.
# 27. **Using `zip`**: Use `zip()` to iterate over multiple iterables in parallel.
# 28. **Using `try` and `except`**: Use `try` and `except` blocks to handle exceptions gracefully,
# and avoid catching all exceptions with a bare `except`.
# 29. **Using `isinstance`**: Use `isinstance()` to check the type of an object instead of using `type()`.
# 30. **Using `lambda` Functions**: Use `lambda` functions for small, throwaway functions, but avoid using them for complex logic.
# 31. **Using `map`, `filter`, and `reduce`**: Use these functions for functional programming constructs,
# but prefer list comprehensions for readability.
# 32. **Using `collections` Module**: Use the `collections` module for specialized data structures like `Counter`,
# `defaultdict`, and `namedtuple`.
# 33. **Using `itertools` Module**: Use the `itertools` module for efficient looping constructs like `chain`,
# `cycle`, and `combinations`.
# 34. **Using `functools` Module**: Use the `functools` module for higher-order functions like `lru_cache`
# and `partial` to optimize function calls.
# 35. **Using `typing` Module**: Use the `typing` module for type hints and annotations to improve code clarity and
# maintainability.

# 36. **Using `dataclasses` Module**: Use the `dataclasses` module to create classes that are primarily used to store data,
# which automatically generates special methods like `__init__`, `__repr__`, and `__eq__`.
# 37. **Using `contextlib` Module**: Use the `contextlib` module to create context managers for resource management.
# 38. **Using `asyncio` Module**: Use the `asyncio` module for writing asynchronous code, especially for I/O-bound tasks.
# 39. **Using `pathlib` Module**: Use the `pathlib` module for file system path manipulations, which provides an object-oriented approach.
# 40. **Using `json` Module**: Use the `json` module for working with JSON data, which is a common data interchange format.
# 41. **Using `csv` Module**: Use the `csv` module for reading and writing CSV files, which is a common format for tabular data.
# 42. **Using `re` Module**: Use the `re` module for regular expression operations, which are useful for pattern matching in strings.
# 43. **Using `logging` Module**: Use the `logging` module for logging messages instead of using print statements,
# which provides a flexible framework for emitting log messages from Python programs.
# 44. **Using `argparse` Module**: Use the `argparse` module for parsing command-line arguments, which provides a way to handle user input.
# 45. **Using `unittest` Module**: Use the `unittest` module for writing unit tests, which helps ensure code correctness and maintainability.
# 46. **Using `pytest` Framework**: Use the `pytest` framework for writing and running tests, which provides a more powerful and flexible testing environment.
# 47. **Using `time` Module**: Use the `time` module for measuring time intervals, which is useful for performance monitoring.
# 48. **Using `datetime` Module**: Use the `datetime` module for working with dates and times, which provides a rich set of functionalities.
# 49. **Using `random` Module**: Use the `random` module for generating random numbers and performing random operations.
# 50. **Using `math` Module**: Use the `math` module for mathematical operations, which provides a wide range of mathematical functions.
# 51. **Using `os` Module**: Use the `os` module for interacting with the operating system, such as file and directory operations.
# 52. **Using `sys` Module**: Use the `sys` module for accessing system-specific parameters and functions, such as command-line arguments.
# 53. **Using `subprocess` Module**: Use the `subprocess` module for spawning new processes, connecting to their input/output/error pipes,
# and obtaining their return codes.
# 54. **Using `socket` Module**: Use the `socket` module for network communication, which provides low-level networking interfaces.
# 55. **Using `sqlite3` Module**: Use the `sqlite3` module for working with SQLite databases, which is a lightweight disk-based database.
# 56. **Using `xml.etree.ElementTree` Module**: Use this module for parsing and creating XML data, which is a common data format.
# 57. **Using `html` Module**: Use the `html` module for escaping and unescaping HTML entities, which is useful for web development.
# 58. **Using `urllib` Module**: Use the `urllib` module for working with URLs, which provides functions for fetching data across the web.
# 59. **Using `requests` Library**: Use the `requests` library for making HTTP requests, which simplifies the process of sending HTTP requests and handling responses.
# 60. **Using `beautifulsoup4` Library**: Use the `beautifulsoup4` library for parsing HTML and XML documents, which is useful for web scraping.