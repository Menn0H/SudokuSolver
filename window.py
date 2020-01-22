#!/usr/bin/env python3

import pygame
from sudoku import Sudoku

def main():

    screen = pygame.display.set_mode((1000,800))

    black = (0,0,0)
    white = (255,255,255)

    screen.fill(white)

    for i in range(20, 600, 30):
        for j in range(20, 600, 30):
            pygame.draw.rect(screen, black, (i, j, 30, 30), 3)

    pygame.display.update()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    

if __name__ == '__main__':
    main()
