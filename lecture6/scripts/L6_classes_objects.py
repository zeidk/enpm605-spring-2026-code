"""
Course: ENPM605
Lecture: OOP Part 1

Author: zeidk
Created: 2026-03-01
"""


# # ──────────────────────────────────────────────
# # 📌 Snippet 1
# # ──────────────────────────────────────────────
# class RobotArm:
#     """Blueprint for a robot arm.

#     A robot arm is mounted at a fixed station and can rotate
#     its joint and grip objects. The arm tracks its current
#     joint angle and gripping state.

#     Attributes:
#         station (int): The station number where the arm is mounted.
#         joint_angle (float): The current joint angle in degrees.
#         gripping (bool): Whether the arm is currently gripping an object.
#     """

#     def __init__(self, station: int) -> None:
#         """Initialize a RobotArm at the given station.

#         The arm starts with a joint angle of 0.0 degrees and
#         is not gripping anything.

#         Args:
#             station: The station number where the arm is mounted.
#         """
#         self.station = station
#         self.joint_angle = 0.0
#         self.gripping = False

#     def pick_up(self) -> None:
#         """Activate the gripper to pick up an object.

#         Sets the gripping state to True.
#         """
#         self.gripping = True

#     def rotate(self, angle: float) -> None:
#         """Rotate the arm's joint by the given angle.

#         The angle is added to the current joint angle. Positive
#         values rotate clockwise, negative values rotate
#         counterclockwise.

#         Args:
#             angle: The rotation angle in degrees.
#         """
#         self.joint_angle += angle


# # ──────────────────────────────────────────────
# # 📌 Snippet 2
# # ──────────────────────────────────────────────
# if __name__ == "__main__":
#     # Three arms built from the same blueprint
#     arm_1 = RobotArm(station=1)
#     arm_2 = RobotArm(station=2)
#     arm_3 = RobotArm(station=3)

#     arm_1.pick_up()  # arm_1 is gripping, others are not
#     arm_2.rotate(45.0)  # arm_2 rotated, others unchanged

#     print(arm_1.gripping)  # True
#     print(arm_2.joint_angle)  # 45.0
#     print(arm_3.gripping)  # False

# # ──────────────────────────────────────────────
# # 📌 Snippet 3
# # ──────────────────────────────────────────────
# if __name__ == "__main__":
#     arm = RobotArm(station=1)  # or arm = RobotArm(1)
#     print(arm.station)  # 1
#     print(arm.joint_angle)  # 0.0
#     print(arm.gripping)  # False

# # ──────────────────────────────────────────────
# # 📌 Snippet 4
# # ──────────────────────────────────────────────
# if __name__ == "__main__":
#     arm_1 = RobotArm(station=1)
#     arm_2 = RobotArm(station=2)

#     arm_1.joint_angle = 45.0

#     print(arm_1.joint_angle)  # 45.0
#     print(arm_2.joint_angle)  # 0.0  (unaffected)


# # ──────────────────────────────────────────────
# # 📌 Snippet 5
# # ──────────────────────────────────────────────
# class RobotArm:
#     total_arms = 0  # Class attribute (shared by all instances)

#     def __init__(self, station: int):
#         self.station = station  # Instance attribute
#         self.joint_angle = 0.0  # Instance attribute
#         self.gripping = False  # Instance attribute
#         RobotArm.total_arms += 1  # Modify via the class name


# if __name__ == "__main__":
#     arm_1 = RobotArm(station=1)
#     arm_2 = RobotArm(station=2)
#     print(RobotArm.total_arms)  # 2 (shared across all instances)
#     print(arm_1.total_arms)  # 2 (accessible through instances)
#     print(arm_2.total_arms)  # 2 (same value, same attribute)


# # ──────────────────────────────────────────────
# # 📌 Snippet 7
# # ──────────────────────────────────────────────

# class Robot:
#     def __init__(self, name: str, battery: int = 100):
#         self.name = name
#         self.battery = battery


# if __name__ == "__main__":
#     scout = Robot("Scout")
#     print(scout)  # <__main__.Robot object at 0x7fe4dc66bbb0>
#     # Not very useful! Let's fix this by overriding __str__


