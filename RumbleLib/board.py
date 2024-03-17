from RumbleLib import pieces

#class ChessError(Exception): pass
#class InvalidCoord(ChessError): pass
#class InvalidColor(ChessError): pass
#class InvalidMove(ChessError): pass
#class Check(ChessError): pass
#class CheckMate(ChessError): pass
#class Draw(ChessError): pass
#class NotYourTurn(ChessError): pass


class Board(dict):
    """
       Board
       A simple RumbleBoard class
       TODO:
    """

    axis_x = ('A', 'B', 'C', 'D', 'E')
    axis_y = tuple(range(1,9)) # (1,2,3,...8)
    lenX = len(axis_x)
    lenY = len(axis_y)
    
    #captured_pieces = { 'white': [], 'black': [] }
    player_turn = None
    halfmove_clock = 0
    fullmove_number = 1
    history = []
    InitialBoardPosition
    BoardPosition
    
    # Create a 2D array with 3 rows and 4 columns
   
    def __init__(fen = None):
        InitialBoardPosition = [[0 for _ in range(self.lenY)] for _ in range(self.lenX)]
        if fen is None: 
            BoardPosition = InitialBoardPosition
        else: 
            BoardPosition = fen
