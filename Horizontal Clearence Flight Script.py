import cv2
from djitellopy import Tello

# Create a Tello Object
tello = Tello()

# Connect the drone
tello.connect()

# Check your battery
battery_level = tello.get_battery()
print(battery_level

# Flight script

tello.takeoff()

tello.move_forward(50)
tello.move_left(60)
tello.move_forward(50)
tello.move_right(60)
tello.move_forward(50)

# Note : We use the same values for the left and right movements to return to
# original flight path

tello.land()

# End of Flight
