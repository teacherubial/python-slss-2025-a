# Pygame Drawing
# Author: Ubial
# 5 January 2026

import pygame

def game():
    pygame.init()

    # COLOURS - (R, G, B)
    # CONSTANTS ALL HAVE CAPS FOR THEIR NAMES
    WHITE = (255, 255, 255)
    BLACK = (  0,   0,   0)
    RED   = (255,   0,   0)
    GREEN = (  0, 255,   0)
    BLUE  = (  0,   0, 255)
    GREY  = (128, 128, 128)

    # CONSTANTS
    WIDTH = 800
    HEIGHT = 600
    SIZE = (WIDTH, HEIGHT)

    # Creating the Screen
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Beautiful Drawing")

    # Variables
    done = False
    clock = pygame.time.Clock()

    # ------------ MAIN GAME LOOP
    while not done:
        # ------ MAIN EVENT LISTENER
        # when the user does something
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ------ GAME LOGIC

        # ------ DRAWING TO SCREEN
        screen.fill(WHITE)
        # draw a red rectangle in the middle of the screen
        pygame.draw.rect(screen, RED, (WIDTH / 2 - 100, HEIGHT / 2 - 40, 200, 80))
        # draw a blue circle on top of the red rectangle
        pygame.draw.circle(screen, BLUE, (WIDTH / 2, HEIGHT / 2 - 80), 40)

        # draw a 6 lines from the top middle to the middle right
        # they repeat moving down the y-axis 10 px each
        for offset in range(5):
            pygame.draw.line(screen, GREEN, (WIDTH / 2 + 20, 20 + offset * 10), (WIDTH - 20, HEIGHT / 2 - 20 + offset * 10))

        # Update screen
        pygame.display.flip()

        # ------ CLOCK TICK
        clock.tick(60) # 60 fps

    pygame.quit()

if __name__ == "__main__":
    game()
