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


def run_a_star(initial_board):
    return initial_board.get_moves()[0]
