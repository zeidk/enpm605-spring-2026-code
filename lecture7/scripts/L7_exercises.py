"""
exercises.py
============
ENPM605 -- Lecture 7 Exercises

Starter file for all four take-home exercises.  Each exercise contains:
  - A header describing the goal and what to implement.
  - Provided code that must NOT be modified (marked with NOTE).
  - Stub classes and functions for you to complete (marked with TODO).
  - A pre-written __main__ block showing the expected output.

Run a single exercise:
    python exercises.py 1
    python exercises.py 2
    python exercises.py 3
    python exercises.py 4

Run all exercises:
    python exercises.py
"""

import sys


# ===========================================================================
# EXERCISE 1️⃣ -- Robot Hierarchy
# ===========================================================================
#
# Goal
# ----
# Practice single and hierarchical inheritance, super(), method overriding,
# and runtime type inspection with isinstance() and issubclass().
#
# What to implement
# -----------------
# The Robot base class is provided in full below -- do NOT modify it.
# You must implement:
#   - MobileRobot(Robot)
#   - ManipulatorRobot(Robot)
#
# Expected output
# ---------------
#   Scout moving north at up to 1.5 m/s
#   Scout performing: navigate to zone B
#   Arm-1 repositioning left
#   Arm-1 picking up: widget-42
#   Arm-1 delivering widget-42 to zone dropoff
#   MobileRobot(name='Scout', battery=90, max_speed=1.5)
#   ManipulatorRobot(name='Arm-1', battery=100, arm_reach=0.8)
#   True
#   True
#   False
#   True
#   True
# ===========================================================================


# NOTE: Robot is provided. Do NOT modify this class.
class Robot:
    """Base class for all robots in the competition arena.

    Args:
        name: Unique identifier for this robot.
        battery: Initial battery level (0-100). Defaults to 100.
    """

    def __init__(self, name: str, battery: int = 100) -> None:
        self._name: str = name
        self._battery: int = battery

    def perform_task(self, task_name: str) -> None:
        """Perform a named task, consuming 10 battery units.

        If battery is below 10 the task is refused and a recharge
        reminder is printed instead.

        Args:
            task_name: Human-readable description of the task.
        """
        if self._battery < 10:
            print(f"{self._name} needs recharging!")
            return
        print(f"{self._name} performing: {task_name}")
        self._battery -= 10

    def recharge(self) -> None:
        """Restore battery to 100 and print a confirmation message."""
        self._battery = 100
        print(f"{self._name} fully recharged!")

    def __repr__(self) -> str:
        """Return an unambiguous string representation.

        Returns:
            String of the form ``Robot(name='<n>', battery=<b>)``.
        """
        return f"Robot(name={self._name!r}, battery={self._battery})"


# TODO: Implement MobileRobot(Robot)
#
# __init__(self, name: str, max_speed: float, terrain_type: str,
#          battery: int = 100)
#   - Call super().__init__() then set _max_speed (float, m/s)
#     and _terrain_type (str).
#
# move(self, direction: str) -> None
#   - Print: "<n> moving <direction> at up to <max_speed> m/s"
#
# __repr__(self) -> str
#   - Return: "MobileRobot(name='<n>', battery=<b>, max_speed=<s>)"
#
# Every method must have type hints and a Google-style docstring.
class MobileRobot(Robot):
    pass


# TODO: Implement ManipulatorRobot(Robot)
#
# __init__(self, name: str, arm_reach: float, payload_capacity: float,
#          battery: int = 100)
#   - Call super().__init__() then set _arm_reach (float, m)
#     and _payload_capacity (float, kg).
#
# move(self, direction: str) -> None
#   - Print: "<n> repositioning <direction>"
#
# pick_up(self, obj: str) -> None
#   - Print: "<n> picking up: <obj>"
#
# deliver(self, obj: str, zone: str) -> None
#   - Print: "<n> delivering <obj> to zone <zone>"
#
# __repr__(self) -> str
#   - Return: "ManipulatorRobot(name='<n>', battery=<b>, arm_reach=<r>)"
#
# Every method must have type hints and a Google-style docstring.
class ManipulatorRobot(Robot):
    pass


