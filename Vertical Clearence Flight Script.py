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
tello.move_up(60)
tello.move_forward(50)
tello.move_down(60)
tello.move_forward(50)

# Note : We use the same values for the up and down movements to return to
# original flight altitude

tello.land()

# End of Flight
