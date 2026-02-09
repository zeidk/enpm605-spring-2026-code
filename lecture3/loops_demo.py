"""
ENPM605 - Python Applications for Robotics
Lecture 3: Python Fundamentals — Part II
Spring 2026 | University of Maryland

Section: Loops
"""

import sys

# ============================================================
# The range() Function
# ============================================================

# # ──────────────────────────────────────────────
# # 📌 Snippet 1 — range() Basics
# # ──────────────────────────────────────────────
# # range() returns a range object, not a list
# r = range(5)
# print(r)        # range(0, 5)
# print(type(r))  # <class 'range'>

# # Convert to list to see all values
# print(list(range(5)))  # [0, 1, 2, 3, 4]


# # ──────────────────────────────────────────────
# # 📌 Snippet 2 — range() with start, stop, step
# # ──────────────────────────────────────────────
# # range(stop) - generates 0 to stop-1
# print(list(range(5)))       # [0, 1, 2, 3, 4]

# # range(start, stop) - generates start to stop-1
# print(list(range(2, 7)))    # [2, 3, 4, 5, 6]

# # range(start, stop, step) - with custom increment
# print(list(range(0, 10, 2)))  # [0, 2, 4, 6, 8]
# print(list(range(1, 10, 2)))  # [1, 3, 5, 7, 9]

# # Negative step - counting backwards
# print(list(range(5, 0, -1)))  # [5, 4, 3, 2, 1]
# print(list(range(10, 0, -2))) # [10, 8, 6, 4, 2]


# # ──────────────────────────────────────────────
# # 📌 Snippet 3 — range() Indexing, Slicing, Membership
# # ──────────────────────────────────────────────
# # Get the length of a range without converting to list
# r = range(0, 1_000_000)
# print(len(r))           # 1000000 (instant, no memory used!)

# # Check membership efficiently - O(1) constant time!
# print(500_000 in r)      # True (very fast!)
# print(999_999 in r)      # True
# print(1_000_000 in r)     # False (stop value not included)

# # Indexing works on range objects
# r = range(10, 20)
# print(r[0])             # 10 (first element)
# print(r[-1])            # 19 (last element)
# print(r[5])             # 15

# # Slicing returns a new range object
# print(r[2:5])           # range(12, 15)
# print(list(r[2:5]))     # [12, 13, 14]


# # ──────────────────────────────────────────────
# # 📌 Snippet 4 — range() Common Patterns
# # ──────────────────────────────────────────────
# # Generate even numbers from 0 to 20
# evens = list(range(0, 21, 2))
# print(evens)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# # Generate odd numbers from 1 to 19
# odds = list(range(1, 20, 2))
# print(odds)   # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# # Countdown from 10 to 1
# countdown = list(range(10, 0, -1))
# print(countdown)  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# # Multiples of 5 from 5 to 50
# multiples = list(range(5, 51, 5))
# print(multiples)  # [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

# # Reverse a range using reversed()
# print(list(reversed(range(1, 6))))  # [5, 4, 3, 2, 1]


# # ──────────────────────────────────────────────
# # 📌 Snippet 5 — range() Memory Efficiency
# # ──────────────────────────────────────────────
# # A list stores all values in memory
# big_list = list(range(1_000_000))
# print(sys.getsizeof(big_list))  # ~8,000,056 bytes (8 MB)

# # A range object only stores start, stop, step
# big_range = range(1_000_000)
# print(sys.getsizeof(big_range))  # 48 bytes (always!)

# # Even a massive range uses the same tiny amount of memory
# huge_range = range(1_000_000_000_000)  # One trillion!
# print(sys.getsizeof(huge_range))   # Still just 48 bytes

# # ──────────────────────────────────────────────
# # 📌 Snippet 6 — Inside the 48-byte object
# # ──────────────────────────────────────────────
# r = range(10, 100, 3)  # start=10, stop=100, step=3
# # Accessing index 5: value = 10 + (5 * 3) = 25
# print(r[5])   # 25  <-- No iteration needed!
# print(r[20])  # 70  <-- Instant, same speed as r[0]

# # ──────────────────────────────────────────────
# # 📌 Snippet 7 — range() Edge Cases
# # ──────────────────────────────────────────────
# # Empty ranges (when start >= stop with positive step)
# print(list(range(5, 5)))      # []
# print(list(range(10, 5)))     # []
# print(list(range(5, 10, -1))) # [] (can't go up with negative step)

# # Range equality - two ranges are equal if they produce same sequence
# print(range(0, 10, 2) == range(0, 10, 2))  # True
# print(range(0, 10, 2) == range(0, 11, 2))  # False [0, 2, 4, 6, 8] != [0, 2, 4, 6, 8, 10]
# print(range(0) == range(5, 5))             # True (both empty)

# # Negative numbers work too
# print(list(range(-5, 0)))      # [-5, -4, -3, -2, -1]
# print(list(range(-10, -5)))    # [-10, -9, -8, -7, -6]
# print(list(range(0, -5, -1)))  # [0, -1, -2, -3, -4]


