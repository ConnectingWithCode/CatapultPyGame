import pygame
import sys


def main():
    # pre-define RGB colors for Pygame
    BLACK = pygame.Color("Black")
    WHITE = pygame.Color("White")
    IMAGE_SIZE = 470
    TEXT_HEIGHT = 30
    pygame.init()
    screen = pygame.display.set_mode((IMAGE_SIZE, IMAGE_SIZE + TEXT_HEIGHT))
    pygame.display.set_caption("Text, Sound, and an Image")

    # Prepare the image
    image = pygame.image.load("2dogs.JPG")
    image = pygame.transform.scale(image, (IMAGE_SIZE, IMAGE_SIZE))

    # Prepare the text caption(s)
    # TODO 4: Create a font object with a size 28 font.
    font1 = pygame.font.SysFont("comicsansms", 28)
    # print(pygame.font.get_fonts())
    my_fonts = pygame.font.get_fonts()
    for afont in sorted(my_fonts):
        print(afont)
    caption1 = font1.render("Two Dogs", True, BLACK)

    font2 = pygame.font.SysFont("impact", 48)
    caption2 = font2.render("MINE!", True, WHITE)

    bark_sound = pygame.mixer.Sound("bark.mp3")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                bark_sound.play()

        screen.fill(WHITE)
        screen.blit(image, (0,0))

        # TODO 6: Draw (blit) the text image onto the screen in the middle bottom.
        x_loc = screen.get_width() / 2 - caption1.get_width() / 2
        y_loc = image.get_height() - 5
        screen.blit(caption1, (x_loc, y_loc))
        screen.blit(caption2, (50, 200))

        # TODO 7: On your own, create a new bigger font and in white text place a 'funny' message on top of the image.

        # Update the screen
        pygame.display.update()


main()
