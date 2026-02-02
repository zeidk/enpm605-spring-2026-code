"""
ENPM605 - Python Applications for Robotics
Lecture 2: Python Fundamentals — Part I
Spring 2026 | University of Maryland

Section: Putting It All Together
"""

# ──────────────────────────────────────────────
# 📌 Snippet 40 — Exercise 5: Robot Status Monitor
# ──────────────────────────────────────────────

# Robot parameters (add type hints to all variables)
robot_name = "Waffle_01"
battery = 65
speed = 0.8
status_log = "IDLE:MOVING:CHARGING:MOVING:IDLE"

# 1. Use an f-string to print: "Robot Waffle_01 | Battery: 65%"

# 2. Classify battery level using if/elif/else:
#    >= 80: "OK", 50-79: "LOW", 20-49: "WARNING", < 20: "CRITICAL"

# 3. Use string methods to:
#    a) Count how many times "MOVING" appears in status_log
#    b) Split status_log by ":" into a list
#    c) Check if the last status is "IDLE"

# 4. Use slicing to extract the first status entry from status_log

# 5. Create a formatted status message:
#    "Waffle_01 | Battery: LOW | Speed: 0.80 m/s | States: 5"