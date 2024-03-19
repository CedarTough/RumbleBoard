#!/usr/bin/env python
import os
import sys

if sys.version_info[0] > 3:
    print("This game runs on python 3 only")


from RumbleLib import board
from RumbleLib import pieces
#from RumbleLib import game

def printBoardPosition(boardPosition,lenX,lenY):
  for j in range(lenY-1,-1,-1):
    strl = ""
    for i in range(lenX):
        strl += str("%2s" % game.BoardPosition[i][j]) + " "
    print (strl)

def printBoardDist(distArray,lenX,lenY):
  for j in range(lenY-1,-1,-1):
    strl = ""
    for i in range(lenX):
        strl += str("%1.2f" % distArray[i][j]) + " "
    print (strl)

# initialize
board = board.Board()

#pieceX = OzzyP
#pieceX = CapeKidP
pieceX = pieces.Piece('B','white')
pieceX.setPosition(3,4)

print(pieceX.fullname, "Pos:(",pieceX.posX, ',',pieceX.posY, ') \tMoveRange:',pieceX.movement_range, '\tAttackRange:', pieceX.attack_range, '\tAttackDammage:', pieceX.attack_dammage, '\tHP:',pieceX.hit_points,'\n\n')

#distArray = game.determine_dist(CapeKidP.posX, CapeKidP.posY, CapeKid.movement_range)
distArray = board.determine_movement_dist(pieceX.posX, pieceX.posY, pieceX.movement_range)
printBoardDist(distArray,board.lenX,board.lenY)

print('\n')

attackArray = board.determine_attack_dist(pieceX.posX, pieceX.posY, pieceX.attack_range)
printBoardDist(attackArray,board.lenX,board.lenY)
print(pieces.SYMBOLS.keys())
toto = list(pieces.SYMBOLS.keys())
print(toto[3])