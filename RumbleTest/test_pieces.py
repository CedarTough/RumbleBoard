from RumbleLib import pieces
import pytest

def test_white_piece():
  OzzyP = pieces.Piece('O',"white",6,2,4,20) #symbol, color, movement_range, attack_range, attack_dammage, hit_points
  assert OzzyP.symbol == OzzyP.symbol.upper()
 
def test_black_piece():
  BeeSwarmP = pieces.Piece('B',"black",5,3,2,15) #symbol, color, movement_range, attack_range, attack_dammage, hit_points
  assert BeeSwarmP.symbol == BeeSwarmP.symbol.lower()

def test_init():
  CapeKidP = pieces.Piece('K',"white",2,3,1,18) #symbol, color, movement_range, attack_range, attack_dammage, hit_points
  assert CapeKidP.movement_range == 2
  assert CapeKidP.attack_range == 3
  assert CapeKidP.attack_dammage == 1
  assert CapeKidP.hit_points == 18

def test_set_position():
  CapeKidP = pieces.Piece('K',"white",2,2,3,18) #symbol, color, movement_range, attack_range, attack_dammage, hit_points
  CapeKidP.setPosition(0,3)
  assert CapeKidP.posX == 0
  assert CapeKidP.posY == 3