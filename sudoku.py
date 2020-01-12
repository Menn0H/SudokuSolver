#!/usr/bin/env python3

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


#returns in which square (1-9) the position is in
def getSquareNum(x, y):
	x1, x2, y1, y2= [0,3,6], [2,5,8], [0,3,6], [2,5,8]
	count = 1
	
	for i in range(3):
		for j in range(3):
			if x >= x1[i] and y >= y1[j] and x <= x2[i] and y <= y2[j]:
				return count
			else:
				count += 1
	
#returns an array which represents a square
def getSquare(n, board):
	count = 1
	
	for i in [0,3,6]:
		for j in [0,3,6]:
			if n == count:
				return square(i,j,board)
			else:
				count += 1
		
def square(x, y, board):
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
def isValidMove(x, y, num, board):
	row = board[x]
	row = [i for i in row if i != 0]

	col = []
	for i in range(9):
		col.append(board[i][y])	
	col = [i for i in col if i != 0]
	
	sqr = getSquare(getSquareNum(x,y), board)	
	sqr = [i for i in sqr if i != 0]

	if allUnique(row) and allUnique(col) and allUnique(sqr):
		return True
	else:
		return False

def allUnique(n):
	seen = set()
	return not any(i in seen or seen.add(i) for i in n)

def isValidSolution(board):
	bools = []

	for i in range(9):
		for j in range(9):
			bools.append(isValidMove(i, j, board[i][j], board))
	return all(bools)

def playMove(x, y, num, board):
	if isValidMove(x, y, num, board):
		board[x][y] = num
	else:
		print("Invalid move")

def printBoard(board):
	for i in board:
		print(i)

def startingNumbers(board):
	numbers = []

	for i in range(9):
		for j in range(9):
			if board[i][j] != 0:
				numbers.append((i, j, board[i][j]))
	
	return numbers

def isStartingNumber(x, y, num, board):
	numbers = startingNumbers(board)
	outcome = False	

	for i in numbers:
		if i[0] == x and i[1] == y and i[2] == num:
			outcome = True
	
	return outcome

def isPlayable(x, y, board):
    number = 0
    playable = False

    for i in range(1,10):
        if isValidMove(x, y, i, board):
            number = i
            playable = True 
            break

    return playable, number

def solveSudoku(board):
    i, j = 0, 0

    while i < 10:
        while j < 10:
            if not isStartingNumber(i, j, board[i][j], board):
                playable, number = isPlayable(i, j, board)

                if playable:
                    playMove(i, j, number, board)
                    j += 0
                else:
                    if j >= 0:
                        j -= 1
                    else:
                        i -= 1
            else:
                j += 1
        i += 1
    printBoard(board)


print(isValidMove(5, 7, 6, boardUnc), isValidSolution(boardCom))
print(startingNumbers(boardUnc))
print(isStartingNumber(1,2,8,boardUnc))
solveSudoku(boardUnc)
