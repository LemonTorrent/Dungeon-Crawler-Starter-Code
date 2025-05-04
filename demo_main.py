import pygame, sys
from pygame.locals import *

pygame.init()

size = (width, height) = (pygame.display.Info().current_w, pygame.display.Info().current_h)

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
color = (0, 0, 0)

def main():
    global screen
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                # Screen controls
                if event.key == K_f:
                    screen = pygame.display.set_mode(size, FULLSCREEN)
                elif event.key == K_ESCAPE:
                    screen = pygame.display.set_mode(size)
                elif event.key == K_q:
                    sys.exit()
        screen.fill(color)
        pygame.display.flip()


if __name__ == "__main__":
    main()