#!/usr/bin/env python3

import pygame

boardHardU = [[0,0,8,0,0,0,0,5,0],
              [0,2,9,0,0,0,4,1,8],
              [0,0,0,0,2,0,0,0,0],
              [0,0,0,0,5,3,1,0,0],
              [6,0,7,4,0,1,3,0,9],
              [0,0,1,7,9,0,0,0,0],
              [0,0,0,0,1,0,0,0,0],
              [3,4,2,0,0,0,8,6,0],
              [0,8,0,0,0,0,9,0,0]]

boardUnc = [[0,0,0,2,0,0,9,0,0],
	        [0,0,9,6,0,0,4,1,0],
	        [2,0,0,0,0,0,0,0,6],

	        [0,0,8,0,0,0,5,9,0],
	        [9,0,4,0,0,0,0,7,0],
	        [0,1,2,0,0,3,0,0,0],

	        [0,0,0,0,9,5,0,0,4],
	        [0,0,3,0,8,1,0,0,0],
	        [0,0,0,7,0,0,0,0,0]]

boardCom = [[3,4,6,2,1,8,9,5,7],
	        [8,5,9,6,3,7,4,1,2],
	        [2,7,1,5,4,9,3,8,6],

	        [7,6,8,1,2,4,5,9,3],
	        [9,3,4,8,5,6,2,7,1],
	        [5,1,2,9,7,3,6,4,8],

	        [1,2,7,3,9,5,8,6,4],
	        [6,9,3,4,8,1,7,2,5],
	        [4,8,5,7,6,2,1,3,9]]


board = boardHardU

#returns in which square (1-9) the position is in
def getSquareNum( x, y):
    x1, x2, y1, y2= [0,3,6], [2,5,8], [0,3,6], [2,5,8]
    count = 1
    
    for i in range(3):
        for j in range(3):
            if x >= x1[i] and y >= y1[j] and x <= x2[i] and y <= y2[j]:
                return count
            else:
                count += 1
    
#returns an array which represents a square
def getSquare( n):
    count = 1
    
    for i in [0,3,6]:
        for j in [0,3,6]:
            if n == count:
                return square(i,j)
            else:
                count += 1
        
def square( x, y):
    square = []
    realy = y
    for i in range(3):
        for j in range(3):
            square.append(board[x][y])	
            y += 1
        x += 1
        y = realy

    return square

#returns if number played on position x,y is valid
def isValidMove( x, y, num):
    row = board[x]
    row = [i for i in row if i != 0]

    col = []
    for i in range(9):
        col.append(board[i][y])	
    col = [i for i in col if i != 0]

    sqr = getSquare(getSquareNum(x,y))	
    sqr = [i for i in sqr if i != 0]

    if allUnique(row) and allUnique(col) and allUnique(sqr):
        return True
    else:
        return False

def allUnique( n):
    seen = set()
    return not any(i in seen or seen.add(i) for i in n)

def isValidSolution():
    bools = []

    for i in range(9):
        for j in range(9):
            bools.append(isValidMove(i, j, board[i][j]))
    return all(bools)

def printBoard():
    for i in board:
        print(i)

def startingNumbers():
    numbers = []

    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                numbers.append((i, j, board[i][j]))
    
    return numbers

def isStartingNumber( x, y, num, startNum):
    outcome = False	

    for i in startNum:
        if i[0] == x and i[1] == y and i[2] == num:
            outcome = True
    
    return outcome

def solveSudoku():
    i, j = 0, 0
    startNum = startingNumbers()
    number = 1
    noValidMove = False

    while i < 9:
        while j < 9:
            if i >= 9:
                break
            elif not isStartingNumber(i, j, board[i][j], startNum):
                drawBlank(i,j)
                if number > 9:
                    drawBlank(i,j)
                else:
                    drawNumber(number, i, j, blue)
                drawGrid()
                drawIndications()
                pygame.display.update()

                if noValidMove:
                    board[i][j] += 1
                    number = board[i][j]
                    noValidMove = False
                else:
                    board[i][j] = number
                    if number > 9:
                        board[i][j] = 0
                        j -= 1
                        if j < 0:
                            j = 8
                            i -= 1
                        noValidMove = True
                        number = 1
                    elif isValidMove(i, j, number):
                        j += 1
                        if j == 9:
                            j = 0
                            i += 1
                        number = 1
                    else:
                        number += 1
            else:
                if noValidMove:
                    j -= 1
                    if j < 0:
                        j = 8
                        i -= 1
                else:
                    j += 1
                    if j > 8:
                        j = 0
                        i += 1


white = pygame.Color('white')
black = pygame.Color('black')
blue = pygame.Color('blue')

running = True
size = 800
width, height = size, size 
squareSize = width // 9
edgeBorder = (width % 9) // 2

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sudoku Solver")

def drawGrid():
    eb = edgeBorder
    for i in range(eb, (width-squareSize), squareSize):
        for j in range(eb, (height-squareSize), squareSize):
            pygame.draw.rect(screen, black, (i,j,squareSize,squareSize), 3)

def drawNumber(number, x, y, colour):
    font = pygame.font.Font('freesansbold.ttf', 92)
    text = font.render(str(number), True, colour)
    textRect = text.get_rect()
    textRect.center = ((50 + y * squareSize), (55 + x * squareSize))
    screen.blit(text, textRect)

def drawBlank(x, y):
    blank = pygame.Rect(0,0,(squareSize), (squareSize))
    blank.center = ((50 + y * squareSize), (55 + x * squareSize))
    pygame.draw.rect(screen, white, blank,0)

def drawStartingNumbers():
    number = startingNumbers()
    
    for i in number:
        drawNumber(i[2], i[0], i[1], black)

def drawIndications():
    eb = edgeBorder
    pygame.draw.line(screen, blue, (eb,(squareSize*3+eb)), ((squareSize*9+eb),(squareSize*3+eb)), 6)
    pygame.draw.line(screen, blue, (eb,(squareSize*6+eb)), ((squareSize*9+eb),(squareSize*6+eb)), 6)
    pygame.draw.line(screen, blue, ((squareSize*3+eb),eb), ((squareSize*3+eb),(squareSize*9+eb)), 6)
    pygame.draw.line(screen, blue, ((squareSize*6+eb),eb), ((squareSize*6+eb),(squareSize*9+eb)), 6)

def setup():
    screen.fill(white)
    drawGrid()
    drawIndications()
    drawStartingNumbers()
    pygame.display.update()

def event(event):
    if event.type == pygame.QUIT:
        pygame.display.quit()
        pygame.quit()
        exit()
        running = False

def execute():
    setup()

    solveSudoku()

    while running:
        for e in pygame.event.get():
            event(e)

    
execute()
