class Board:
    # initializer
    def __init__(self):
        self.length = input('Please neter length of the board: ')
        self.width = input('Please neter width of the board: ')
        self.grid = [['_' for i in range(int(self.length))] for rows in range(int(self.width))]

    def displayBoard(self):
        for row in self.grid:
            print('|'.join([str(elem) for elem in row]))

    def updateBoard(self):
        pass    
board = Board()
board.displayBoard()