# # ──────────────────────────────────────────────
# # 📌 Snippet 8
# # ──────────────────────────────────────────────
# class Robot:
#     def __init__(self, name: str, battery: int = 100):
#         self.name = name
#         self.battery = battery

#     def __str__(self) -> str:
#         return f"{self.name} (Battery: {self.battery}%)"


# if __name__ == "__main__":
#     scout = Robot("Scout")
#     print(scout)  # Scout (Battery: 100%)
#     print(str(scout))  # Scout (Battery: 100%)


# # ──────────────────────────────────────────────
# # 📌 Snippet 9
# # ──────────────────────────────────────────────
# class Robot:
#     def __init__(self, name: str, battery: int = 100):
#         self.name = name
#         self.battery = battery

#     def __repr__(self) -> str:
#         return f"Robot(name='{self.name}', battery={self.battery})"


# if __name__ == "__main__":
#     scout = Robot("Scout")
#     print(repr(scout))
#     # Robot(name='Scout', battery=100)
#     robots = [Robot("Scout"), Robot("Hauler", 80)]
#     print(robots)
#     # [Robot(name='Scout', battery=100),
#     #  Robot(name='Hauler', battery=80)]


# # ──────────────────────────────────────────────
# # 📌 Snippet 10
# # ──────────────────────────────────────────────
# class Robot:
#     def __init__(self, name: str, battery: int = 100):
#         self.name = name
#         self.battery = battery

#     def __str__(self) -> str:
#         return f"{self.name} (Battery: {self.battery}%)"

#     def __repr__(self) -> str:
#         return f"Robot(name='{self.name}', battery={self.battery})"


# if __name__ == "__main__":
#     scout = Robot("Scout", 80)

#     print(scout)  # Scout (Battery: 80%)             __str__
#     print(repr(scout))  # Robot(name='Scout', battery=80)  __repr__
#     print(f"Bot: {scout}")  # Bot: Scout (Battery: 80%)        __str__
#     print([scout])  # [Robot(name='Scout', battery=80)] __repr__


# # ──────────────────────────────────────────────
# # 📌 Snippet 11
# # ──────────────────────────────────────────────
# class Sensor:
#     def __init__(self, sensor_type: str, range_m: float):
#         self.sensor_type = sensor_type
#         self.range_m = range_m

#     def __eq__(self, other) -> bool:
#         if isinstance(other, Sensor):
#             return self.range_m == other.range_m
#         return NotImplemented

#     def __gt__(self, other) -> bool:
#         if isinstance(other, Sensor):
#             return self.range_m > other.range_m
#         return NotImplemented


# if __name__ == "__main__":
#     lidar = Sensor("lidar", 50.0)
#     camera = Sensor("camera", 30.0)
#     print(lidar == 3)  # False
#     print(lidar > camera)  # True


# # ──────────────────────────────────────────────
# # 📌 Snippet 12
# # ──────────────────────────────────────────────
# class Sensor:
#     def __init__(self, sensor_type: str, range_m: float):
#         self.sensor_type = sensor_type
#         self.range_m = range_m

#     def __add__(self, other):
#         if isinstance(other, Sensor):
#             return Sensor("fused", self.range_m + other.range_m)
#         elif isinstance(other, (int, float)):
#             return Sensor(self.sensor_type, self.range_m + other)
#         return NotImplemented

#     def __repr__(self) -> str:
#         return f"Sensor('{self.sensor_type}', {self.range_m})"


# if __name__ == "__main__":
#     lidar = Sensor("lidar", 50.0)
#     camera = Sensor("camera", 30.0)
#     print(lidar + camera)  # Sensor('fused', 80.0)
#     print(lidar + 10.0)  # Sensor('lidar', 60.0)


# # ──────────────────────────────────────────────
# # 📌 Snippet 13
# # ──────────────────────────────────────────────
# class Robot:
#     def __init__(self, name: str, battery: int = 100):
#         self.name = name
#         self.battery = battery
#         self.log: list[str] = []

#     def __iter__(self):
#         return iter(self.log)

#     def __contains__(self, task_name: str):
#         return task_name in self.log

#     def __call__(self, task_name: str):
#         self.log.append(task_name)
#         print(f"{self.name} assigned: {task_name}")


