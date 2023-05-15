import cv2
from djitellopy import Tello


# Create a Tello Object
drone = Tello()

# Connect the drone
drone.connect()

# Check your battery
battery_level = drone.get_battery()
print(battery_level)

# Image Set-up
drone.streamon()
# Flight script
drone.takeoff()
# Capture this image
frame_read = drone.get_frame_read()
cv2.imwrite(f"name.png", frame_read.frame)

drone.land()
drone.streamoff()

# End of Flight


