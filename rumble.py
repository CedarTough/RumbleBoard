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

game.setupGame(10, 10)   # 10 seconds per epoch, 10 update periods per epoch
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

for epochs in range(10):
  for periods in range(game.periods_per_epoch):
    game.advanceTime()
    print("time:",game.time)
    if(game.numberOfPiecesP1>game.numberOfPiecesP2):
      MM = game.numberOfPiecesP1
      P1P = 1 - 0.000001
      P2P = game.numberOfPiecesP1/game.numberOfPiecesP2-0.000001
    else:
      MM = game.numberOfPiecesP2
      P2P = 1 - 0.000001
      P1P = game.numberOfPiecesP2/game.numberOfPiecesP1-0.000001
    print('MM:',MM,'P1P:',P1P, 'P2P:', P2P)
    P1counter = 0
    P1PieceNumber = 0
    P2counter = 0
    P2PieceNumber = 0
    for k in range(MM):
      if (P1counter<=k):
        while(game.makeMove(game.pieceArrayP1[P1PieceNumber],1)):
          pass
        P1PieceNumber += 1
        P1counter += P1P
      if (P2counter<=k):
        while(game.makeMove(game.pieceArrayP2[P2PieceNumber],1)):
          pass
        P2PieceNumber += 1
        P2counter += P2P
    game.board.printBoardPosition()
    time.sleep(game.period_duration)
