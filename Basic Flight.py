from djitellopy import Tello
import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

FORWARD = 0
LEFT = 0
BACKWARD = 0
RIGHT = 0
UP = 0
TURN_L = 0
DOWN = 0
TURN_R = 0

screen = pygame.display.set_mode((582, 450))
pygame.display.set_caption("Tello Drones")

big_font = pygame.font.SysFont("Comic Sans MS", 40, True)
font = pygame.font.SysFont("Comic Sans MS", 20, True)

welcome = big_font.render("Welcome to Tello and Python!", True, BLACK)
controls = font.render("Press WASD to move the drone.", True, BLACK)
more_controls = font.render("UP and DOWN to change the altitude.", True, BLACK)


rectangle = pygame.Rect(460, 420, 150, 50)

screen.fill(WHITE)
screen.blit(welcome, (5, -9))
screen.blit(controls, (5, 40))
screen.blit(more_controls, (5, 65))


pygame.display.flip()

tello = Tello()

tello.connect()

print("Starting")

running = True

while running:

    battery = font.render("Battery: " + str(tello.get_battery()), True, BLACK)

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_t:

                tello.takeoff()

            if event.key == pygame.K_l:

                running = False

            if event.key == pygame.K_w:

                FORWARD = 100

            if event.key == pygame.K_a:

                LEFT = -100

            if event.key == pygame.K_s:

                BACKWARD = -100

            if event.key == pygame.K_d:

                RIGHT = 100

            if event.key == pygame.K_UP:

                UP = 100

            if event.key == pygame.K_LEFT:

                TURN_L = -100

            if event.key == pygame.K_DOWN:

                DOWN = -100

            if event.key == pygame.K_RIGHT:

                TURN_R = 100

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_w:

                FORWARD = 0

            if event.key == pygame.K_a:

                LEFT = 0

            if event.key == pygame.K_s:

                BACKWARD = 0

            if event.key == pygame.K_d:

                RIGHT = 0

            if event.key == pygame.K_UP:

                UP = 0

            if event.key == pygame.K_LEFT:

                TURN_L = 0

            if event.key == pygame.K_DOWN:

                DOWN = 0

            if event.key == pygame.K_RIGHT:

                TURN_R = 0

    left_right = LEFT + RIGHT
    forward_backward = FORWARD + BACKWARD
    up_down = UP + DOWN
    rotate = TURN_L + TURN_R

    tello.send_rc_control(left_right, forward_backward, up_down, rotate)

    pygame.draw.rect(screen, WHITE, rectangle)
    screen.blit(battery, (460, 420))
    pygame.display.flip()

tello.land()
pygame.quit()

# Up Arrow Key - Altitude Increases
# Down Arrow Key - Altitude Decreases
# Left Arrow Key - CCW Rotation
# Right Arrow Key - CW Rotation
# W Key - Move Forward
# A Key - Move Left
# S Key - Move Backwards
# D Key - Move Right
# L Key - Land
# T Key - Takeoff
