
from RumbleLib import pieces
from RumbleLib import board

class Game():
    """
       Game
       Class implementing the game - builds on Board and Piece classes
       TODO:
    """
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

    __slots__ = ('board','lenX','lenY','boardSize','NumberOfPieces','pieceArrayAll','pieceArrayP1','pieceArrayP2')

    def createPieceSet():
        toto = list(pieces.SYMBOLS.keys())
        pass

    def pickLineUp(color):
        pass

    def movePiece()
        return EpochEndIndicator

