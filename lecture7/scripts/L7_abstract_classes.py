"""
Course: ENPM605
Lecture: OOP Part 2

Author: zeidk
Created: 2026-03-06
"""

from abc import ABC, abstractmethod


# ──────────────────────────────────────────────
# Snippet 1️⃣4️⃣: The abc Module and @abstractmethod
# ──────────────────────────────────────────────
class Animal(ABC):
    def __init__(self, name: str):
        self._name = name

    @abstractmethod
    def make_sound(self) -> None: ...

    @abstractmethod
    def move(self) -> None: ...


class Cat(Animal):
    def make_sound(self) -> None:
        print(f"{self._name} says: Meow")

    def move(self) -> None:
        print(f"{self._name} walks gracefully")


if __name__ == "__main__":
    kitty = Cat("Kitty")  # OK: all abstract methods implemented
    kitty.make_sound()  # Kitty says: Meow


# # ──────────────────────────────────────────────
# # Snippet 1️⃣5️⃣: ABCs, Polymorphism, and Method Overriding
# # ──────────────────────────────────────────────
# class Animal(ABC):
#     def __init__(self, name: str):
#         self._name = name

#     @abstractmethod
#     def make_sound(self) -> None: ...  # contract: every subclass must override this


# class Cat(Animal):
#     def make_sound(self) -> None:      # overriding the abstract method
#         print(f"{self._name} says: Meow")


# class Dog(Animal):
#     def make_sound(self) -> None:      # overriding the abstract method
#         print(f"{self._name} says: Woof")


# ──────────────────────────────────────────────
# Snippet 1️⃣6️⃣: What Happens When You Forget
# ──────────────────────────────────────────────
# class Animal(ABC):
#     def __init__(self, name: str):
#         self._name = name

#     @abstractmethod
#     def make_sound(self) -> None: ...


# class Cat(Animal):
#     def make_sound(self) -> None:
#         print(f"{self._name} says: Meow")


# class Dog(Animal):
#     def move(self) -> None:
#         print(f"{self._name} runs")

#     # make_sound() is NOT implemented -- forgot!


# if __name__ == "__main__":
#     kitty = Cat("Kitty")  # OK
#     rex = Dog("Rex")  # TypeError: Can't instantiate abstract class Dog
#     # without an implementation for abstract method 'make_sound'


# # ──────────────────────────────────────────────
# # Snippet 1️⃣7️⃣: Practical Example -- Abstract and Concrete Together
# # ──────────────────────────────────────────────
# class Animal(ABC):
#     def __init__(self, name: str, age: int):
#         self._name = name
#         self._age = age

#     @abstractmethod
#     def make_sound(self) -> None: ...

#     @abstractmethod
#     def move(self) -> None: ...

#     # concrete: shared by all
#     def eat(self) -> None:
#         print(f"{self._name} is eating")

#     # concrete: shared by all
#     def __repr__(self) -> str:
#         return f"{type(self).__name__}(name={self._name!r}, age={self._age})"


# class Cat(Animal):
#     def make_sound(self) -> None:
#         print(f"{self._name} says: Meow")

#     def move(self) -> None:
#         print(f"{self._name} walks gracefully")


# if __name__ == "__main__":
#     kitty = Cat("Kitty", age=3)
#     kitty.eat()  # inherited from Animal
#     kitty.make_sound()  # overridden in Cat
#     kitty.move()  # overridden in Cat
#     print(kitty)  # Cat(name='Kitty', age=3)
