import time
import cv2
from djitellopy import Tello

import numpy as np


# Create a Tello Object
tello = Tello()

# Connect the drone
tello.connect()

# Check your battery
battery_level = tello.get_battery()
print(battery_level)

# Stream Set-up
tello.streamon()

while True:
    img = tello.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)




# Flight script


# End of Flight


