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
        "numberOfPiecesP1",
        "numberOfPiecesP2",
        "pieceArrayAllP1",
        "pieceArrayAllP2",
        "pieceArrayP1",
        "pieceArrayP2",
        "time",
        "period_duration",
        "epoch_duration_seconds"
    )

    def __init__(self, boardSize, numberOfPieces):
        self.lenX = boardSize[0]
        self.lenY = boardSize[1]
        self.board = board.Board(self.lenX, self.lenY)
        self.numberOfPiecesP1 = numberOfPieces
        self.numberOfPiecesP2 = numberOfPieces
        self.pieceArrayAllP1=[]
        self.pieceArrayAllP2=[]
        self.pieceArrayP1=[]
        self.pieceArrayP2=[]
        self.loadPieceArray()

    def setupGame(self, periods_per_epoch):
        self.pickLineUp()
        self.setupTime(periods_per_epoch)

    def setupTime(self, epoch_duration_seconds, periods_per_epoch):
        self.periods_duration = 1.0/periods_per_epoch
        self.epoch_duration_seconds = epoch_duration_seconds
        self.time = 0

    def advanceTime(self):
        self.time += self.period_duration

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
        toto = list(self.pieceArrayAllP1)
        for i in range(self.numberOfPiecesP1):
            n = random.randint(0, len(toto)-1)
            self.pieceArrayP1.append(toto.pop(n))
        toto = list(self.pieceArrayAllP2)
        for i in range(self.numberOfPiecesP2):
            n = random.randint(0, len(toto)-1)
            self.pieceArrayP2.append(toto.pop(n))
    
    def randomInitialPlacement(self,rows:int =3):
        #place pieces in first 3 rows
        # Todo: add check if there are enough squares for all the pieces
        for i in range(self.numberOfPiecesP1):
            while True:
                n = random.randint(0, rows*self.lenX -1)
                PosY = n//self.lenX
                PosX = n-PosY*self.lenX
                print(self.pieceArrayP1[i].symbol, 'Px,Py:',PosX,PosY)
                if self.board.BoardPosition[PosX][PosY] == 0:
                    break
            self.pieceArrayP1[i].setPosition(PosX,PosY)
            self.board.placePiece(self.pieceArrayP1[i].symbol, PosX,PosY)

        for i in range(self.numberOfPiecesP2):
            while True:
                n = random.randint(0, rows*self.lenX -1)
                PosY = n//self.lenX
                PosX = n-PosY*self.lenX
                PosY = self.lenY - PosY - 1
                print(self.pieceArrayP2[i].symbol, 'Px,Py:',PosX,PosY)
                if self.board.BoardPosition[PosX][PosY] == 0:
                    break
            self.pieceArrayP2[i].setPosition(PosX,PosY)
            self.board.placePiece(self.pieceArrayP2[i].symbol, PosX,PosY)

    def makeMove(self,pieceA:pieces.Piece)-> list:
        # check on time for move
        if (pieceA.getNextMoveTimestamp>self.time):
            return([])

        if (pieceA.color == "white"):
            enemyPieces = self.pieceArrayP2
            numberEnemyPieces = self.numberOfPiecesP2
        else:
            enemyPieces = self.pieceArrayP1
            numberEnemyPieces = self.numberOfPiecesP1
        # Determine target square
        #first calculate distance board
        distArray = self.board.determine_movement_dist(pieceA.posX, pieceA.posY, pieceA.movement_range)
        #next iterate on enemy pieces and move to attack closest
        minEnemy = -1
        minDistance = 1000
        targetSquare = []

        for k in range(numberEnemyPieces):
            pieceB = enemyPieces[k]
            attackArray = self.board.determine_attack_dist(pieceB.posX, pieceB.posY, pieceA.attack_range)
            for i in range(self.lenX):
               for j in range(self.lenY):
                    if (distArray[i][j]<minDistance) and (attackArray[i][j]<1000):
                        minDistance = distArray[i][j]
                        minEnemy = k
                        targetSquare = [i,j]
        if (minEnemy==-1):
            return([])
        else:
            pieceA.setAttackTarget = minEnemy
            pieceA.setTargetSquare(targetSquare)
            # find next square to move to
            i = targetSquare[0]
            j = targetSquare[1]
            while (minDistance>0):
              minDistance -=1 
              if (distArray[min(i-1,0)][j] == minDistance):
                i = i-1
              elif (distArray[max(i+1,self.lenX-1)][j] == minDistance):
                 i = i+1
              elif (distArray[i][max(j+1,self.lenY-1)] == minDistance):
                 j= i+1
              elif (distArray[i][min(j-1,0)] == minDistance-1):
                 j = j-1
              else: # we should never get here
                assert (0)
            return([i,j])