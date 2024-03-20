from RumbleLib import pieces
from RumbleLib import board
import random


class Game:
    """
    Game
    Class implementing the game - builds on Board and Piece classes
    TODO:
    """

    __slots__ = (
        "board",
        "lenX",
        "lenY",
        "totalNumberOfPieces",
        "numberOfPieces",
        "pieceArrayAllP1",
        "pieceArrayAllP2",
        "pieceArrayP1",
        "pieceArrayP2",
    )

    def __init__(self, boardSize, numberOfPieces):
        self.lenX = boardSize[0]
        self.lenY = boardSize[1]
        self.board = board.Board(self.lenX, self.lenY)
        self.numberOfPieces = numberOfPieces
        self.pieceArrayAllP1=[]
        self.pieceArrayAllP2=[]
        self.pieceArrayP1=[]
        self.pieceArrayP2=[]
        self.loadPieceArray()

    def setupGame(self):
        self.pickLineUp()

    def printBoardPosition(self, BoardPosition):
        for j in range(self.lenY - 1, -1, -1):
            strl = ""
            for i in range(self.lenX):
                strl += str("%2s" % BoardPosition[i][j]) + " "
        print(strl)

    def printBoardDist(self, distArray):
        for j in range(self.lenY - 1, -1, -1):
            strl = ""
            for i in range(self.lenX):
                strl += str("%1.2f" % distArray[i][j]) + " "
        print(strl)

    def loadPieceArray(self):
        toto = list(pieces.SYMBOLS.keys())
        self.totalNumberOfPieces = len(toto)
        pieceArrayAll = []
        for i in range(self.totalNumberOfPieces):
            self.pieceArrayAllP1.append(pieces.Piece(toto[i], "white"))
            self.pieceArrayAllP2.append(pieces.Piece(toto[i], "black"))

    def pickLineUp(self):
        random.seed()
        toto = self.pieceArrayAllP1
        for i in range(self.numberOfPieces):
            n = random.randint(0, len(toto)-1)
            self.pieceArrayP1.append(toto.pop(n))
        toto = self.pieceArrayAllP2
        for i in range(self.numberOfPieces):
            n = random.randint(0, len(toto)-1)
            self.pieceArrayP2.append(toto.pop(n))

    def makeMove(self):
        pass
