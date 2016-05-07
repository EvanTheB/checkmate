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

    def rate_board(self):
        def line(a, b, c):
            if self.board[a] == self.board[b] == self.board[c]:
                return self.board[a]

        def all_lines():
            for x in range(3):
                yield ((x, 0), (x, 1), (x, 2))
                yield ((0, x), (1, x), (2, x))
            yield ((0, 0), (1, 1), (2, 2))
            yield ((2, 0), (1, 1), (0, 2))

        if any(line(a, b, c) == (not self.x_turn) for a, b, c in all_lines()):
            # Don't check for other win, they would have won already
            return float("inf")


if __name__ == '__main__':
    import random
    print TicTac()
    print list(TicTac().get_moves())
    print TicTac().apply_move(random.choice(list(TicTac().get_moves())))
    print

    # board = TicTac()
    # for x in xrange(1000):
    #     print board
    #     print board.rate_board()
    #     moves = list(board.get_moves())
    #     if moves:
    #         board = board.apply_move(random.choice(moves))
    #     else:
    #         break

    board = TicTac()
    checkmate.run_min_max(board)