def exercise1_main() -> None:
    scout = MobileRobot("Scout", max_speed=1.5, terrain_type="indoor")
    arm   = ManipulatorRobot("Arm-1", arm_reach=0.8, payload_capacity=2.0)

    scout.move("north")
    scout.perform_task("navigate to zone B")

    arm.move("left")
    arm.pick_up("widget-42")
    arm.deliver("widget-42", "dropoff")

    print(scout)
    print(arm)

    # isinstance checks
    print(isinstance(scout, MobileRobot))      # True
    print(isinstance(scout, Robot))             # True
    print(isinstance(scout, ManipulatorRobot))  # False

    # issubclass checks
    print(issubclass(MobileRobot, Robot))       # True
    print(issubclass(ManipulatorRobot, Robot))  # True


# # ===========================================================================
# # EXERCISE 2️⃣ -- Abstract Robot Interface
# # ===========================================================================
# #
# # Goal
# # ----
# # Practice defining abstract base classes with the abc module, enforcing
# # interface contracts with @abstractmethod, mixing abstract and concrete
# # methods, and verifying that Python raises TypeError on direct
# # instantiation of an abstract class.
# #
# # What to implement
# # -----------------
# #   - AbstractRobot(ABC)              -- abstract base class
# #   - MobileRobotABC(AbstractRobot)   -- concrete subclass
# #   - ManipulatorRobotABC(AbstractRobot) -- concrete subclass
# #
# # Note: classes are prefixed to avoid name collisions with Exercise 1.
# # In your standalone robot_abstract.py file simply name them
# # Robot, MobileRobot, and ManipulatorRobot.
# #
# # Expected output
# # ---------------
# #   TypeError: Can't instantiate abstract class AbstractRobot without an
# #              implementation for abstract method 'move'
# #   Scout moving north at up to 1.5 m/s
# #   Scout performing: navigate to zone B
# #   Arm-1 repositioning left
# #   Arm-1 performing: pick widget
# #   Arm-1 fully recharged!
# # ===========================================================================

# from abc import ABC, abstractmethod


# # TODO: Implement AbstractRobot(ABC)
# #
# # __init__(self, name: str, battery: int = 100)
# #   - Set _name and _battery.
# #
# # @abstractmethod move(self, direction: str) -> None
# #   - Every concrete subclass must implement this.
# #
# # perform_task(self, task_name: str) -> None  [concrete]
# #   - Print: "<n> performing: <task_name>" and decrease _battery by 10.
# #   - If _battery < 10, print: "<n> needs recharging!" and return early.
# #
# # recharge(self) -> None  [concrete]
# #   - Set _battery to 100.
# #   - Print: "<n> fully recharged!"
# #
# # Every method must have type hints and a Google-style docstring.
# class AbstractRobot(ABC):
#     pass


# # TODO: Implement MobileRobotABC(AbstractRobot)
# #
# # __init__(self, name: str, max_speed: float, terrain_type: str,
# #          battery: int = 100)
# #   - Call super().__init__() then set _max_speed and _terrain_type.
# #
# # move(self, direction: str) -> None
# #   - Print: "<n> moving <direction> at up to <max_speed> m/s"
# #
# # Every method must have type hints and a Google-style docstring.
# class MobileRobotABC(AbstractRobot):
#     pass


# # TODO: Implement ManipulatorRobotABC(AbstractRobot)
# #
# # __init__(self, name: str, arm_reach: float, payload_capacity: float,
# #          battery: int = 100)
# #   - Call super().__init__() then set _arm_reach and _payload_capacity.
# #
# # move(self, direction: str) -> None
# #   - Print: "<n> repositioning <direction>"
# #
# # Every method must have type hints and a Google-style docstring.
# class ManipulatorRobotABC(AbstractRobot):
#     pass


