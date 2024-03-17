from RumbleLib import board
import pytest

def test_board_axis():
  board1 = board.Board()
  assert "A" in board1.axis_x
  assert "E" in board1.axis_x
  assert 1 in board1.axis_y
  assert 8 in board1.axis_y
  assert board1.lenX == 5
  assert board1.lenY == 8

def test_board_position():
  board1 = board.Board()
  assert board1.BoardPosition[board1.lenX-1][board1.lenY-1] == 0
  assert board1.InitialBoardPosition[board1.lenX-1][board1.lenY-1] == 0