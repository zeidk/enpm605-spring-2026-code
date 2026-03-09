"""
Course: ENPM605
Lecture: OOP Part 2

Author: zeidk
Created: 2026-03-06
"""

from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable


# ──────────────────────────────────────────────
# Snippet 2️⃣6️⃣: Defining and Using a Protocol
# ──────────────────────────────────────────────
class Executable(Protocol):
    def execute(self, robot_name: str) -> bool: ...


# Neither class inherits from Executable
class PickTask:
    def execute(self, robot_name: str) -> bool:
        print(f"{robot_name} picks an object")
        return True


class NavigateTask:
    def execute(self, robot_name: str) -> bool:
        print(f"{robot_name} navigates to destination")
        return True


class SleepTask:
    def sleep(self, duration: float) -> None:
        print("sleeping")  # wrong method -- does not satisfy Executable


def dispatch(task: Executable, robot_name: str) -> bool:
    return task.execute(robot_name)


if __name__ == "__main__":
    dispatch(PickTask(), "Scout")  # OK
    dispatch(NavigateTask(), "Hauler")  # OK
    # dispatch(SleepTask(), "Scout")    # mypy error: SleepTask does not satisfy Executable


# # ──────────────────────────────────────────────
# # Snippet 2️⃣7️⃣: Runtime Checkable Protocols
# # ──────────────────────────────────────────────
# @runtime_checkable
# class Executable(Protocol):
#     def execute(self, robot_name: str) -> bool: ...


# class PickTask:
#     def execute(self, robot_name: str) -> bool:
#         print(f"{robot_name} picks an object")
#         return True


# class SleepTask:
#     def sleep(self, duration: float) -> None:
#         pass


# if __name__ == "__main__":
#     pick = PickTask()
#     sleep = SleepTask()

#     print(isinstance(pick, Executable))  # True
#     print(isinstance(sleep, Executable))  # False


# # ──────────────────────────────────────────────
# # Snippet 2️⃣7️⃣: Protocols vs. ABCs -- When to Use Which
# # ──────────────────────────────────────────────


# # ABC: shared base behavior + enforced interface
# class Sensor(ABC):
#     def __init__(self, name: str):
#         self._name = name  # shared concrete state

#     @abstractmethod
#     def read(self) -> float: ...


# # Protocol: pure interface, no shared behavior
# class Readable(Protocol):
#     def read(self) -> float: ...


# # Any class with read() satisfies Readable -- including third-party classes
# # Only Sensor subclasses satisfy isinstance(x, Sensor)
