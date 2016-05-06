import checkmate


class Checkers(checkmate.BoardState):
    """Checkers"""

    def __init__(self):
        self.board = [[None] * 10 for _ in range(10)]
        for x in range(10):
            self.board[x][x % 2] = 0
            self.board[x][x % 2 + 2] = 0

            self.board[x][x % 2 + 6] = 1
            self.board[x][x % 2 + 8] = 1

        self.x_turn = True

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

if __name__ == '__main__':
    print str(Checkers())
    print Checkers().get_moves()
