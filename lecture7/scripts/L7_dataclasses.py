"""
Course: ENPM605
Lecture: OOP Part 2

Author: zeidk
Created: 2026-03-06
"""

from dataclasses import dataclass, field
from enum import Enum, auto


# ──────────────────────────────────────────────
# Snippet 1️⃣8️⃣: @dataclass -- Definition and Motivation
# ──────────────────────────────────────────────
@dataclass
class Animal:
    name: str
    age: int
    weight: float


if __name__ == "__main__":
    kitty = Animal("Kitty", 3, 4.2)
    rex   = Animal("Rex",   5, 30.0)

    print(kitty)
    # Animal(name='Kitty', age=3, weight=4.2)

    print(kitty == Animal("Kitty", 3, 4.2))
    # True

    print(kitty == rex)
    # False


# # ──────────────────────────────────────────────
# # Snippet 1️⃣9️⃣: field() and Default Factories
# # ──────────────────────────────────────────────
# @dataclass
# class Animal:
#     name: str
#     age: int
#     weight: float
#     nicknames: list[str] = field(default_factory=list)
#     _id: int = field(default=0, repr=False, compare=False)


# if __name__ == "__main__":
#     kitty = Animal("Kitty", 3, 4.2)
#     kitty.nicknames.append("Kit")
#     print(kitty)
#     # Animal(name='Kitty', age=3, weight=4.2, nicknames=['Kit'])

#     rex = Animal("Rex", 5, 30.0)
#     print(rex.nicknames)   # []  (independent list)


# # ──────────────────────────────────────────────
# # Snippet 2️⃣0️⃣: __post_init__ -- Validation
# # ──────────────────────────────────────────────
# @dataclass
# class Animal:
#     name: str
#     age: int
#     weight: float

#     def __post_init__(self):
#         if self.age < 0:
#             raise ValueError(f"age cannot be negative: {self.age}")
#         if self.weight <= 0:
#             raise ValueError(f"weight must be positive: {self.weight}")


# if __name__ == "__main__":
#     kitty = Animal("Kitty", age=3, weight=4.2)  # OK
#     # bad = Animal("Bad", age=-1, weight=4.2)   # ValueError


# # ──────────────────────────────────────────────
# # Snippet 2️⃣1️⃣: __post_init__ -- Derived Attributes
# # ──────────────────────────────────────────────
# @dataclass
# class Animal:
#     name: str
#     age: int
#     life_stage: str = field(init=False)

#     def __post_init__(self):
#         if self.age < 1:
#             self.life_stage = "infant"
#         elif self.age < 7:
#             self.life_stage = "adult"
#         else:
#             self.life_stage = "senior"


# if __name__ == "__main__":
#     kitty = Animal("Kitty", age=3)
#     print(kitty)
#     # Animal(name='Kitty', age=3, life_stage='adult')


# # ──────────────────────────────────────────────
# # Snippet 2️⃣2️⃣: Frozen Data Classes
# # ──────────────────────────────────────────────
# @dataclass(frozen=True)
# class Animal:
#     name: str
#     age: int
#     weight: float


# if __name__ == "__main__":
#     kitty = Animal("Kitty", 3, 4.2)
#     print(kitty)
#     # Animal(name='Kitty', age=3, weight=4.2)

#     # kitty.age = 4
#     # FrozenInstanceError: cannot assign to field 'age'

#     # Frozen instances are hashable
#     animal_set = {kitty, Animal("Rex", 5, 30.0)}
#     lookup = {kitty: "indoor cat"}
#     print(lookup[kitty])   # indoor cat
