from RumbleLib import pieces
import pytest

def test_white_piece():
  OzzyP = pieces.Piece('O',"white") 
  assert OzzyP.symbol == OzzyP.symbol.upper()
 
def test_black_piece():
  BeeSwarmP = pieces.Piece('B',"black") 
  assert BeeSwarmP.symbol == BeeSwarmP.symbol.lower()

def test_init():
  CapeKidP = pieces.Piece('K',"white")
  assert CapeKidP.movement_range == 9
  assert CapeKidP.attack_range == 2
  assert CapeKidP.attack_dammage == 3
  assert CapeKidP.hit_points == 30

def test_set_position():
  CapeKidP = pieces.Piece('K',"white") 
  CapeKidP.setPosition(0,3)
  assert CapeKidP.posX == 0
  assert CapeKidP.posY == 3