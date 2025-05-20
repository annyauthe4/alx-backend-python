# Access Nested Map - Unit Testing Project

## 📋 Description

This project demonstrates how to write unit tests in Python for utility functions, specifically focusing on the `access_nested_map` function. The function allows retrieving values from nested dictionaries using a sequence of keys (a path).

Testing is implemented using the `unittest` framework, with the help of `parameterized` for running multiple test scenarios.

---

## 🧪 Features

- Unit testing with `unittest`
- Multiple test scenarios using `parameterized.expand`
- Organized, clean, and concise test cases

---

## 🧰 Function: `access_nested_map`

### 🔹 Purpose

Access values in a nested map (dictionary) using a tuple path.

### 🔹 Example Usage

```python
from utils import access_nested_map

result = access_nested_map({"a": {"b": 2}}, ("a", "b"))
print(result)  # Output: 2

<h1> Running the Tests</h1>
<ol>
    <li> Make sure you have parameterized installed: <code> pip install parameterized</code>
    <li> Run the tests using unittest: <code>python3 -m unittest test_utils.py</code>
</ol>

AUTHOR:Otetumo Oluwaseun
