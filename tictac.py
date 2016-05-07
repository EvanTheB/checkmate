import checkmate

import collections

class TicTac(checkmate.BoardState):
    """Tic Tac Toe"""
    def __init__(self):
        self.board = collections.defaultdict(lambda: None)
        self.x_turn = True

    def __str__(self):
        tch = {0: 'X', 1: 'O', None: " "}
        ret = "x_turn:{}\n".format(self.x_turn)
        for y in reversed(range(3)):
            for x in range(3):
                ret += tch[self.board[(x,y)]]
            ret += "\n"
        return ret[:-1]


if __name__ == '__main__':
    print TicTac()