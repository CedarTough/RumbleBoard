
from RumbleLib import pieces
from RumbleLib import board

class Game():
    """
       Board
       A simple RumbleBoard class
       TODO:
    """
    def printBoard(self):
        for j in range(self.lenY-1,-1,-1):
         strl = ""
          for i in range(self.lenX):
            strl += str("%1.2f" % self.board.distArray[i][j]) + " "
        print (strl)

