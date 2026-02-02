"""
ENPM605 - Python Applications for Robotics
Lecture 2: Python Fundamentals — Part I
Spring 2026 | University of Maryland

Section: Indentation
"""

# ──────────────────────────────────────────────
# 📌 Snippet 8 — Indentation Defines Code Blocks
# ──────────────────────────────────────────────
# Unlike C++ or Java which use braces {},
# Python uses indentation to define blocks of code.


def greeting(name):
    print("Hello", name)
    if name == "Alice":
        print("Welcome back!")


greeting("Alice")
greeting("Bob")