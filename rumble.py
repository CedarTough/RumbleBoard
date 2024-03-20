#!/usr/bin/env python
import os
import sys
import time

if sys.version_info[0] > 3:
    print("This game runs on python 3 only")


from RumbleLib import game

# from RumbleLib import game

# initialize
game = game.Game([7, 8],3) # 7x8 board, 3 pieces per side
game.board.printBoardPosition()

print('Player 1 - All pieces')
for i in range(game.totalNumberOfPieces):
  game.pieceArrayAllP1[i].printPieceInfo()
print('\n')
print('Player 2 - All pieces')
for i in range(game.totalNumberOfPieces):
  game.pieceArrayAllP2[i].printPieceInfo()
print('\n')

game.setupGame(10, 10)   # 1 second per epoch, 10 update periods per epoch
print('Player 1 - randomly selected for game')
for i in range(game.numberOfPiecesP1):
  game.pieceArrayP1[i].printPieceInfo()
print('\n')
print('Player 2 - randomly selected for game')
for i in range(game.numberOfPiecesP2):
  game.pieceArrayP2[i].printPieceInfo()
print("Epoch in s: ",game.epoch_duration_seconds,"\t Update period in s:", game.period_duration)
print("Current time in s:", game.time)
print('\n')

game.randomInitialPlacement(3) #random placement in first 3 rows
print("time:",game.time)
game.board.printBoardPosition()

for i in range(20):
  game.advanceTime()
  game.makeMove(game.pieceArrayP1[0],1)
  print("time:",game.time)
  game.board.printBoardPosition()
  time.sleep(game.period_duration)
'''
game.randomInitialPlacement(3)
print('Initial placement:')
game.board.printBoardPosition()
print('\n')
'''
