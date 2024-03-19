from RumbleLib import pieces
import pytest

def test_white_piece():
  OzzyP = pieces.Piece('O',"white",6,2) #symbol, color, movement_range, attack_range
  assert OzzyP.symbol == OzzyP.symbol.upper()
 
def test_black_piece():
  BeeSwarmP = pieces.Piece('B',"black",5,3) #symbol, color, movement_range, attack_range
  assert BeeSwarmP.symbol == BeeSwarmP.symbol.lower()

def test_set_position():
  CapeKidP = pieces.Piece('K',"white",2,2)
  CapeKidP.setPosition(0,3)
  assert CapeKidP.posX == 0
  assert CapeKidP.posY == 3