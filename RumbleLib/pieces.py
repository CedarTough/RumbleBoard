SYMBOLS = {
    # symbol: fullname, movement_range,attack_range, attack_damage, hit_points
    "B": ["BeeSwarm", 6, 1, 1, 30],
    "C": ["ChocolatePrince", 2, 2, 2, 25],
    "CB": ["CabbageMoth", 3, 3, 3, 20],
    "CH": ["ChubChub", 4, 2, 1, 15],
    "D": ["Detective", 5, 7, 1, 10],
    "F": ["DrFertilizer", 6, 2, 3, 15],
    "G": ["GingerbreadMan", 7, 3, 1, 20],
    "GM": ["GMachina", 8, 6, 1, 18],
    "K": ["CapeKid", 9, 2, 2, 30],
    "L": ["LostPrincess", 10, 10, 1, 6],
    "LC": ["LittleCake", 1, 1, 2, 20],
    "M": ["Magician", 2, 2, 3, 15],
    "MD": ["MarshmallowDuck", 3, 3, 2, 10],
    "N": ["Ninja", 4, 1, 4, 15],
    "O": ["Ozzy", 5, 2, 5, 20],
    "P": ["Pterodactyle", 6, 3, 2, 25],
    "S": ["SugarAddict", 7, 1, 1, 30],
    "T": ["Tarantula", 8, 2, 2, 25],
    "V": ["VolleyballLongshot", 9, 3, 6, 20],
    "W": ["WildPlant", 10, 1, 4, 15],
}


class InvalidSymbol(Exception):
    pass


class InvalidColor(Exception):
    pass


class Piece(object):
    __slots__ = (
        "symbol",
        "fullname",
        "color",
        "movement_range",
        "attack_range",
        "attack_damage",
        "hit_points",
        "posX",
        "posY",
        "next_movement_timestamp",
        "target_square",
        "attack_target",
        "movement_periodicity"
    )

    def __init__(self, symbol, color):
        if symbol.upper() in SYMBOLS.keys():
            self.symbol = symbol
        else:
            raise InvalidSymbol
        if color == "white":
            self.symbol = self.symbol.upper()
            self.color = color
        elif color == "black":
            self.symbol = self.symbol.lower()
            self.color = color
        else:
            raise InvalidColor
        toto = SYMBOLS[symbol.upper()]
        self.fullname = toto[0]
        self.movement_range = toto[1]
        self.attack_range = toto[2]
        self.attack_damage = toto[3]
        self.hit_points = toto[4]
        self.posX = -1
        self.posY = -1
        self.next_movement_timestamp = 0
        self.attack_target = -1
        self.target_square = None

    @property
    def name(self):
        return self.__class__.__name__

    def setPosition(self, posX, posY):
        self.posX = posX
        self.posY = posY

    def setMoveParameter(self, epoch_duration,periods_per_epoch):
        self.movement_periodicity = epoch_duration/self.movement_range - 0.0000001
        self.next_movement_timestamp = self.movement_periodicity - 0.0000001

    def updateNextMoveTimestamp(self):
        self.next_movement_timestamp += self.movement_periodicity - 0.0000001

    def getNextMoveTimestamp(self) -> float:
        return(self.next_movement_timestamp)

    def setAttackTarget(self, enemy_piece_number):
        self.attack_target = enemy_piece_number
    
    def getAttackTarget(self)-> int:
        return(self.attack_target)
    
    def receiveDamage(self, damage)-> int:
        self.hit_points = max(0, self.hit_points - damage)
        return(self.hit_points)
    
    def setTargetSquare(self, target_square:list = None):
        self.target_square = target_square
    
    def getTargetSquare(self)-> list:
        return(self.target_square)
    
    def dead(self)-> bool:
        if (self.hit_points == 0):
            return(1)
        else:
            return(0)
    def __str__(self):
        return self.symbol.lower()

    def __repr__(self):
        return "<" + self.color.capitalize() + " " + self.__class__.__name__ + ">"

    def printPieceInfo(self):
        print(
            "'", self.symbol, "'",
            self.fullname,
            "Pos:(",
            self.posX,
            ",",
            self.posY,
            ") \tMoveRange:",
            self.movement_range,
            "\tAttackRange:",
            self.attack_range,
            "\tAttackDamage:",
            self.attack_damage,
            "\tHP:",
            self.hit_points
        )


class Ozzy(Piece):
    symbol = "O"


class BeeSwarm(Piece):
    symbol = "B"


class CapeKid(Piece):
    symbol = "C"
