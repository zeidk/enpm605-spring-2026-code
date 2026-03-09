"""
Course: ENPM605
Lecture: OOP Part 2

Author: zeidk
Created: 2026-03-06
"""


# ──────────────────────────────────────────────
# Snippet 4️⃣: Association -- Robot assigned a Task
# ──────────────────────────────────────────────
class Task:
    def __init__(self, name: str, priority: int):
        self._name = name
        self._priority = priority


class Robot:
    def __init__(self, name: str):
        self._name = name
        self._current_task: Task | None = None

    def assign_task(self, task: Task) -> None:
        self._current_task = task  # Robot references Task; neither owns the other


if __name__ == "__main__":
    pick  = Task("pick widget", priority=1)
    scout = Robot("Scout")
    scout.assign_task(pick)
    # Both Task and Robot exist independently; deleting one does not destroy the other


# # ──────────────────────────────────────────────
# # Snippet 5️⃣: Aggregation -- Team has Robots
# # ──────────────────────────────────────────────
# class Robot:
#     def __init__(self, name: str, battery: int = 100):
#         self._name = name
#         self._battery = battery
#         self._team: "Team | None" = None

#     @property
#     def name(self) -> str:
#         return self._name


# class Team:
#     def __init__(self, team_name: str):
#         self._team_name = team_name
#         self._robots: list[Robot] = []

#     def add_robot(self, robot: Robot) -> None:
#         if robot._team is not None:
#             raise ValueError(f"{robot.name} already in a team")
#         self._robots.append(robot)
#         robot._team = self

#     def remove_robot(self, robot: Robot) -> None:
#         self._robots.remove(robot)
#         robot._team = None


# if __name__ == "__main__":
#     scout  = Robot("Scout")          # Created independently
#     hauler = Robot("Hauler", 80)     # Created independently
#     alpha  = Team("Alpha")
#     alpha.add_robot(scout)
#     alpha.add_robot(hauler)
#     del alpha                        # Team dissolved
#     print(scout.name)                # Scout -- still exists


# # ──────────────────────────────────────────────
# # Snippet 6️⃣: Composition -- Robot owns Sensors
# # ──────────────────────────────────────────────
# class Sensor:
#     def __init__(self, sensor_type: str, range_m: float):
#         self._sensor_type = sensor_type
#         self._range_m = range_m

#     def __repr__(self) -> str:
#         return f"Sensor({self._sensor_type!r}, {self._range_m})"


# class Robot:
#     def __init__(self, name: str, sensors: list[Sensor]):
#         self._name = name
#         self._sensors = sensors  # Sensors passed in and owned by Robot

#     def __repr__(self) -> str:
#         return f"Robot({self._name!r}, {self._sensors})"


# if __name__ == "__main__":
#     scout = Robot("Scout", [Sensor("lidar", 50.0), Sensor("camera", 20.0)])
#     print(scout)
#     # Robot('Scout', [Sensor('lidar', 50.0), Sensor('camera', 20.0)])
#     # Sensors are created and destroyed with the Robot