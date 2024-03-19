import sys

SYMBOLS = {
 'O':'Ozzy',
 'B':'BeeSwarm',
 'K':'CapeKid'
}

class InvalidSymbol(Exception): pass
class InvalidColor(Exception): pass

class Piece(object):
    __slots__ = ('symbol', 'color','movement_range','attack_range','posX','posY')
    position = None

    def __init__(self, symbol,color, movement_range, attack_range):
        if symbol.upper() in SYMBOLS.keys():
            self.symbol = symbol
        else:
            raise InvalidSymbol 
        if color == 'white':
            self.symbol = self.symbol.upper()
            self.color = color
        elif color == 'black':
            self.symbol = self.symbol.lower()
            self.color = color
        else:
            raise InvalidColor
        self.movement_range = movement_range
        self.attack_range = attack_range

    @property
    def name(self): return self.__class__.__name__

    def setPosition(self, posX, posY): 
        self.posX = posX
        self.posY = posY


    def __str__(self):
        return self.symbol.lower()

    def __repr__(self):
        return "<" + self.color.capitalize() + " " + self.__class__.__name__ + ">"

class Ozzy(Piece):
    symbol = 'O'


class BeeSwarm(Piece):
    symbol = 'B'


class CapeKid(Piece):
    symbol = 'C'

