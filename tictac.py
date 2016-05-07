import checkmate
import copy
import collections


class TicTac(checkmate.BoardState):
    """Tic Tac Toe"""

    def __init__(self, board=None, x_turn=False):
        self.board = collections.defaultdict(lambda: None, board or [])
        self.x_turn = x_turn

    def __str__(self):
        tch = {0: 'X', 1: 'O', None: " "}
        ret = "x_turn:{}\n".format(self.x_turn)
        for y in reversed(range(3)):
            for x in range(3):
                ret += tch[self.board[(x, y)]]
            ret += "\n"
        return ret[:-1]

    def get_moves(self):
        for y in range(3):
            for x in range(3):
                if self.board[(x, y)] is None:
                    yield (x, y)

    def apply_move(self, move):
        x, y = move
        assert not self.board[(x, y)]
        new_board = copy.copy(self.board)
        new_board[(x, y)] = self.x_turn
        return TicTac(new_board, not self.x_turn)




if __name__ == '__main__':
    import random
    print TicTac()
    print list(TicTac().get_moves())
    print TicTac().apply_move(random.choice(list(TicTac().get_moves())))
    print

    board = TicTac()
    for x in xrange(1000):
        print board
        moves = list(board.get_moves())
        if moves:
            board = board.apply_move(random.choice(moves))
        else:
            break
