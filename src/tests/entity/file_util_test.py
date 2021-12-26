import unittest
import copy
from entity.file_util import Loader
from entity.internal_board import Board

class TestLoader(unittest.TestCase):
    def setUp(self):
        self.loader = Loader()

    def test_dec_cursor(self):
        for i in range (len(self.loader.states)):
            self.loader.dec_cursor()
            self.assertEqual(self.loader.cursor, max(0, len(self.loader.states) - i - 2))

    def test_inc_cursor(self):
        for i in range (len(self.loader.states)):
            self.loader.dec_cursor()
        for i in range (len(self.loader.states) + 1):
            self.loader.inc_cursor()
            self.assertEqual(self.loader.cursor, min(len(self.loader.states) - 1 , i + 1))

    def test_add(self):
        board = Board()
        self.loader.add(board)
        self.assertEqual(board.get_piece_on_square(28), self.loader.states[len(self.loader.states) - 1].get_piece_on_square(28))
