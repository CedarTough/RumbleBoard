class Board:
    """
    Royal Rumble Board
    TODO:
    """

    InitialBoardPosition = None
    BoardPosition = None

    # Create a 2D array with 3 rows and 4 columns

    def __init__(self, lenX, lenY):
        self.lenX = lenX
        self.lenY = lenY
        self.InitialBoardPosition = [
            [0 for _ in range(self.lenY)] for _ in range(self.lenX)
        ]
        self.BoardPosition = self.InitialBoardPosition

    def placePiece(self, symbol, posx, posy):
        self.BoardPosition[posx][posy] = symbol

    def clearPiece(self, symbol, posx, posy):
        if self.BoardPosition[posx][posy] == symbol:
            self.BoardPosition[posx][posy] = 0
        else:
            assert(0)

    def determine_movement_dist(self, posX, posY):
        board_dist = [[1000 for _ in range(self.lenY)] for _ in range(self.lenX)]
        board_mark = [[-1 for _ in range(self.lenY)] for _ in range(self.lenX)]
        board_mark[posX][posY] = 0
        board_dist[posX][posY] = 0

        done = 0
        while not (done):
            done = 1
            for x in range(self.lenX):
                for y in range(self.lenY):
                    if board_mark[x][y] == 0:
                        board_mark[x][y] = -1
                        if (
                            (x - 1 >= 0)
                            and (board_dist[x - 1][y] > board_dist[x][y] + 1)
                            and (self.BoardPosition[x - 1][y] == 0)
                        ):
                            board_dist[x - 1][y] = board_dist[x][y] + 1
                            board_mark[x - 1][y] = 0
                            done = 0
                        if (
                            (x + 1 < self.lenX)
                            and (board_dist[x + 1][y] > board_dist[x][y] + 1)
                            and (self.BoardPosition[x + 1][y] == 0)
                        ):
                            board_dist[x + 1][y] = board_dist[x][y] + 1
                            board_mark[x + 1][y] = 0
                            done = 0
                        if (
                            (y - 1 >= 0)
                            and (board_dist[x][y - 1] > board_dist[x][y] + 1)
                            and (self.BoardPosition[x][y - 1] == 0)
                        ):
                            board_dist[x][y - 1] = board_dist[x][y] + 1
                            board_mark[x][y - 1] = 0
                            done = 0
                        if (
                            (y + 1 < self.lenY)
                            and (board_dist[x][y + 1] > board_dist[x][y] + 1)
                            and (self.BoardPosition[x][y + 1] == 0)
                        ):
                            board_dist[x][y + 1] = board_dist[x][y] + 1
                            board_mark[x][y + 1] = 0
                            done = 0
                        """ Remove the diagonal movement
                        if (
                            (x - 1 >= 0)
                            and (y - 1 >= 0)
                            and (board_dist[x - 1][y - 1] > board_dist[x][y] + 1.414)
                            and (self.BoardPosition[x - 1][y - 1] == 0)
                        ):
                            board_dist[x - 1][y - 1] = board_dist[x][y] + 1.414
                            board_mark[x - 1][y - 1] = 0
                            done = 0
                        if (
                            (x - 1 >= 0)
                            and (y + 1 < self.lenY)
                            and (board_dist[x - 1][y + 1] > board_dist[x][y] + 1.414)
                            and (self.BoardPosition[x - 1][y + 1] == 0)
                        ):
                            board_dist[x - 1][y + 1] = board_dist[x][y] + 1.414
                            board_mark[x - 1][y + 1] = 0
                            done = 0
                        if (
                            (x + 1 < self.lenX)
                            and (y - 1 >= 0)
                            and (board_dist[x + 1][y - 1] > board_dist[x][y] + 1.414)
                            and (self.BoardPosition[x + 1][y - 1] == 0)
                        ):
                            board_dist[x + 1][y - 1] = board_dist[x][y] + 1.414
                            board_mark[x + 1][y - 1] = 0
                            done = 0
                        if (
                            (x + 1 < self.lenX)
                            and (y + 1 < self.lenY)
                            and (board_dist[x + 1][y + 1] > board_dist[x][y] + 1.414)
                            and (self.BoardPosition[x + 1][y + 1] == 0)
                        ):
                            board_dist[x + 1][y + 1] = board_dist[x][y] + 1.414
                            board_mark[x + 1][y + 1] = 0
                            done = 0
                        """
        return board_dist

    def determine_attack_dist(self, posX, posY, attack_range):
        board_dist = [[1000 for _ in range(self.lenY)] for _ in range(self.lenX)]
        board_mark = [[-1 for _ in range(self.lenY)] for _ in range(self.lenX)]
        board_mark[posX][posY] = 0
        board_dist[posX][posY] = 0

        done = 0
        while not (done):
            done = 1
            for x in range(self.lenX):
                for y in range(self.lenY):
                    if (board_mark[x][y] == 0) and (
                        board_dist[x][y] + 1 <= attack_range
                    ):
                        board_mark[x][y] = -1
                        if (
                            (x - 1 >= 0)
                            and (board_dist[x - 1][y] > board_dist[x][y] + 1)
                            and (board_dist[x][y] + 1 <= attack_range)
                        ):
                            board_dist[x - 1][y] = board_dist[x][y] + 1
                            board_mark[x - 1][y] = 0
                            done = 0
                        if (
                            (x + 1 < self.lenX)
                            and (board_dist[x + 1][y] > board_dist[x][y] + 1)
                            and (board_dist[x][y] + 1 <= attack_range)
                        ):
                            board_dist[x + 1][y] = board_dist[x][y] + 1
                            board_mark[x + 1][y] = 0
                            done = 0
                        if (
                            (y - 1 >= 0)
                            and (board_dist[x][y - 1] > board_dist[x][y] + 1)
                            and (board_dist[x][y] + 1 <= attack_range)
                        ):
                            board_dist[x][y - 1] = board_dist[x][y] + 1
                            board_mark[x][y - 1] = 0
                            done = 0
                        if (
                            (y + 1 < self.lenY)
                            and (board_dist[x][y + 1] > board_dist[x][y] + 1)
                            and (board_dist[x][y] + 1 <= attack_range)
                        ):
                            board_dist[x][y + 1] = board_dist[x][y] + 1
                            board_mark[x][y + 1] = 0
                            done = 0
                        if (
                            (x - 1 >= 0)
                            and (y - 1 >= 0)
                            and (board_dist[x - 1][y - 1] > board_dist[x][y] + 1.414)
                            and (board_dist[x][y] + 1.414 <= attack_range)
                        ):
                            board_dist[x - 1][y - 1] = board_dist[x][y] + 1.414
                            board_mark[x - 1][y - 1] = 0
                            done = 0
                        if (
                            (x - 1 >= 0)
                            and (y + 1 < self.lenY)
                            and (board_dist[x - 1][y + 1] > board_dist[x][y] + 1.414)
                            and (board_dist[x][y] + 1.414 <= attack_range)
                        ):
                            board_dist[x - 1][y + 1] = board_dist[x][y] + 1.414
                            board_mark[x - 1][y + 1] = 0
                            done = 0
                        if (
                            (x + 1 < self.lenX)
                            and (y - 1 >= 0)
                            and (board_dist[x + 1][y - 1] > board_dist[x][y] + 1.414)
                            and (board_dist[x][y] + 1.414 <= attack_range)
                        ):
                            board_dist[x + 1][y - 1] = board_dist[x][y] + 1.414
                            board_mark[x + 1][y - 1] = 0
                            done = 0
                        if (
                            (x + 1 < self.lenX)
                            and (y + 1 < self.lenY)
                            and (board_dist[x + 1][y + 1] > board_dist[x][y] + 1.414)
                            and (board_dist[x][y] + 1.414 <= attack_range)
                        ):
                            board_dist[x + 1][y + 1] = board_dist[x][y] + 1.414
                            board_mark[x + 1][y + 1] = 0
                            done = 0
        return board_dist

    def printBoardPosition(self):
        for j in range(self.lenY - 1, -1, -1):
            strl = ""
            for i in range(self.lenX):
                strl += str("%2s" % self.BoardPosition[i][j]) + " "
            print(strl)

    def printBoardDist(self, distArray):
        for j in range(self.lenY - 1, -1, -1):
            strl = ""
            for i in range(self.lenX):
                strl += str("%1.2f" % distArray[i][j]) + " "
            print(strl)
