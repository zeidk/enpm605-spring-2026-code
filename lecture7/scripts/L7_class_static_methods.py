"""
Course: ENPM605
Lecture: OOP Part 2

Author: zeidk
Created: 2026-03-06
"""

import time
import sys


# ──────────────────────────────────────────────
# Snippet 1️⃣: Class Methods -- Factory Methods
# ──────────────────────────────────────────────
class Robot:
    def __init__(self, name: str, battery: int = 100):
        self._name = name
        self._battery = battery

    def __repr__(self) -> str:
        return f"Robot(name={self._name!r}, battery={self._battery}%)"

    @classmethod
    def create_scout(cls) -> "Robot":
        """Factory: create a lightweight scout robot."""
        return cls("Scout", 100)

    @classmethod
    def create_scout_team(cls, count: int = 3) -> list["Robot"]:
        """Factory: create a team of scouts."""
        return [cls(f"Scout-{i + 1}", 100) for i in range(count)]


if __name__ == "__main__":
    scout = Robot.create_scout()
    team  = Robot.create_scout_team(4)
    print(scout)   # Robot(name='Scout', battery=100%)
    print(team)


# # ──────────────────────────────────────────────
# # Snippet 2️⃣: Static Methods -- Validation and Formatting
# # ──────────────────────────────────────────────
# class Robot:
#     def __init__(self, name: str, battery: int = 100):
#         self._name = name
#         self._battery = battery

#     @staticmethod
#     def is_valid_name(name: str) -> bool:
#         """Check if a robot name follows the naming convention."""
#         return isinstance(name, str) and len(name) > 0

#     @staticmethod
#     def battery_to_bar(level: int) -> str:
#         """Convert a battery level to a visual bar."""
#         bars = level // 10
#         return "[" + "#" * bars + "." * (10 - bars) + "]"


# if __name__ == "__main__":
#     print(Robot.is_valid_name("Scout"))  # True
#     print(Robot.battery_to_bar(70))      # [#######...]


# # ──────────────────────────────────────────────
# # Snippet 2️⃣🅱️: Static Methods -- Fancier charging animation
# # ──────────────────────────────────────────────
# class Robot:
#     def __init__(self, name: str, battery: int = 0):
#         self._name = name
#         self._battery = battery

#     @staticmethod
#     def battery_to_bar(level: int) -> str:
#         """Convert a battery level to a visual bar using block characters."""
#         bars = level // 10
#         return "[" + "\U0001f7e9" * bars + "\u2b1c" * (10 - bars) + "]"

#     def charge(self, target: int, delay: float = 0.3) -> None:
#         """Animate battery charging from current level to target."""
#         for level in range(self._battery, target + 1, 10):
#             bar = Robot.battery_to_bar(level)
#             sys.stdout.write(f"\r{self._name} charging... {bar} {level:3d}%")
#             sys.stdout.flush()
#             time.sleep(delay)
#         self._battery = target
#         print()


# if __name__ == "__main__":
#     scout = Robot("Scout", battery=20)
#     scout.charge(100, delay=0.3)


# # ──────────────────────────────────────────────
# # Snippet 3️⃣: Class vs. Static Methods -- Side-by-Side Comparison
# # ──────────────────────────────────────────────
# class Robot:
#     total_robots = 0

#     def __init__(self, name: str, battery: int = 100):
#         self._name = name
#         self._battery = battery
#         Robot.total_robots += 1

#     def status(self) -> str:
#         return f"{self._name}: {self._battery}%"

#     @classmethod
#     def get_fleet_size(cls) -> str:
#         return f"Fleet size: {cls.total_robots}"

#     @staticmethod
#     def is_valid_battery(level: int) -> bool:
#         return isinstance(level, int) and 0 <= level <= 100


# if __name__ == "__main__":
#     scout = Robot("Scout")
#     print(scout.status())              # Scout: 100%
#     print(Robot.get_fleet_size())      # Fleet size: 1
#     print(Robot.is_valid_battery(50))  # True