# This is a sample Python script.
import pygame
import math

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
pygame.init()

WITH, HEIGHT = 800, 900
WIN = pygame.display.set_mode((WITH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

# PUT COLOR VALUE VAR HERE
DARK_GREY = (80, 78, 81)

FONT = pygame.font.SysFont("NotoSansMono Nerd", 16)

class Planet:

    def __init__(self, x, y, radius, color, mass):
        self.x=x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0


def main():
    # Use a breakpoint in the code line below to debug your script.
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        WIN.fill(DARK_GREY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
    pygame.quit()


main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/