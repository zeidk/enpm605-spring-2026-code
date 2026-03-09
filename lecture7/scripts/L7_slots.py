"""
Course: ENPM605
Lecture: OOP Part 2

Author: zeidk
Created: 2026-03-06
"""

import sys


# ──────────────────────────────────────────────
# Snippet 2️⃣3️⃣: __slots__ -- Definition
# ──────────────────────────────────────────────

# Without __slots__: each instance has a __dict__
class Waypoint:
    def __init__(self, x: float, y: float, label: str = ""):
        self._x = x
        self._y = y
        self._label = label


wp = Waypoint(1.0, 2.5, "start")
wp._extra = "dynamic"   # allowed -- __dict__ accepts anything
print(wp.__dict__)      # {'_x': 1.0, '_y': 2.5, '_label': 'start', '_extra': 'dynamic'}


# With __slots__: no __dict__, only listed names allowed
class WaypointSlotted:
    __slots__ = ("_x", "_y", "_label")

    def __init__(self, x: float, y: float, label: str = ""):
        self._x = x
        self._y = y
        self._label = label


wp2 = WaypointSlotted(1.0, 2.5, "start")
# wp2._extra = "dynamic"  # AttributeError: _extra not in __slots__


# # ──────────────────────────────────────────────
# # Snippet 2️⃣4️⃣: __slots__ -- Memory and Performance
# # ──────────────────────────────────────────────
# class Waypoint:
#     def __init__(self, x: float, y: float, label: str = ""):
#         self._x = x
#         self._y = y
#         self._label = label


# class WaypointSlotted:
#     __slots__ = ("_x", "_y", "_label")

#     def __init__(self, x: float, y: float, label: str = ""):
#         self._x = x
#         self._y = y
#         self._label = label


# if __name__ == "__main__":
#     wp   = Waypoint(1.0, 2.5, "start")
#     wp_s = WaypointSlotted(1.0, 2.5, "start")

#     total = sys.getsizeof(wp) + sys.getsizeof(wp.__dict__)
#     print(f"Waypoint total:        {total} bytes")            # ~280 bytes
#     print(f"WaypointSlotted total: {sys.getsizeof(wp_s)} bytes")  # ~56 bytes


# # ──────────────────────────────────────────────
# # Snippet 2️⃣5️⃣: __slots__ -- Tradeoffs and Inheritance
# # ──────────────────────────────────────────────
# class Robot:
#     __slots__ = ("_name", "_battery")

#     def __init__(self, name: str, battery: int = 100):
#         self._name = name
#         self._battery = battery


# class MobileRobot(Robot):
#     __slots__ = ("_speed",)  # only new attributes

#     def __init__(self, name: str, speed: float = 1.0):
#         super().__init__(name)
#         self._speed = speed


# if __name__ == "__main__":
#     scout = MobileRobot("Scout", speed=2.5)
#     # scout._extra = "x"
#     # AttributeError: no __slots__ entry for _extra