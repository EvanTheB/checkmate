import checkmate

class Checkers(checkmate.BoardState):
    """Checkers"""
    def __init__(self):
        self.board = [[None]*10 for _ in range(10)]
        for x in range(10):
            self.board[x][x%2] = 0
            self.board[x][x%2 + 2] = 0

            self.board[x][x%2 + 6] = 1
            self.board[x][x%2 + 8] = 1

        self.white_turn = True

    def __str__(self):
        tch = {0:'X', 1:'O', None:" "}
        ret = "white_turn:{}\n".format(self.white_turn)
        for y in reversed(range(10)):
            for x in range(10):
                ret += tch[self.board[x][y]]
            ret += "\n"
        return ret[:-1]



if __name__ == '__main__':
    print str(Checkers())