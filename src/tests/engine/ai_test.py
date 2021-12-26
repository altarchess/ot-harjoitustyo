import unittest
from entity.internal_board import Board
from misc.defs import N_SQUARES
import engine.ai

class TestBoard(unittest.TestCase):

    # Idea on etta generoinnin pitaa tasmata taysin kaikissa asemissa tiettyyn syvyteen, joten tama
    # lienee erittain tehokas tapa testata
    def test_evaluate(self):
        board = Board()
        for i in range(N_SQUARES):
            board.set_piece(i, 1)
        self.assertGreater(engine.ai.evaluate(board), 0)
        for i in range(N_SQUARES):
            board.set_piece(i, -1)
        self.assertLess(engine.ai.evaluate(board), 0)

    def test_alpha_beta(self):
        board = Board()
        for i in range(N_SQUARES):
            board.set_piece(i, 1)
        board.set_piece(0, 0)
        board.set_piece(1, -1)
        self.assertGreater(engine.ai.alpha_beta(3, 0, board, -10**19, 10**19), 0)
