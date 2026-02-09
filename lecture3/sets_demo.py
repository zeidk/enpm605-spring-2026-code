"""
ENPM605 - Python Applications for Robotics
Lecture 3: Python Fundamentals — Part II
Spring 2026 | University of Maryland

Section: Sets
"""

# ============================================================
# Set Basics
# ============================================================

# ──────────────────────────────────────────────
# 📌 Snippet 61 — Set Basics
# ──────────────────────────────────────────────
# Sets automatically remove duplicates
numbers = {1, 2, 2, 3, 3, 3}
print(numbers)  # {1, 2, 3}

# Creating sets
fruits = {"apple", "banana", "cherry"}
from_list = set([1, 2, 2, 3])  # {1, 2, 3}
empty_set = set()  # NOT {} (that's an empty dict!)

print(fruits)
print(from_list)
print(type(empty_set))  # <class 'set'>
print(type({}))         # <class 'dict'>  -- be careful!


# # ============================================================
# # Mathematical Set Operations
# # ============================================================

# # ──────────────────────────────────────────────
# # 📌 Snippet 62 — Set Operations
# # ──────────────────────────────────────────────
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}

# # Union: elements in either set
# print(a | b)              # {1, 2, 3, 4, 5, 6}
# print(a.union(b))         # Same result

# # Intersection: elements in both sets
# print(a & b)              # {3, 4}
# print(a.intersection(b))  # Same result

# # Difference: elements in a but not in b
# print(a - b)              # {1, 2}
# print(a.difference(b))    # Same result

# # Symmetric difference: elements in either but not both
# print(a ^ b)                      # {1, 2, 5, 6}
# print(a.symmetric_difference(b))  # Same result


# # ──────────────────────────────────────────────
# # 📌 Snippet 63 — Adding Elements
# # ──────────────────────────────────────────────
# s = {1, 2, 3}

# # Add single element
# s.add(4)      # {1, 2, 3, 4}

# # Add multiple elements
# s.update([5, 6])  # {1, 2, 3, 4, 5, 6}
# s.update({7}, [8])  # Mix iterables

# # ──────────────────────────────────────────────
# # 📌 Snippet 64 — Removing Elements
# # ──────────────────────────────────────────────
# s = {1, 2, 3, 4, 5}

# # Remove (raises KeyError if missing)
# s.remove(3)    # {1, 2, 4, 5}

# # Discard (no error if missing)
# s.discard(99)  # No error

# # Pop (remove arbitrary element)
# x = s.pop()    # Returns removed element

# # Clear all elements
# s.clear()      # set()



# # ============================================================
# # Practical Set Use Cases
# # ============================================================

# # ──────────────────────────────────────────────
# # 📌 Snippet 65 — Practical Set Examples
# # ──────────────────────────────────────────────
# # Remove duplicates from a list
# readings = [1.5, 2.3, 1.5, 3.7, 2.3, 1.5]
# unique_readings = list(set(readings))
# print(unique_readings)  # [1.5, 2.3, 3.7] (order may vary)

# # Fast membership testing
# valid_commands = {"start", "stop", "pause", "reset"}
# user_input = "stop"
# if user_input in valid_commands:
#     print(f"Executing: {user_input}")

# # Find common elements between lists
# sensor_1_detections = ["obstacle", "wall", "person", "robot"]
# sensor_2_detections = ["wall", "person", "door"]
# common = set(sensor_1_detections) & set(sensor_2_detections)
# print(f"Both sensors detected: {common}")  # {'wall', 'person'}


# # ──────────────────────────────────────────────
# # 📌 Snippet 66 — Set Comprehensions
# # ──────────────────────────────────────────────
# Basic set comprehension
squares = {x**2 for x in range(5)}
print(squares)  # {0, 1, 4, 9, 16}

# With condition
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(even_squares)  # {0, 4, 16, 36, 64}

# Extract unique first letters
words = ["apple", "apricot", "banana", "blueberry", "cherry"]
first_letters = {word[0] for word in words}
print(first_letters)  # {'a', 'b', 'c'}
