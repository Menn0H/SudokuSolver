#!/usr/bin/env python3
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


class Sudoku:
    def __init__(self, board):
        self.board = board

    #returns in which square (1-9) the position is in
    def getSquareNum(self, x, y):
        x1, x2, y1, y2= [0,3,6], [2,5,8], [0,3,6], [2,5,8]
        count = 1
        
        for i in range(3):
            for j in range(3):
                if x >= x1[i] and y >= y1[j] and x <= x2[i] and y <= y2[j]:
                    return count
                else:
                    count += 1
        
    #returns an array which represents a square
    def getSquare(self, n):
        count = 1
        
        for i in [0,3,6]:
            for j in [0,3,6]:
                if n == count:
                    return self.square(i,j)
                else:
                    count += 1
            
    def square(self, x, y):
        square = []
        realy = y
        for i in range(3):
            for j in range(3):
                square.append(self.board[x][y])	
                y += 1
            x += 1
            y = realy

        return square

    #returns if number played on position x,y is valid
    def isValidMove(self, x, y, num):
        row = self.board[x]
        row = [i for i in row if i != 0]

        col = []
        for i in range(9):
            col.append(self.board[i][y])	
        col = [i for i in col if i != 0]

        sqr = self.getSquare(self.getSquareNum(x,y))	
        sqr = [i for i in sqr if i != 0]

        if self.allUnique(row) and self.allUnique(col) and self.allUnique(sqr):
            return True
        else:
            return False

    def allUnique(self, n):
        seen = set()
        return not any(i in seen or seen.add(i) for i in n)

    def isValidSolution(self):
        bools = []

        for i in range(9):
            for j in range(9):
                bools.append(self.isValidMove(i, j, self.board[i][j]))
        return all(bools)

    def printBoard(self):
        for i in self.board:
            print(i)

    def startingNumbers(self):
        numbers = []

        for i in range(9):
            for j in range(9):
                if self.board[i][j] != 0:
                    numbers.append((i, j, self.board[i][j]))
        
        return numbers

    def isStartingNumber(self, x, y, num, startNum):
        outcome = False	

        for i in startNum:
            if i[0] == x and i[1] == y and i[2] == num:
                outcome = True
        
        return outcome

    def solveSudoku(self):
        i, j = 0, 0
        startNum = self.startingNumbers()
        number = 1
        noValidMove = False

        while i < 9:
            while j < 9:
                if i >= 9:
                    break
                elif not self.isStartingNumber(i, j, self.board[i][j], startNum):
                    if noValidMove:
                        self.board[i][j] += 1
                        number = self.board[i][j]
                        noValidMove = False
                    else:
                        self.board[i][j] = number
                        if number > 9:
                            self.board[i][j] = 0
                            j -= 1
                            if j < 0:
                                j = 8
                                i -= 1
                            noValidMove = True
                            number = 1
                        elif self.isValidMove(i, j, number):
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

if __name__ == '__main__':
    s = Sudoku(boardUnc)
    s.printBoard()
    print('\n')

    s.solveSudoku()
    s.printBoard()
