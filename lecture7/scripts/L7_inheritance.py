"""
Course: ENPM605
Lecture: OOP Part 2

Author: zeidk
Created: 2026-03-06
"""


# ──────────────────────────────────────────────
# Snippet 7️⃣: Inheritance -- UML to Python
# ──────────────────────────────────────────────
class Animal:
    def __init__(self, name: str, age: int, weight: float):
        self._name = name
        self._age = age
        self._weight = weight

    # @property for the getters

    def eat(self) -> None: ...
    def sleep(self) -> None: ...
    def make_sound(self) -> None: ...
    def move(self) -> None: ...


class Dog(Animal):
    def __init__(self, name: str, age: int, weight: float, breed: str):
        super().__init__(name, age, weight)
        self._breed = breed

    @property
    def breed(self) -> str:
        return self._breed

    def fetch(self) -> None: ...


# # ──────────────────────────────────────────────
# # Snippet 8️⃣: Attribute Initialization with super()
# # ──────────────────────────────────────────────
# class Animal:
#     def __init__(self, name: str, age: int, weight: float):
#         self._name = name        # parent attribute -- initialized here
#         self._age = age          # parent attribute -- initialized here
#         self._weight = weight    # parent attribute -- initialized here


# class Cat(Animal):
#     def __init__(self, name: str, age: int, weight: float, indoor_only: bool = True):
#         super().__init__(name, age, weight)  # delegate to Animal
#         self._indoor_only = indoor_only      # child attribute -- initialized here


# class Dog(Animal):
#     def __init__(self, name: str, age: int, weight: float, breed: str = "unknown"):
#         super().__init__(name, age, weight)  # delegate to Animal
#         self._breed = breed                  # child attribute -- initialized here


# if __name__ == "__main__":
#     kitty = Cat("Kitty", age=3, weight=4.2)
#     rex   = Dog("Rex",   age=5, weight=30.0, breed="Labrador")


# # ──────────────────────────────────────────────
# # Snippet 9️⃣: Method Resolution Order (MRO)
# # ──────────────────────────────────────────────
# class Animal:
#     pass


# class Dog(Animal):
#     pass


# if __name__ == "__main__":
#     print(Dog.__mro__)
#     # (<class 'Dog'>, <class 'Animal'>, <class 'object'>)


# # ──────────────────────────────────────────────
# # Snippet 1️⃣0️⃣: isinstance() and issubclass()
# # ──────────────────────────────────────────────
# class Animal:
#     pass


# class Cat(Animal):
#     pass


# class Dog(Animal):
#     pass


# if __name__ == "__main__":
#     kitty = Cat()
#     rex = Dog()

#     # isinstance: is this object an instance of the class (or any subclass)?
#     print(isinstance(kitty, Cat))  # True
#     print(isinstance(kitty, Animal))  # True  -- Cat IS-A Animal
#     print(isinstance(kitty, Dog))  # False -- unrelated subclass

#     # issubclass: is this class a subclass of another?
#     print(issubclass(Cat, Animal))  # True
#     print(issubclass(Dog, Animal))  # True
#     print(issubclass(Animal, Cat))  # False -- parent is not a subclass of child
