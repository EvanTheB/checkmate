import checkmate

import copy


class Checkers(checkmate.BoardState):
    """Checkers"""

    def __init__(self, init_board=None, x_turn=True):
        if init_board:
            self.board = init_board
        else:
            self.board = [[None] * 10 for _ in range(10)]
            for x in range(10):
                self.board[x][x % 2] = 0
                self.board[x][x % 2 + 2] = 0

                self.board[x][x % 2 + 6] = 1
                self.board[x][x % 2 + 8] = 1

        self.x_turn = x_turn

    def __str__(self):
        tch = {0: 'X', 1: 'O', None: " "}
        ret = "x_turn:{}\n".format(self.x_turn)
        for y in reversed(range(10)):
            for x in range(10):
                ret += tch[self.board[x][y]]
            ret += "\n"
        return ret[:-1]

    def get_moves(self):
        yinc = 1 if self.x_turn else -1
        movers_piece = 0 if self.x_turn else 1
        not_movers_piece = 1 if self.x_turn else 0

        def get_moves_for_piece(x, y):
            if 0 > y + yinc > 9:
                return []
            moves = []

            if (0 <= x < 9 and self.board[x + 1][y + yinc] is None
                or (0 > y + 2 * yinc > 9
                    and self.board[x + 1][y + yinc] == not_movers_piece
                    and self.board[x + 2][y + yinc + yinc] is None)):
                moves.append((x, y, 1))
            if (1 <= x < 10 and self.board[x - 1][y + yinc] is None
                or (0 > y + 2 * yinc > 9
                    and self.board[x - 1][y + yinc] == not_movers_piece
                    and self.board[x - 2][y + yinc + yinc] is None)):
                moves.append((x, y, -1))
            return moves

        moves = []
        for y in range(10):
            for x in range(10):
                if self.board[x][y] == movers_piece:
                    moves += get_moves_for_piece(x, y)
        return moves

    def apply_move(self, move):
        yinc = 1 if self.x_turn else -1

        new_board = copy.deepcopy(self.board)
        piece = new_board[move[0]][move[1]]
        new_board[move[0]][move[1]] = None
        new_board[move[0] + move[2]][move[1] + yinc] = piece

        return Checkers(init_board=new_board, x_turn=not self.x_turn)

if __name__ == '__main__':
    import random

    print Checkers()
    print Checkers().get_moves()
    print Checkers().apply_move(Checkers().get_moves()[0])
    print

    board = Checkers()
    for x in xrange(1000):
        print board
        moves = board.get_moves()
        if moves:
            board = board.apply_move(random.choice(moves))
        else:
            break
    print board



