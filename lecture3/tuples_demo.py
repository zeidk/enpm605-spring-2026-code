"""
ENPM605 - Python Applications for Robotics
Lecture 3: Python Fundamentals — Part II
Spring 2026 | University of Maryland

Section: Tuples
"""

# ============================================================
# Tuple Basics
# ============================================================

# ──────────────────────────────────────────────
# 📌 Snippet 41 — Tuple Basics
# ──────────────────────────────────────────────
# Creating tuples
coordinates = (3.5, 7.2)
rgb = (255, 128, 0)
mixed = (1, "hello", [1, 2])  # Can contain mutable objects

# Important: commas make the tuple, not parentheses!
single = 42,3   # Tuple with one element
not_tuple = (42) # Just an integer!

print(type(single))     # <class 'tuple'>
print(type(not_tuple))  # <class 'int'>


# # ============================================================
# # Creating Tuples
# # ============================================================

# # ──────────────────────────────────────────────
# # 📌 Snippets 42-44 — Ways to Create Tuples
# # ──────────────────────────────────────────────
# # Parentheses (optional but recommended)
# point = (3, 4)
# empty = ()

# # Comma-separated values (tuple packing)
# point = 3, 4           # Same as (3, 4)
# singleton = 42,        # Tuple with one element

# # tuple() constructor
# from_list = tuple([1, 2, 3])    # (1, 2, 3)
# from_string = tuple("abc")      # ('a', 'b', 'c')
# from_range = tuple(range(3))    # (0, 1, 2)

# print(from_list)
# print(from_string)
# print(from_range)


# # ============================================================
# # Tuple Unpacking
# # ============================================================

# # ──────────────────────────────────────────────
# # 📌 Snippet 45 — Basic Tuple Unpacking
# # ──────────────────────────────────────────────
# # Basic unpacking
# coordinates = (3.5, 7.2)
# x, y = coordinates
# print(f"x={x}, y={y}")  # x=3.5, y=7.2

# # Swap values elegantly
# a, b = 10, 20
# print(f"Before swap: a={a}, b={b}")
# a, b = b, a  # Now a=20, b=10
# print(f"After swap: a={a}, b={b}")

# # Ignore values with underscore
# point = (1, 2, 3)
# x, _, z = point  # Ignore the y-coordinate
# print(f"x={x}, z={z}")

# # Extended unpacking with *
# first, *rest = [1, 2, 3, 4, 5]
# print(first)  # 1
# print(rest)   # [2, 3, 4, 5]

# # * can be in the middle too
# first, *middle, last = [1, 2, 3, 4, 5]
# print(first)   # 1
# print(middle)  # [2, 3, 4]
# print(last)    # 5


# # ============================================================
# # Tuple Immutability
# # ============================================================

# # ──────────────────────────────────────────────
# # 📌 Snippet 46 — Tuples Are Immutable
# # ──────────────────────────────────────────────
# point = (3, 4, 5)

# # These will raise TypeError:
# # point[0] = 10    # TypeError: 'tuple' object does not support item assignment
# # del point[1]     # TypeError: 'tuple' object doesn't support item deletion

# # However, mutable objects inside tuples CAN be modified!
# data = (1, 2, [3, 4])
# data[2].append(5)     # OK!
# print(data)           # (1, 2, [3, 4, 5])

# # But you cannot replace the list itself
# # data[2] = [10, 20]  # TypeError!

