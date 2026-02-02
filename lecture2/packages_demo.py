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

# result = compute_area(4)
# print(f"Approach 3 — compute_area(4) = {result}")


# # ──────────────────────────────────────────────
# # 📌 Snippet 5 — Approach 4: Wildcard (avoid)
# # ──────────────────────────────────────────────
# # from shape.square import *  # Namespace pollution risk!


# # ──────────────────────────────────────────────
# # 📌 Snippet 6 — Namespace Pollution Demo
# # ──────────────────────────────────────────────
# from shape.square import compute_area as square_area
# from shape.circle import compute_area as circle_area

# print(f"\nsquare_area(4) = {square_area(4)}")
# print(f"circle_area(4) = {circle_area(4):.4f}")

# # Without aliases, the second import silently overwrites the first:
# # from shape.square import *    # brings in compute_area, compute_perimeter
# # from shape.circle import *    # also brings in compute_area, compute_perimeter
# # result = compute_area(4)      # Which version is this? circle!


# # ──────────────────────────────────────────────
# # 📌 Snippet 7 — The __name__ Guard
# # ──────────────────────────────────────────────
# # This pattern is demonstrated in shape/triangle.py.
# # When a module is run directly, __name__ == "__main__".
# # When imported, __name__ is set to the module's name.

# import math


# def compute_triangle_area(base: float, height: float) -> float:
#     return 0.5 * base * height


# def compute_triangle_perimeter(side1: float, side2: float, side3: float) -> float:
#     return side1 + side2 + side3


# if __name__ == "__main__":
#     # Only runs when executed directly, not when imported
#     print(f"\nTriangle area (4.5, 5.6) = {compute_triangle_area(4.5, 5.6)}")
#     print(f"Triangle area (4.7, 6.0) = {compute_triangle_area(4.7, 6.0)}")
#     print(f"Triangle area (4.8, 7.1) = {compute_triangle_area(4.8, 7.1)}")
#     print(f"Triangle area (4.9, 8.45) = {compute_triangle_area(4.9, 8.45)}")