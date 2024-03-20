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
print('Initial placement:')
game.board.printBoardPosition()
print('\n')


for i in range(game.numberOfPiecesP1):
  game.pieceArrayP1[i].printPieceInfo()
print('\n')
print('Player 2 - randomly selected for game')
for i in range(game.numberOfPiecesP2):
  game.pieceArrayP2[i].printPieceInfo()
print('\n')


