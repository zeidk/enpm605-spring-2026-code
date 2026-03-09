"""
Course: ENPM605
Lecture: OOP Part 2

Author: zeidk
Created: 2026-03-06
"""


# ──────────────────────────────────────────────
# Snippet 1️⃣1️⃣: Duck Typing
# ──────────────────────────────────────────────
class Animal:
    def __init__(self, name: str):
        self._name = name


class Cat(Animal):
    def make_sound(self) -> None:
        print(f"{self._name} says: Meow")


class Dog(Animal):
    def make_sound(self) -> None:
        print(f"{self._name} says: Woof")


def chorus(animals: list[Animal]) -> None:
    for animal in animals:
        animal.make_sound()   # polymorphic call


if __name__ == "__main__":
    chorus([Cat("Kitty"), Dog("Rex")])
    # Kitty says: Meow
    # Rex says: Woof


# # ──────────────────────────────────────────────
# # Snippet 1️⃣2️⃣: Built-in Polymorphism
# # ──────────────────────────────────────────────
# if __name__ == "__main__":
#     # len() calls __len__ on whatever object it receives
#     print(len("hello"))         # 5    (str.__len__)
#     print(len([1, 2, 3]))       # 3    (list.__len__)
#     print(len({"a": 1}))        # 1    (dict.__len__)

#     # str() calls __str__ on whatever object it receives
#     print(str(42))              # '42'
#     print(str(3.14))            # '3.14'
#     print(str(True))            # 'True'

#     # + calls __add__ on whatever object it receives
#     print(1 + 2)                # 3
#     print("hello" + " world")   # hello world
#     print([1, 2] + [3, 4])      # [1, 2, 3, 4]


# # ──────────────────────────────────────────────
# # Snippet 1️⃣3️⃣: Operator Overriding
# # ──────────────────────────────────────────────
# class Animal:
#     def __init__(self, name: str, age: int, weight: float):
#         self._name = name
#         self._age = age
#         self._weight = weight

#     def __repr__(self) -> str:
#         return f"Animal(name={self._name!r}, age={self._age}, weight={self._weight} kg)"

#     def __eq__(self, other: object) -> bool:
#         if not isinstance(other, Animal):
#             return NotImplemented
#         return self._name == other._name and self._age == other._age

#     def __add__(self, other: "Animal") -> float:
#         return self._weight + other._weight  # combined weight


# if __name__ == "__main__":
#     kitty = Animal("Kitty", age=3, weight=4.2)
#     rex   = Animal("Rex",   age=5, weight=30.0)

#     print(kitty == rex)    # False
#     print(kitty + rex)     # 34.2  (combined weight)