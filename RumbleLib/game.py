from RumbleLib import pieces
from RumbleLib import board
import random

class Game():
    """
       Game
       Class implementing the game - builds on Board and Piece classes
       TODO:
    """
    __slots__ = ('board','lenX','lenY', 'totalNumberOfPieces','numberOfPieces','pieceArrayAllP1','pieceArrayAllP2','pieceArrayP1','pieceArrayP2')
  
    def __init__(self, boardSize, numberOfPieces):
        self.lenX = boardSize[0]
        self.lenY = boadSize[1]
        self.board = board.Board(self.lenX,self.lenY)
        self.numberOfPieces = numberOfPieces
        self.loadPieceArray()

    def setupGame(self):
        self.pickLineUp()
   
    def printBoardPosition(self, BoardPosition):
        for j in range(self.lenY-1,-1,-1):
          strl = ""
            for i in range(self.lenX):
                strl += str("%2s" % BoardPosition[i][j]) + " "
        print (strl)

    def printBoardDist(self, distArray):
        for j in range(self.lenY-1,-1,-1):
            strl = ""
            for i in range(self.lenX):
                strl += str("%1.2f" % distArray[i][j]) + " "
        print (strl)


    def loadPieceArray():
        toto = list(pieces.SYMBOLS.keys())
        self.totalNumberOfPieces = len(toto)
        pieceArrayAll = []
        for i in range(self.totalNumberOfPieces):
            pieceArrayAllP1[i] = pieces.Piece(toto[i],'white')
            pieceArrayAllP2[i] = pieces.Piece(toto[i],'black')

    def pickLineUp(self):
        random.seed()
        toto = self.pieceArrayAllP1
        for i in range (self.numberOfPieces):
            n = randint(0,len(toto))
                pieceArrayP1[i] = toto.pop(n)
        toto = self.pieceArrayAllP2
        for i in range (self.numberOfPieces):
            n = randint(0,len(toto))
                pieceArrayP2[i] = toto.pop(n)

    def makeMove(self):
       pass
    