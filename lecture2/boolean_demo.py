"""
ENPM605 - Python Applications for Robotics
Lecture 2: Python Fundamentals — Part I
Spring 2026 | University of Maryland

Section: Boolean Type
"""

# ──────────────────────────────────────────────
# 📌 Snippet 15 — Falsy Values
# ──────────────────────────────────────────────
print(bool(0))       # False
print(bool(0.0))     # False
print(bool(""))      # False
print(bool([]))      # False
print(bool({}))      # False
print(bool(None))    # False


# # ──────────────────────────────────────────────
# # 📌 Snippet 16 — Truthy Values
# # ──────────────────────────────────────────────
# print(bool(1))       # True
# print(bool(-2))      # True
# print(bool("hi"))    # True
# print(bool([1, 2]))  # True
# print(bool(" "))     # True (space!)
# print(bool(0.001))   # True

# # Pythonic idiom: Use truthiness directly in conditions
# my_list = [1, 2, 3]
# if my_list:  # Instead of: if len(my_list) > 0
#     print("List is not empty (Pythonic style)")