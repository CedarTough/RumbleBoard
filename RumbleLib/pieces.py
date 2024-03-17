import sys

SYMBOLS = {
 'O':'Ozzy',
 'B':'BeeSwarm',
 'K':'CapeKid'
}

class InvalidSymbol(Exception): pass
class InvalidColor(Exception): pass

def piece(symbol):
    """ Takes a piece symbol and returns the corresponding piece instance """
    if symbol in (None, ' '): return
    if symbol.isupper(): self.color = 'white'
    else: self.color = 'black'
    piece = SYMBOLS[symbol.upper()]
    return

class Piece(object):
    __slots__ = ('symbol', 'color')
    position = None

    def __init__(self, symbol,color):
        if symbol in SYMBOLS.keys:
            self.symbol = symbol
        else:
            raise InvalidSymbol 
        if color == 'white':
            self.symbol = self.symbol.upper()
            self.color = color
        elif color == 'black':
            self.symbol = self.symbol.lower()
            self.color = color
        else:
            raise InvalidColor

    @property
    def name(self): return self.__class__.__name__
    def place(self, board, position):
        """ Keep a reference to the board and position """
        self.board = board
        self.position = position

    def possible_moves(self):
        board = self.board
        boardPosition = self.boardPosition
        board_dist = [[1000 for _ in range(board.lenY)] for _ in range(board.lenX)]
        board_mark = [[-1 for _ in range(board.lenY)] for _ in range(board.lenX)]
        posX = self.position["x"]
        posY = self.position["y"]
        board_mark[posX][posY] = 0
        board_dist[posX][posY] = 0

        done = 0
        while not(done):
          done = 1
          for x in range(board.lenX):
            for y in range(board.lenY):
               if (board_mark[x][y] == 0):
                 board_mark[x][y] = - 1
                 if ((x-1>=0) and (board_dist[x-1][y]>board_dist[x][y]+1) and (board_dist[x-1][y]==0)):
                   board_dist[x-1][y] = board_dist[x][y]+1
                   board_mark[x-1][y] = 0
                   done = 0
                 if ((x+1<board.lenX) and (board_dist[x+1][y]>board_dist[x][y]+1)and (board_dist[x+1][y]==0)):
                   board_dist[x+1][y] = board_dist[x][y]+1
                   board_mark[x+1][y] = 0
                   done = 0
                 if ((y-1>=0) and (board_dist[x][y-1]>board_dist[x][y]+1)and (board_dist[x][y-1]==0)):
                   board_dist[x][y-1] = board_dist[x][y]+1
                   board_mark[x][y-1] = 0
                   done = 0
                 if ((y+1<board.lenY) and (board_dist[x][y+1]>board_dist[x][y]+1)and (board_dist[x][y+1]==0)):
                   board_dist[x][y+1] = board_dist[x][y]+1
                   board_mark[x][y+1] = 0
                   done = 0
        return map(board_dist)

    def __str__(self):
        return self.symbol.lower()

    def __repr__(self):
        return "<" + self.color.capitalize() + " " + self.__class__.__name__ + ">"

class Ozzy(Piece):
    symbol = 'O'
    range = 5

class BeeSwarm(Piece):
    symbol = 'B'
    range = 3

class CapeKid(Piece):
    symbol = 'C'
    range = 2
