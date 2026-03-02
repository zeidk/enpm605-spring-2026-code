"""
Course: ENPM605
Lecture: OOP Part 1

Author: zeidk
Created: 2026-03-01
"""

# ──────────────────────────────────────────────
# 📌 Snippet 6
# ──────────────────────────────────────────────
# 1. Create a class called 'Robot' with the following:
#    - __init__ that takes 'name' (str) and 'battery' (int, default 100)
#    - Attributes: name, battery, tasks_completed (int, default 0)

# 2. Add a method 'perform_task(self, task_name: str)' that:
#    - If battery >= 10: prints "<name> performing: <task_name>",
#      decreases battery by 10, and increments tasks_completed
#    - Otherwise: prints "<name> needs recharging!"

# 3. Add a method 'recharge(self)' that sets battery back to 100
#    and prints "<name> fully recharged!"

# 4. Create two Robot instances and have them perform several tasks.
#    Print each robot's tasks_completed and battery after the tasks.

# 5. Add a class attribute 'total_robots' that tracks how many
#    Robot instances have been created. Increment it in __init__.

# class Robot:
#     pass

# if __name__ == '__main__':
#     # Create two Robot instances
#     robot1 = Robot("Atlas")
#     robot2 = Robot("Spot", 50)

#     # Have them perform several tasks
#     robot1.perform_task("welding")
#     robot1.perform_task("painting")
#     robot1.perform_task("inspection")

#     robot2.perform_task("delivery")
#     robot2.perform_task("sorting")
#     robot2.perform_task("scanning")
#     robot2.perform_task("lifting")
#     robot2.perform_task("packing")
#     robot2.perform_task("cleaning")  # battery hits 0 after this

#     # This one should trigger the recharge warning
#     robot2.perform_task("assembly")

#     # Recharge and continue
#     robot2.recharge()
#     robot2.perform_task("assembly")

#     # Print final state
#     print(f"\n{robot1.name}: tasks={robot1.tasks_completed}, battery={robot1.battery}")
#     print(f"{robot2.name}: tasks={robot2.tasks_completed}, battery={robot2.battery}")
#     print(f"Total robots created: {Robot.total_robots}")

# ──────────────────────────────────────────────
# 📌 Snippet 14
# ──────────────────────────────────────────────
# 1. Create a class 'Robot' with:
#    - __init__(self, name: str, battery: int = 100)
#    - __str__ that returns "<name> [<battery>%]"
#    - __repr__ that returns "Robot('<name>', <battery>)"

# 2. Implement __eq__ so two robots are equal if their
#    battery levels are equal (regardless of name).

# 3. Implement __add__ so adding two Robots returns a new Robot
#    with name "merged" and the sum of their batteries (capped at 100).

# 4. Implement __gt__ so robots can be compared by battery level.

# 5. Implement __len__ so len(robot) returns tasks_completed.

# 6. Test your class (see next slide)


# class Robot:
#     pass


# if __name__ == "__main__":
#     scout = Robot("Scout", 60)
#     hauler = Robot("Hauler", 60)

#     # __str__: human-readable output
#     print(scout)  # Scout [60%]

#     # __repr__: developer output, looks like valid Python
#     print(repr(scout))  # Robot('Scout', 60)

#     # __eq__: compare by battery level
#     print(scout == hauler)  # True  (both have battery 60)
#     print(scout == Robot("X", 90))  # False (different battery)

#     # __add__: merge two robots, battery capped at 100
#     print(scout + hauler)  # merged [100%]  (60 + 60 = 120, capped to 100)
#     print(scout + Robot("X", 20))  # merged [80%]   (60 + 20 = 80, no cap needed)

#     # __gt__: compare by battery level
#     print(scout > Robot("X", 40))  # True  (60 > 40)
#     print(scout > hauler)  # False (60 > 60 is False)

#     # __len__: number of tasks completed
#     scout.tasks_completed = 3
#     print(len(scout))  # 3
#     print(len(hauler))  # 0  (default, no tasks performed yet)


# ──────────────────────────────────────────────
# 📌 Snippet 23
# ──────────────────────────────────────────────
# 1. Create a class 'Sensor' with:
#    - __init__(self, sensor_type: str, range_m: float = 10.0)
#    - Non-public attributes: _sensor_type, _range_m

# 2. Add a read-only @property 'sensor_type' (cannot be changed
#    after creation).

# 3. Add a @property 'range_m' with a setter that:
#    - Raises ValueError if range_m is set to a negative number (review appendix first)
#    - Raises TypeError if range_m is not int or float (review appendix first)

# 4. Add methods:
#    - calibrate(offset: float) -> None  (adjusts _range_m by offset)
#    - read() -> float  (returns _range_m with simulated noise)

# 5. Add __str__ that returns "Sensor(<type>): range=<range_m>m"

# 6. Test your class

# class Sensor:
#     pass

# if __name__ == "__main__":
#     lidar = Sensor("lidar", 50.0)
#     print(lidar)            # Sensor(lidar): range=50.0m
#     lidar.calibrate(2.5)
#     print(lidar)            # Sensor(lidar): range=52.5m
#     lidar.calibrate(-5.0)
#     print(lidar)            # Sensor(lidar): range=47.5m