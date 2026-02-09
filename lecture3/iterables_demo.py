"""
ENPM605 - Python Applications for Robotics
Lecture 3: Python Fundamentals — Part II
Spring 2026 | University of Maryland

Section: Iterables
"""

# ============================================================
# What Are Iterables?
# ============================================================

# # ──────────────────────────────────────────────
# # 📌 Snippet 18 — Iterable Types
# # ──────────────────────────────────────────────
# # Strings are iterable
# for char in "Hi":
#     print(char, end=" ")  # H i
# print()

# # Ranges are iterable
# for num in range(3):
#     print(num, end=" ")  # 0 1 2
# print()

# # Lists are iterable
# for item in [1, 2, 3]:
#     print(item, end=" ")  # 1 2 3
# print()

# # Dictionaries are iterable (iterates over keys)
# for key in {"a": 1, "b": 2}:
#     print(key, end=" ")  # a b
# print()


# # ============================================================
# # In-Place vs Out-of-Place Operations
# # ============================================================

# # ──────────────────────────────────────────────
# # 📌 Snippet 19 — In-Place Operations
# # ──────────────────────────────────────────────
# # In-place operations modify the original object
# # and typically return None

# fruits = ["apple", "banana"]
# result = fruits.append("kiwi")
# print(f"append() returned: {result}")  # None
# print(f"fruits is now: {fruits}")      # ['apple', 'banana', 'kiwi']

# # Common mistake: assigning the result of an in-place method
# numbers = [3, 1, 4, 1, 5]
# sorted_nums = numbers.sort()  # WRONG!
# print(f"sorted_nums: {sorted_nums}")  # None - not what you wanted!
# print(f"numbers: {numbers}")          # [1, 1, 3, 4, 5] - original modified


# # ──────────────────────────────────────────────
# # 📌 Snippet 20 — Out-of-Place Operations
# # ──────────────────────────────────────────────
# # Out-of-place operations return a new object
# # and leave the original unchanged

# text = "hello"
# upper_text = text.upper()
# print(f"Original: {text}")        # hello (unchanged)
# print(f"New: {upper_text}")       # HELLO

# # sorted() is out-of-place (compare to list.sort())
# numbers = [3, 1, 4, 1, 5]
# sorted_nums = sorted(numbers)     # CORRECT!
# print(f"sorted_nums: {sorted_nums}")  # [1, 1, 3, 4, 5]
# print(f"numbers: {numbers}")          # [3, 1, 4, 1, 5] - unchanged!