# def exercise2_main() -> None:
#     # Confirm AbstractRobot cannot be instantiated directly
#     try:
#         r = AbstractRobot("Base")  # type: ignore[abstract]
#     except TypeError as e:
#         print(f"TypeError: {e}")

#     scout = MobileRobotABC("Scout", max_speed=1.5, terrain_type="indoor")
#     arm   = ManipulatorRobotABC("Arm-1", arm_reach=0.8, payload_capacity=2.0)

#     scout.move("north")
#     scout.perform_task("navigate to zone B")

#     arm.move("left")
#     arm.perform_task("pick widget")

#     arm.recharge()  # inherited concrete method


# # ===========================================================================
# # EXERCISE 3️⃣ -- __slots__ and Memory Comparison
# # ===========================================================================
# #
# # Goal
# # ----
# # Practice using __slots__ to restrict instance attributes, measure the
# # memory savings over regular instances, and extend a slotted class
# # through inheritance.
# #
# # What to implement
# # -----------------
# #   - Pose          -- regular class, no __slots__
# #   - PoseSlotted   -- same interface, declares __slots__
# #   - StampedPose   -- extends PoseSlotted, adds _timestamp slot only
# #
# # Expected output (byte counts are approximate)
# # -----------------------------------------------
# #   AttributeError: 'PoseSlotted' object has no attribute '_extra'
# #   Pose total (1000 instances):        280000 bytes
# #   PoseSlotted total (1000 instances): 56000 bytes
# #   Memory saved:                       224000 bytes
# #   StampedPose(x=1.0, y=2.0, heading=0.5, timestamp=1712345678.0)
# #   1.0 2.0 0.5 1712345678.0
# # ===========================================================================

# import sys as _sys


# # TODO: Implement Pose
# #
# # __init__(self, x: float, y: float, heading: float)
# #   - Set _x, _y, _heading.
# #
# # Read-only @property for each attribute: x, y, heading.
# #
# # __repr__(self) -> str
# #   - Return: "Pose(x=<x>, y=<y>, heading=<heading>)"
# #
# # Every method must have type hints and a Google-style docstring.
# class Pose:
#     pass


# # TODO: Implement PoseSlotted
# #
# # Identical interface to Pose but declares:
# #   __slots__ = ("_x", "_y", "_heading")
# #
# # __init__, @property x / y / heading, and __repr__ are the same as Pose.
# #
# # Every method must have type hints and a Google-style docstring.
# class PoseSlotted:
#     pass


# # TODO: Implement StampedPose(PoseSlotted)
# #
# # Adds ONE new slot:
# #   __slots__ = ("_timestamp",)
# # Do NOT redeclare _x, _y, or _heading.
# #
# # __init__(self, x: float, y: float, heading: float, timestamp: float)
# #   - Call super().__init__(x, y, heading) then set _timestamp.
# #
# # Read-only @property timestamp -> float.
# #
# # __repr__(self) -> str
# #   - Return: "StampedPose(x=<x>, y=<y>, heading=<heading>,
# #              timestamp=<timestamp>)"
# #
# # Every method must have type hints and a Google-style docstring.
# class StampedPose(PoseSlotted):
#     pass


# def exercise3_main() -> None:
#     # Verify dynamic attribute restriction
#     ps = PoseSlotted(1.0, 2.0, 0.0)
#     try:
#         ps._extra = "dynamic"  # type: ignore[attr-defined]
#     except AttributeError as e:
#         print(f"AttributeError: {e}")

#     # Memory comparison
#     poses   = [Pose(float(i), float(i), 0.0) for i in range(1000)]
#     slotted = [PoseSlotted(float(i), float(i), 0.0) for i in range(1000)]

#     pose_mem    = sum(_sys.getsizeof(p) + _sys.getsizeof(p.__dict__) for p in poses)
#     slotted_mem = sum(_sys.getsizeof(p) for p in slotted)

