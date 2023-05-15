import cv2
from djitellopy import Tello

# Create a Tello Object
tello = Tello()

# Connect the drone
tello.connect()

# Check your battery
battery_level = tello.get_battery()
print(battery_level)

# Flight script

tello.takeoff()

tello.move_forward(50)
tello.move_left(60)
tello.move_back(50)
tello.move_right(60)

# Arguments for left and right movements must be equal.
# Arguments for forward and backward movements must be equal
# Arguments for all four movements may be equal

# Alternate flight script for a circular path
# tello.move_forward(50)
# tello.rotate_clockwise(90)
# tello.move_forward(50)
# tello.rotate_clockwise(90)
# tello.move_forward(50)
# tello.rotate_clockwise(90)
# tello.move_forward(50)
# tello.rotate_clockwise(90)


tello.land()

# End of Flight
