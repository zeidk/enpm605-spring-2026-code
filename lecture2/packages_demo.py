"""
ENPM605 - Python Applications for Robotics
Lecture 2: Python Fundamentals — Part I
Spring 2026 | University of Maryland

Section: Packages and Modules
"""

import sys
import os

# Add the parent directory to sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# ──────────────────────────────────────────────
# 📌 Snippet 1 — Making Packages Discoverable
# ──────────────────────────────────────────────
# (The sys.path setup above is Snippet 1)
# After this, imports from sibling packages work
# regardless of how the script is run.


# # ──────────────────────────────────────────────
# # 📌 Snippet 2 — Approach 1: Full module path
# # ──────────────────────────────────────────────
# import shape.square

# result = shape.square.compute_area(4)
# print(f"Approach 1 — shape.square.compute_area(4) = {result}")


# # ──────────────────────────────────────────────
# # 📌 Snippet 3 — Approach 2: Alias
# # ──────────────────────────────────────────────
# import shape.square as sq

# result = sq.compute_area(4)
# print(f"Approach 2 — sq.compute_area(4) = {result}")


# # ──────────────────────────────────────────────
# # 📌 Snippet 4 — Approach 3: Import specific names (recommended)
# # ──────────────────────────────────────────────
# from shape.square import compute_area, compute_perimeter

# print(f"Approach 3 — compute_area(4) = {compute_area(4)}")
# print(f"Approach 3 — compute_perimeter(3) = {compute_perimeter(3)}")


# # ──────────────────────────────────────────────
# # 📌 Snippet 5 — Approach 4: Wildcard (avoid)
# # ──────────────────────────────────────────────
# from shape.square import *  # Namespace pollution risk!

# print(f"Approach 4 — compute_area(4) = {compute_area(4)}")
# print(f"Approach 4 — compute_perimeter(3) = {compute_perimeter(3)}")

# # ──────────────────────────────────────────────
# # 📌 Snippet 6 — Namespace Pollution Demo
# # ──────────────────────────────────────────────
# from shape.square import compute_area as square_area
# from shape.circle import compute_area as circle_area

# print(f"\nsquare_area(4) = {square_area(4)}")
# print(f"circle_area(4) = {circle_area(4):.4f}")

# # Without aliases, the second import silently overwrites the first:
# from shape.square import *    # brings in compute_area, compute_perimeter
# from shape.circle import *    # also brings in compute_area, compute_perimeter
# result = compute_area(4)      # Which version is this? circle!
# print(result)


# # ──────────────────────────────────────────────
# # 📌 Method 1: PYTHONPATH Environment Variable
# # ──────────────────────────────────────────────
# from shape.square import compute_area

# print(compute_area(3))

# # ──────────────────────────────────────────────
# # 📌 Method 2: .pth Files
# # ──────────────────────────────────────────────
# from shape.square import compute_area

# print(compute_area(4))

# # ──────────────────────────────────────────────
# # 📌 Method 3: Editable Install pip3 install -e .
# # ──────────────────────────────────────────────
# from shape2.shape2.square import compute_area

# print(compute_area(4))

# # ──────────────────────────────────────────────
# # 📌 Snippet 10 — The __name__ Guard
# # ──────────────────────────────────────────────
# # This pattern is demonstrated in shape/triangle.py.
# # When a module is run directly, __name__ == "__main__".
# # When imported, __name__ is set to the module's name.

# from shape.triangle import compute_area

# print(compute_area(3,2))