#     print(f"Pose total (1000 instances):        {pose_mem} bytes")
#     print(f"PoseSlotted total (1000 instances): {slotted_mem} bytes")
#     print(f"Memory saved:                       {pose_mem - slotted_mem} bytes")

#     # StampedPose
#     sp = StampedPose(1.0, 2.0, 0.5, timestamp=1712345678.0)
#     print(sp)
#     print(sp.x, sp.y, sp.heading, sp.timestamp)


# # ===========================================================================
# # EXERCISE 4️⃣ -- Protocols and Structural Subtyping
# # ===========================================================================
# #
# # Goal
# # ----
# # Practice defining a typing.Protocol, implementing it in independent
# # classes without inheritance, writing a polymorphic dispatch function,
# # and using @runtime_checkable for isinstance() checks.
# #
# # What to implement
# # -----------------
# #   - Executable    -- @runtime_checkable Protocol
# #   - PickTask      -- satisfies Executable, no shared base
# #   - DeliverTask   -- satisfies Executable, no shared base
# #   - SleepTask     -- does NOT satisfy Executable (wrong method name)
# #   - dispatch()    -- module-level function
# #
# # Expected output
# # ---------------
# #   Scout picks an object
# #   Arm-1 delivers to destination
# #   True
# #   True
# #   False
# # ===========================================================================

# from typing import Protocol, runtime_checkable


# # TODO: Implement Executable
# #
# # Decorate with @runtime_checkable and inherit from Protocol.
# #
# # execute(self, robot_name: str) -> bool
# #   - Declare only (body is ...). Any class that has this method with
# #     this signature satisfies the protocol without inheriting from it.
# #
# # Include a class-level Google-style docstring.
# class Executable(Protocol):
#     pass


# # TODO: Implement PickTask
# #
# # Do NOT inherit from Executable or any other base.
# #
# # execute(self, robot_name: str) -> bool
# #   - Print: "<robot_name> picks an object"
# #   - Return True.
# #
# # Every method must have type hints and a Google-style docstring.
# class PickTask:
#     pass


# # TODO: Implement DeliverTask
# #
# # Do NOT inherit from Executable or any other base.
# #
# # execute(self, robot_name: str) -> bool
# #   - Print: "<robot_name> delivers to destination"
# #   - Return True.
# #
# # Every method must have type hints and a Google-style docstring.
# class DeliverTask:
#     pass


# # TODO: Implement SleepTask
# #
# # This class intentionally does NOT satisfy the Executable protocol.
# # Add a sleep() method instead of execute() so that isinstance() returns
# # False when checked against Executable.
# #
# # sleep(self, duration: float) -> None
# #   - Print: "sleeping for <duration>s"
# #
# # Every method must have type hints and a Google-style docstring.
# class SleepTask:
#     pass


# # TODO: Implement dispatch(task: Executable, robot_name: str) -> bool
# #
# # A module-level function that calls task.execute(robot_name) and
# # returns its result.  Accept any Executable-conforming object.
# #
# # Must have type hints and a Google-style docstring.
# def dispatch(task: Executable, robot_name: str) -> bool:
#     pass  # type: ignore[return-value]


# def exercise4_main() -> None:
#     pick    = PickTask()
#     deliver = DeliverTask()
#     sleep   = SleepTask()

#     dispatch(pick,    "Scout")
#     dispatch(deliver, "Arm-1")

#     # isinstance checks via @runtime_checkable
#     print(isinstance(pick,    Executable))   # True
#     print(isinstance(deliver, Executable))   # True
#     print(isinstance(sleep,   Executable))   # False


# ===========================================================================
# Entry point -- comment/uncomment the exercise you want to run
# ===========================================================================

if __name__ == "__main__":
    exercise1_main()
    # exercise2_main()
    # exercise3_main()
    # exercise4_main()