# :snake: Python - Variable Annotations

[![Python](https://img.shields.io/badge/Python-3.9-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

![image](https://github.com/v-dav/holbertonschool-web_back_end/assets/115344057/6bb56897-324d-419d-90f7-747792f96c81)


## 🧐 Project Overview

Python is a dynamically-typed language, meaning variable types are determined at run-time upon assignment. While Python remains dynamically-typed, Python 3 introduced type annotations, a powerful feature for code documentation and linting.

## 📖 Learning objectives
At the end of this project, I'am expected to be able to explain to anyone:

- Type annotations in Python 3
- How you can use type annotations to specify function signatures and variable types
- Duck typing
- How to validate your code with mypy

### 🎓 Purpose of Type Annotations

1. **Code Documentation:** Type annotations enhance code readability and serve as documentation. Developers can easily understand the expected types of variables, reducing bugs and exceptions.

2. **Linting and Validation:** Code editors and CI pipelines can validate type-annotated code at build-time, catching potential issues early in the development process.

## Example

```python
def add_numbers(a: int, b: int) -> int:
    return a + b
```

```python
# Function with type annotations
def multiply(a: float, b: float) -> float:
    return a * b

# Usage of the annotated function
result = multiply(3.5, 2)
print(result)  # Output: 7.0
```

In the above example, the function `add_numbers` takes two parameters (`a` and `b`) of type `int` and returns an `int`. The `multiply`function uses float types. This helps developers understand the function's intended usage.

##  🙇 Author

[Vladimir Davidov](https://github.com/v-dav) - Holberton School