# if __name__ == "__main__":
#     scout = Robot("Scout")
#     scout("pick widget")  # Scout assigned: pick widget
#     scout("navigate to zone B")  # Scout assigned: navigate to zone B
#     for entry in scout:  # Uses __iter__
#         print(entry)  # pick widget, then navigate to zone B
#     print("pick widget" in scout)  # True  -- uses __contains__

# # ──────────────────────────────────────────────
# # 📌 Snippet 15
# # ──────────────────────────────────────────────
# class Robot:
#     """A robot that performs tasks. The caller only needs to know
#     that recharge() restores the battery. How it works internally
#     is hidden.
#     """

#     def __init__(self, name: str, battery: int = 100):
#         self.name = name
#         self.battery = battery

#     def recharge(self):
#         """Restore battery to full."""
#         # Internal details hidden:
#         # - validate current state
#         # - reset drain counter
#         # - log the recharge event
#         self.battery = 100


# if __name__ == "__main__":
#     scout = Robot("Scout")
#     scout.recharge()  # Simple interface
#     print(scout.battery)  # 100


# # ──────────────────────────────────────────────
# # 📌 Snippet 16
# # ──────────────────────────────────────────────
# class Robot:
#     def __init__(self, name: str, battery: int = 100):
#         self.name = name
#         self.battery = battery

#     def perform_task(self, task_name: str):
#         self.battery -= 10


# if __name__ == "__main__":
#     scout = Robot("Scout")
#     scout.battery = "full"  # No validation!
#     scout.perform_task("pick")  # TypeError: unsupported operand type(s)


# # ──────────────────────────────────────────────
# # 📌 Snippet 17
# # ──────────────────────────────────────────────
# class Robot:
#     def __init__(self, name: str, battery: int = 100):
#         self._name = name  # Non-public by convention
#         self._battery = battery  # Non-public by convention


# if __name__ == "__main__":
#     scout = Robot("Scout")
#     scout._battery = "full"  # Still possible, but violates the convention

# # ──────────────────────────────────────────────
# # 📌 Snippet 18
# # ──────────────────────────────────────────────
# class Robot:
#     def __init__(self, name: str, battery: int = 100):
#         self._name = name
#         self._battery = battery

#     def get_battery(self) -> int:
#         return self._battery

#     def set_battery(self, battery: int):
#         if isinstance(battery, int) and 0 <= battery <= 100:
#             self._battery = battery
#         else:
#             raise ValueError("Battery must be int in [0, 100]")


# if __name__ == "__main__":
#     scout = Robot("Scout")
#     scout.set_battery(80)
#     # scout.set_battery("full")  # ValueError
#     print(scout.get_battery())  # 80


# # ──────────────────────────────────────────────
# # 📌 Snippet 19
# # ──────────────────────────────────────────────
# class Robot:
#     def __init__(self, name: str, battery: int = 100):
#         self._name = name
#         self._battery = battery

#     @property
#     def battery(self) -> int:
#         """The battery level of the robot."""
#         return self._battery

#     # # ──────────────────────────────────────────────
#     # # 📌 Snippet 20
#     # # ──────────────────────────────────────────────
#     # @battery.setter
#     # def battery(self, value: int):
#     #     if not isinstance(value, int) or not (0 <= value <= 100):
#     #         raise ValueError("Battery must be an integer between 0 and 100")
#     #     self._battery = value


# # # ──────────────────────────────────────────────
# # # 📌 Snippet 21
# # # ──────────────────────────────────────────────
# # if __name__ == "__main__":
# #     scout = Robot("Scout")
# #     print(scout.battery)  # 100  (calls the getter)
# #     scout.battery = 80  # OK   (calls the setter with validation)
# #     print(scout.battery)  # 80  (calls the getter)
# #     # scout.battery = "full"  # (calls the setter with validation) ValueError!


# # ──────────────────────────────────────────────
# # 📌 Snippet 22
# # ──────────────────────────────────────────────
# class Robot:
#     def __init__(self, name: str):
#         self._name = name

#     @property
#     def name(self) -> str:
#         return self._name

#     @name.setter
#     def name(self, value):
#         raise AttributeError("Cannot rename a robot after creation")


# if __name__ == "__main__":
#     scout = Robot("Scout")
#     print(scout.name)  # Scout
#     # scout.name = "Bob"   # AttributeError: Cannot rename a robot after creation
