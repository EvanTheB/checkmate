class BoardState(object):
    """ABC for boardstate"""

    def get_moves():
        """all possible moves to get new boards"""
        raise NotImplementedError()
        return []

    def apply_move(move):
        """return new Boardstate after making move"""
        raise NotImplementedError()
        return BoardState()

    def game_done():
        """True if the game is done. IE a winner or no possible moves."""
        raise NotImplementedError()
        return False

    def rate_board():
        """rate board for search algorithm
        +ve for states good for the player whos turn it is.
        """
        raise NotImplementedError()
        return 0.0


def run_min_max(initial_board):
    def min_max_rec(board, maximise):
        moves = list(board.get_moves())
        if len(moves) == 0 or board.game_done():
            return (board.rate_board() * maximise, None)

        if maximise > 0:
            return max(((min_max_rec(board.apply_move(m), -1)[0], m) for m in moves), key=lambda x: x[0])
        else:
            return min(((min_max_rec(board.apply_move(m), +1)[0], m) for m in moves), key=lambda x: x[0])
    return min_max_rec(initial_board, 1)


def run_alpha_beta(initial_board):
    def min_max_rec(board, maximise, alpha, beta):
        moves = list(board.get_moves())
        if len(moves) == 0 or board.game_done():
            return (board.rate_board() * maximise, None)

        if maximise > 0:
            best = (float("-inf"), None)
            for m in moves:
                cur = min_max_rec(board.apply_move(m), -1,
                                  alpha, beta)
                best = max((cur[0], m), best)
                alpha = max(best[0], alpha)
                if beta <= alpha:
                    # print board
                    # print maximise, alpha, beta, best
                    # print
                    # best = (alpha, None)
                    break
        else:
            best = (float("inf"), None)
            for m in moves:
                best = min((min_max_rec(board.apply_move(m), +1,
                                        alpha, beta)[0], m), best)
                beta = min(best[0], beta)
                if beta <= alpha:
                    # print board
                    # print repr(board)
                    # print maximise, alpha, beta, best
                    # print
                    # best = (beta, None)
                    break
        # mm = run_min_max(board)
        # mm = mm[0]*maximise, mm[1]
        # if mm[0] != best[0]:
        #     pass
        return best
    return min_max_rec(initial_board, 1, float("-inf"), float("inf"))


def run_a_star(initial_board):
    return initial_board.get_moves()[0]
