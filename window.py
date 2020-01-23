#!/usr/bin/env python3

import pygame
from sudoku import Sudoku

boardUnc =  [[0,0,0,2,0,0,9,0,0],
             [0,0,9,6,0,0,4,1,0],
             [2,0,0,0,0,0,0,0,6],
 
             [0,0,8,0,0,0,5,9,0],
             [9,0,4,0,0,0,0,7,0],
             [0,1,2,0,0,3,0,0,0],
 
             [0,0,0,0,9,5,0,0,4],
             [0,0,3,0,8,1,0,0,0],
             [0,0,0,7,0,0,0,0,0]]

class Window:
    white = pygame.Color('white')
    black = pygame.Color('black')
    blue = pygame.Color('blue')

    def __init__(self, width, height):
        self.running = True
        self.width = width
        self.height = height
        self.sudoku = Sudoku(boardUnc)

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Sudoku Solver")

    def drawGrid(self, width):
        squareSize = width // 9

        for i in range(20, (width + 20), squareSize):
            for j in range(20, (width + 20), squareSize):
                pygame.draw.rect(self.screen, self.black, (i, j, squareSize,
squareSize), 3)

    def drawNumber(self, number, x, y, colour):
        font = pygame.font.Font('freesansbold.ttf', 58)
        text = font.render(str(number), True, colour)
        textRect = text.get_rect()
        textRect.center = ((50 + y * 60), (55 + x * 60))
        self.screen.blit(text, textRect)

    def drawStartingNumbers(self):
        number = self.sudoku.startingNumbers()
        
        for i in number:
            self.drawNumber(i[2], i[0], i[1], self.black) 

    def drawIndications(self):
        pygame.draw.line(self.screen, self.blue, (20,200), (560,200), 6)
        pygame.draw.line(self.screen, self.blue, (20,380), (560,380), 6)
        pygame.draw.line(self.screen, self.blue, (200,20), (200,560), 6)
        pygame.draw.line(self.screen, self.blue, (380,20), (380,560), 6) 

    def setup(self):
        self.screen.fill(self.white)

        self.drawGrid(540)
        self.drawIndications()
        self.drawStartingNumbers()

        pygame.display.update()

    def event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

    def gameLoop(self):
        pass

    def render(self):
        pass

    def execute(self):
        self.setup()
    
        while(self.running):
            for event in pygame.event.get():
                self.event(event)

            self.gameLoop()
            self.render()

if __name__ == '__main__':
    w = Window(1000, 800)
    w.execute()