# # ============================================================
# # The for Loop
# # ============================================================

# # ──────────────────────────────────────────────
# # 📌 Snippet 8 — Basic for Loop
# # ──────────────────────────────────────────────
# # Iterate over a string
# message = "Hello"
# for char in message:
#     print(char, end=" ")  # H e l l o

# print()  # Newline

# # Iterate over a range
# for i in range(5):
#     print(i, end=" ")  # 0 1 2 3 4

# print()

# # Using range for repetition
# for _ in range(3):  # _ indicates we don't need the value
#     print("Robot activated!")


# # ──────────────────────────────────────────────
# # 📌 Snippet 9 — for Loop with Strings and range()
# # ──────────────────────────────────────────────
# message = "Python"

# # Access characters by index
# for i in range(len(message)):
#     print(f"Index {i}: {message[i]}")
# # Index 0: P
# # Index 1: y
# # ...

# # Print every other character
# for i in range(0, len(message), 2):
#     print(message[i], end="")  # Pto

# print()

# # Print string in reverse using range
# for i in range(len(message) - 1, -1, -1):
#     print(message[i], end="")  # nohtyP


# # ──────────────────────────────────────────────
# # 📌 Snippet 10 — The enumerate() Function
# # ──────────────────────────────────────────────
# message = "Robot"

# # Less Pythonic way
# for i in range(len(message)):
#     print(f"{i}: {message[i]}")

# # More Pythonic way with enumerate()
# for index, char in enumerate(message):
#     print(f"{index}: {char}")

# # Start counting from 1 instead of 0
# for index, char in enumerate(message, start=1):
#     print(f"Character {index}: {char}")
# # Character 1: R
# # Character 2: o
# # ...


# # ============================================================
# # The while Loop
# # ============================================================

# # ──────────────────────────────────────────────
# # 📌 Snippet 11 — Basic while Loop
# # ──────────────────────────────────────────────
# # Basic while loop - counting
# count = 0
# while count < 5:
#     print(count, end=" ")
#     count += 1  # Don't forget to update!
# # Output: 0 1 2 3 4

# print()

# # Building a string character by character
# result = ""
# i = 0
# word = "Hello"
# while i < len(word):
#     result += word[i].upper()
#     i += 1
# print(result)  # HELLO


# # ──────────────────────────────────────────────
# # 📌 Snippet 12 — while Loop Patterns
# # ──────────────────────────────────────────────
# # Countdown
# n = 5
# while n > 0:
#     print(n, end=" ")
#     n -= 1
# print("Liftoff!")  # 5 4 3 2 1 Liftoff!

# # Summing with a counter
# total = 0
# count = 0
# while count < 5:
#     total += count
#     count += 1
# print(f"Sum of 0-4: {total}")  # Sum of 0-4: 10

# # Processing until a condition
# text = "Hello World"
# i = 0
# while i < len(text) and text[i] != ' ':
#     print(text[i], end="")
#     i += 1
# # Output: Hello


# # ============================================================
# # Loop Control Statements
# # ============================================================

# # ──────────────────────────────────────────────
# # 📌 Snippet 13 — break Statement
# # ──────────────────────────────────────────────
# # Find first vowel in a string
# word = "python"
# for char in word:
#     if char in "aeiou":
#         print(f"First vowel: {char}")
#         break
# # Output: First vowel: o


# # ──────────────────────────────────────────────
# # 📌 Snippet 14 — continue Statement
# # ──────────────────────────────────────────────
# # Print only consonants
# word = "hello"
# for char in word:
#     if char in "aeiou":
#         continue
#     print(char, end=" ")
# # Output: h l l
# print()


# # ──────────────────────────────────────────────
# # 📌 Snippet 15 — else Clause on Loops
# # ──────────────────────────────────────────────
# # Search for a character
# word = "robot"
# target = "x"

# for char in word:
#     if char == target:
#         print(f"Found {target}!")
#         break
# else:
#     print(f"{target} not found")
# # Output: x not found

# # Compare with a successful search
# target = "o"
# for char in word:
#     if char == target:
#         print(f"Found {target}!")
#         break
# else:
#     print(f"{target} not found")
# # Output: Found o!


# # ──────────────────────────────────────────────
# # 📌 Snippet 16 — Practical Loop Examples
# # ──────────────────────────────────────────────
# # Count vowels in a string
# text = "University of Maryland"
# vowel_count = 0
# for char in text.lower():
#     if char in "aeiou":
#         vowel_count += 1
# print(f"Vowels: {vowel_count}")  # Vowels: 7

# # Create a pattern using range
# for i in range(1, 6):
#     print("*" * i)
# # *
# # **
# # ***
# # ****
# # *****

# # Sum of numbers from 1 to 100
# total = 0
# for num in range(1, 101):
#     total += num
# print(f"Sum 1-100: {total}")  # Sum 1-100: 5050
