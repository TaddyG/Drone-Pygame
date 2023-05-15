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

# CODE YOUR FLIGHT PLAN HERE

tello.land()

# End of Flight
