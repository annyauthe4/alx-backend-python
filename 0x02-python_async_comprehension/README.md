# Async Comprehension in Python

This project demonstrates how to use **asynchronous comprehensions** in Python — a concise and efficient way to collect values from asynchronous iterators, such as async generators.

## 📘 What is Async Comprehension?

Async comprehensions combine the power of asynchronous iteration (`async for`) with Python’s comprehension syntax (like list/set/dict comprehensions).

```python
[expression async for item in async_iterable if condition]
