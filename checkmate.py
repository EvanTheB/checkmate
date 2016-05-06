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

    def rate_board():
        """rate board for search algorithm"""
        raise NotImplementedError()
        return 0.0
