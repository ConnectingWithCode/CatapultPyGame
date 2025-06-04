import pygame
import sys

pygame.init()

# Let's create a caption for the game window
pygame.display.set_caption("David Fisher")


screen = pygame.display.set_mode((1280, 600))
# TODO 05: Change the window size, make sure your circle code still works.

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(pygame.Color("Gray"))

    # Draw things on the screen

    # pygame.draw.circle(screen, color, pos, radius, width(optional)  )
    pygame.draw.circle(screen, pygame.Color("Orange"), (400, 100), 50)

    # TODO 03: Try to draw a red circle in the middle of the screen with a radius 100
    # pygame.draw.circle(screen, color, pos, radius, width(optional)  )
    pygame.draw.circle(screen, pygame.Color("Red"), (screen.get_width()/2, screen.get_height()/2), 100)

    # TODO 04: Try to draw a yellow circle with the center exactly in the lower left corner of the screen, radius 10
    # pygame.draw.circle(screen, color, pos, radius, width(optional)  )
    pygame.draw.circle(screen, pygame.Color("Yellow"), (0, screen.get_height()), 10)

    pygame.display.update()
