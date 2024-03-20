from RumbleLib import board
import pytest

def test_board_axis():
  board1 = board.Board(5,8)
  assert board1.lenX == 5
  assert board1.lenY == 8

def test_board_initial_position():
  board1 = board.Board(5,8)
  assert board1.BoardPosition[board1.lenX-1][board1.lenY-1] == 0
  assert board1.InitialBoardPosition[board1.lenX-1][board1.lenY-1] == 0

def test_place_piece():
  game = board.Board(5,8)
  game.placePiece('O',game.lenX-1,game.lenY-1)
  assert game.BoardPosition[game.lenX-1][game.lenY-1]

def test_determine_movement_dist():
  game = board.Board(5,8)
  game.placePiece('O',game.lenX-1,game.lenY-1)
  game.placePiece('B',game.lenX-2,game.lenY-1)
  dist_array = game.determine_movement_dist(game.lenX-1,game.lenY-1, 3)
  assert dist_array[game.lenX-2][game.lenY-1]==1000
  assert dist_array[game.lenX-1][game.lenY-2]==1
  assert dist_array[game.lenX-2][game.lenY-2]==1.414
  assert dist_array[0][0]==1000

def test_determine_attack_dist():
  game = board.Board(5,8)
  game.placePiece('O',game.lenX-1,game.lenY-1)
  game.placePiece('B',game.lenX-2,game.lenY-1)
  dist_array = game.determine_attack_dist(game.lenX-1,game.lenY-1, 2)
  assert dist_array[game.lenX-2][game.lenY-1]==1
  assert dist_array[game.lenX-1][game.lenY-2]==1
  assert dist_array[game.lenX-2][game.lenY-2]==1.414
  assert dist_array[0][0]==1000