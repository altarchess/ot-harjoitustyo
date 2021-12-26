import unittest
from entity.internal_board import Board
from misc.defs import N_SQUARES
import engine.ai


class TestAI(unittest.TestCase):

    """
    Luokka evaluaatio ja alpha_beta funktion testaukselle
    """

    def test_evaluate(self):
        """
        Testaa evaluaatio funktiota antamalla aseman jossa valkoisen pitäisi olla parempi, 
        ja aseman jossa mustalla pitaisi olla paremman nappulat
        """

        board = Board()
        for i in range(N_SQUARES):
            board.set_piece(i, 1)
        self.assertGreater(engine.ai.evaluate(board), 0)
        for i in range(N_SQUARES):
            board.set_piece(i, -1)
        self.assertLess(engine.ai.evaluate(board), 0)

    def test_alpha_beta(self):
        """
        Testaa alpha_beta funktiota antamalla ohjelmalle aseman jossa valkoisella pitaisi olla erinomainen asema, 
        ja aseman jossa mustalla pitäisi olla paremman nappulat 
        """

        board = Board()
        for i in range(N_SQUARES):
            board.set_piece(i, 1)
        board.set_piece(0, 0)
        board.set_piece(1, -1)
        self.assertGreater(engine.ai.alpha_beta(
            3, 0, board, -10**19, 10**19), 0)
