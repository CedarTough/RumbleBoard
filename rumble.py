#!/usr/bin/env python
import os
import sys

if sys.version_info[0] > 3:
    print("This game runs on python 3 only")


from RumbleLib import board
from RumbleLib import pieces

# initialize
game = board.Board()


OzzyP = pieces.Piece('O',"white",6,2,2,20)
OzzyP.setPosition(3,4)
game.placePiece(OzzyP.symbol,OzzyP.posX,OzzyP.posY)
print(game.BoardPosition[3][4])

BeeSwarmP = pieces.Piece('B',"black",5,3,3,25)
BeeSwarmP.setPosition(3,6)
game.placePiece(BeeSwarmP.symbol,BeeSwarmP.posX,BeeSwarmP.posY)
print(game.BoardPosition[3][6])

CapeKidP = pieces.Piece('K',"white",2,2,5,30)
CapeKidP.setPosition(0,0)
game.placePiece(CapeKidP.symbol,CapeKidP.posX,CapeKidP.posY)
print(game.BoardPosition[0][0])

for j in range(game.lenY-1,-1,-1):
    strl = ""
    for i in range(game.lenX):
        strl += str(game.BoardPosition[i][j]) + " "
    print (strl)

print("\n")

#pieceX = OzzyP
#pieceX = CapeKidP
pieceX = BeeSwarmP

print('Bee Swarm', pieceX.posX, pieceX.posY, pieceX.movement_range, pieceX.attack_range, '\n\n')

#distArray = game.determine_dist(CapeKidP.posX, CapeKidP.posY, CapeKid.movement_range)
distArray = game.determine_movement_dist(pieceX.posX, pieceX.posY, pieceX.movement_range)
for j in range(game.lenY-1,-1,-1):
    strl = ""
    for i in range(game.lenX):
        strl += str("%1.2f" % distArray[i][j]) + " "
    print (strl)

print("\n")

distArray = game.determine_attack_dist(pieceX.posX, pieceX.posY, pieceX.attack_range)
for j in range(game.lenY-1,-1,-1):
    strl = ""
    for i in range(game.lenX):
        strl += str("%1.2f" % distArray[i][j]) + " "
    print (strl)