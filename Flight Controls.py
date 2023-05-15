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

# Movements
tello.move_forward()                                 # Enter int between 20-500
tello.move_back()                                    # Enter int between 20-500
tello.move_up()                                      # Enter int between 20-500
tello.move_down()                                    # Enter int between 20-500
tello.move_left()                                    # Enter int between 20-500
tello.move_right()                                   # Enter int between 20-500
tello.rotate_clockwise()                             # Enter int between 1-360
tello.rotate_counter_clockwise()                     # Enter int between 1-360

tello.land()

# End of Flight
