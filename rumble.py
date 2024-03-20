#!/usr/bin/env python
import os
import sys

if sys.version_info[0] > 3:
    print("This game runs on python 3 only")


from RumbleLib import game

# from RumbleLib import game

# initialize
game = game.Game([5, 8],3)
game.board.printBoardPosition()

print('Player 1 - All pieces')
for i in range(game.totalNumberOfPieces):
  game.pieceArrayAllP1[i].printPieceInfo()
print('\n')
print('Player 2 - All pieces')
for i in range(game.totalNumberOfPieces):
  game.pieceArrayAllP2[i].printPieceInfo()
print('\n')

game.pickLineUp()
print('Player 1 - randomly selected for game')
for i in range(game.numberOfPiecesP1):
  game.pieceArrayP1[i].printPieceInfo()
print('\n')
print('Player 2 - randomly selected for game')
for i in range(game.numberOfPiecesP2):
  game.pieceArrayP2[i].printPieceInfo()
print('\n')


print('Player 1 - All pieces')
for i in range(game.totalNumberOfPieces):
  game.pieceArrayAllP1[i].printPieceInfo()
print('\n')
print('Player 2 - All pieces')
for i in range(game.totalNumberOfPieces):
  game.pieceArrayAllP2[i].printPieceInfo()
print('\n')

game.randomInitialPlacement(3)
game.board.printBoardPosition()

"""
pieceX.setPosition(3, 4)
board.placePiece(pieceX.symbol, pieceX.posX, pieceX.posY)

board.printBoardPosition()

# print(pieceX.fullname, "Pos:(",pieceX.posX, ',',pieceX.posY, ') \tMoveRange:',pieceX.movement_range, '\tAttackRange:', pieceX.attack_range, '\tAttackDammage:', pieceX.attack_dammage, '\tHP:',pieceX.hit_points,'\n\n')
pieceX.printPieceInfo()

# distArray = game.determine_dist(CapeKidP.posX, CapeKidP.posY, CapeKid.movement_range)
distArray = board.determine_movement_dist(
    pieceX.posX, pieceX.posY, pieceX.movement_range
)
board.printBoardDist(distArray)

print("\n")

attackArray = board.determine_attack_dist(pieceX.posX, pieceX.posY, pieceX.attack_range)
board.printBoardDist(attackArray)
print(pieces.SYMBOLS.keys())
toto = list(pieces.SYMBOLS.keys())
print(toto[3])
"""