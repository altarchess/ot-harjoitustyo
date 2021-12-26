import unittest
from defs import BLACK_PIECE
from entity.internal_board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_make_null_move(self):
        self.board.make_null_move()
        self.assertEqual(self.board.get_active_player(), BLACK_PIECE)
