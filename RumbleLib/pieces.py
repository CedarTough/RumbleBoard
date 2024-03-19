SYMBOLS = {
    # symbol: name, movement_range,attack_range, attack_dammage, hit_points
 'B':['BeeSwarm', 6, 1, 1, 30],
 'C':['ChocolatePrince',6, 1, 1, 30],
 'CB':['CabbageMoth',6, 1, 1, 30],
 'CH':['ChubChub',6, 1, 1, 30],
 'D':['Detective',6, 1, 1, 30],
 'F':['DrFertilizer',6, 1, 1, 30],
 'G':['GingerbreadMan',6, 1, 1, 30],
 'GM':['GMachina',6, 1, 1, 30],
 'K':['CapeKid',6, 1, 1, 30],
 'L':['LostPrincess',6, 1, 1, 30],
 'LC':['LittleCake',6, 1, 1, 30],
 'M':['Magician',6, 1, 1, 30],
 'MD':['MarshmallowDuck',6, 1, 1, 30],
 'N':['Ninja',6, 1, 1, 30],
 'O':['Ozzy',6, 1, 1, 30],
 'P':['Pterodactyle',6, 1, 1, 30],
 'S':['SugarAddict',6, 1, 1, 30],
 'T':['Tarantula',6, 1, 1, 30],
 'V':['VolleyballLongshot',6, 1, 1, 30],
 'W':['WildPlant',6, 1, 1, 30]
 }

class InvalidSymbol(Exception): pass
class InvalidColor(Exception): pass

class Piece(object):
    __slots__ = ('symbol', 'color','movement_range','attack_range', 'attack_dammage', 'hit_points', 'posX','posY')

    def __init__(self, symbol,color,movement_range,attack_range, attack_dammage, hit_points):
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
        toto = SYMBOLS[symbol.upper]
        self.movement_range = toto[1]
        self.attack_range = toto[2]
        self.attack_dammage = toto[3]
        self.hit_points = toto[4]


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

