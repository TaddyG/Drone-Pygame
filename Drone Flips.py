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

tello.flip_back()
tello.flip_left()
tello.flip_right()
tello.flip_forward()

tello.land()

# End of Flight
