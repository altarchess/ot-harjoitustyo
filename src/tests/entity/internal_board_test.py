import unittest
import random
from defs import BLACK_PIECE, ONGOING, WHITE_WIN, BLACK_WIN, N_SQUARES
from entity.internal_board import Board, x_from_square, y_from_square
from entity.internal_board import square_from_xy
from engine.move_gen import Move

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_x_from_square(self):
        self.assertEqual(x_from_square(12), 4)

    def test_y_from_square(self):
        self.assertEqual(y_from_square(12), 1)

    def test_square_from_xy(self):
        self.assertEqual(square_from_xy(4, 1), 12)

    def test_set_piece(self):
        for i in range(N_SQUARES):
            random_piece = random.randint(-1, 1)
            self.board.set_piece(i, random_piece)
            self.assertEqual(random_piece, self.board.get_piece_on_square(i))

    def test_get_piece_on_square(self):
        self.assertEqual(0, self.board.get_piece_on_square(-1))
        for i in range(N_SQUARES):
            random_piece = random.randint(-1, 1)
            self.board.set_piece(i, random_piece)
            self.assertEqual(random_piece, self.board.get_piece_on_square(i))

    def test_get_piece_on_cord(self):
        self.assertEqual(0, self.board.get_piece_on_cord(-1, -1))
        for i in range(N_SQUARES):
            random_piece = random.randint(-1, 1)
            self.board.set_piece(i, random_piece)
            self.assertEqual(random_piece, self.board.get_piece_on_cord(x_from_square(i), y_from_square(i)))

    def test_make_move(self):
        self.board.make_move(Move(0, 2, 1, 1))
        self.assertEqual(1, self.board.get_piece_on_square(1))
        self.assertEqual(0, self.board.get_piece_on_square(3))
        self.board.make_move(Move(0, 5, 1, 1))
        self.assertEqual(1, self.board.get_piece_on_square(3))

    def test_is_win(self):
        self.assertEqual(ONGOING, self.board.is_win())
        for i in range(N_SQUARES):
            self.board.set_piece(i, 1)
        self.assertEqual(WHITE_WIN, self.board.is_win())
        for i in range(N_SQUARES):
            self.board.set_piece(i, -1)
        self.assertEqual(BLACK_WIN, self.board.is_win())

    def test_make_null_move(self):
        self.board.make_null_move()
        self.assertEqual(self.board.get_active_player(), BLACK_PIECE)
