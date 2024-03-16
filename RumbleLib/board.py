import pieces

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
    
    
    #captured_pieces = { 'white': [], 'black': [] }
    player_turn = None
    halfmove_clock = 0
    fullmove_number = 1
    history = []
    InitialBoardPosition = [0]*len(axis_y)*len(axis_x)
    BoardPosition = [0]*len(axis_y)*len(axis_x)

    def __init__(self, fen = None):
        if fen is None: 
            BoardPosition = InitialBoardPosition
        else: 
            BoardPosition = fen
