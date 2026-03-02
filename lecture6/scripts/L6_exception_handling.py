"""
Course: ENPM605
Lecture: OOP Part 1

Author: zeidk
Created: 2026-03-01
"""


# ──────────────────────────────────────────────
# 📌 Snippet 24
# ──────────────────────────────────────────────
# def compute_speed(distance: float, time: float) -> float:
#     return distance / time


# speed = compute_speed(100.0, 0.0)  # ZeroDivisionError!
# print(f"Speed: {speed}")  # This line never runs


# ──────────────────────────────────────────────
# 📌 Snippet 25
# ──────────────────────────────────────────────
# def compute_speed(distance: float, time: float) -> float:
#     return distance / time


# try:
#     speed = compute_speed(100.0, 0.0)
#     print(f"Speed: {speed}")
# except ZeroDivisionError:
#     print("Error: time cannot be zero")


# ──────────────────────────────────────────────
# 📌 Snippet 26
# ──────────────────────────────────────────────
# values = [10, 20, 30]

# try:
#     print(values[5])
# except IndexError as e:
#     print(f"Caught an error: {e}")

# ──────────────────────────────────────────────
# 📌 Snippet 27
# ──────────────────────────────────────────────
# try:
#     result = int("abc") / 0
# except ValueError:
#     print("Invalid value")
# except ZeroDivisionError:
#     print("Cannot divide by 0")

# # try:
# #     result = int("3") / 0
# # except ValueError:
# #     print("Invalid value")
# # except ZeroDivisionError:
# #     print("Cannot divide by 0")

# ──────────────────────────────────────────────
# 📌 Snippet 28
# ──────────────────────────────────────────────
# try:
#     result = int("abc") / 0
# except (ValueError, ZeroDivisionError) as e:
#     print(f"Error: {e}")

# # try:
# #     result = int("3") / 0
# # except (ValueError, ZeroDivisionError) as e:
# #     print(f"Error: {e}")


# ──────────────────────────────────────────────
# 📌 Snippet 29
# ──────────────────────────────────────────────
# def parse_battery(value: str) -> int:
#     try:
#         level = int(value)
#     except ValueError:
#         print(f"Cannot parse '{value}' as an integer")
#         return -1
#     else:
#         print(f"Successfully parsed battery level: {level}")
#         return level


# parse_battery("85")  # Successfully parsed battery level: 85
# parse_battery("full")  # Cannot parse 'full' as an integer


# ──────────────────────────────────────────────
# 📌 Snippet 30
# ──────────────────────────────────────────────
# def read_config(filename: str):
#     file = None
#     try:
#         file = open(filename)
#         data = file.read()
#         print(f"Loaded {len(data)} characters")
#     except FileNotFoundError:
#         print(f"File '{filename}' not found")
#     finally:
#         if file is not None:
#             file.close()
#         print("Cleanup complete")


# read_config("robot.cfg")  # File 'robot.cfg' not found
# # Cleanup complete


# ──────────────────────────────────────────────
# 📌 Snippet 31
# ──────────────────────────────────────────────
# def read_sensor(value: str) -> float:
#     try:
#         reading = float(value)
#     except ValueError:
#         print(f"Invalid: {value}")
#         reading = 0.0
#     else:
#         print(f"Valid: {reading}")
#     finally:
#         print("Read attempt complete")
#     return reading


# read_sensor("42.5")
# # Valid: 42.5
# # Read attempt complete

# read_sensor("bad")
# # Invalid: bad
# # Read attempt complete


# ──────────────────────────────────────────────
# 📌 Snippet 32
# ──────────────────────────────────────────────
# def set_battery(level: int):
#     if not isinstance(level, int):
#         raise TypeError("Battery level must be an integer")
#     if not (0 <= level <= 100):
#         raise ValueError("Battery level must be between 0 and 100")
#     print(f"Battery set to {level}%")


# set_battery(80)  # Battery set to 80%
# set_battery("full")  # TypeError: Battery level must be an integer
# set_battery(150)  # ValueError: Battery level must be between 0 and 100


# ──────────────────────────────────────────────
# 📌 Snippet 33
# ──────────────────────────────────────────────
# class Robot:
#     def __init__(self, name: str, battery: int = 100):
#         if not isinstance(battery, int) or not (0 <= battery <= 100):
#             raise ValueError("Battery must be an integer between 0 and 100")
#         self._name = name
#         self._battery = battery


# robot = Robot("Scout", 80)  # OK
# robot = Robot("Scout", 200)  # ValueError!


# ──────────────────────────────────────────────
# 📌 Snippet 34
# ──────────────────────────────────────────────
# class Sensor:
#     def __init__(self, sensor_type: str, range_m: float):
#         self.sensor_type = sensor_type
#         self.range_m = range_m

#     def __eq__(self, other):
#         if isinstance(other, Sensor):
#             return self.range_m == other.range_m
#         return NotImplemented


# if __name__ == "__main__":
#     lidar = Sensor("lidar", 50.0)
#     camera = Sensor("camera", 50.0)
#     ultrasonic = Sensor("ultrasonic", 30.0)
#     print(lidar == camera)  # True
#     print(lidar == ultrasonic)  # False
#     print(lidar == "lidar")  # False


# ──────────────────────────────────────────────
# 📌 Snippet 35
# ──────────────────────────────────────────────
# class Robot:
#     def __init__(self, name: str):
#         self.name = name

#     def move(self, direction: str):
#         raise NotImplementedError("Subclasses must implement move()")


# if __name__ == "__main__":
#     robot = Robot("Base")
#     robot.move("north")
#     # NotImplementedError: Subclasses
#     # must implement move()
