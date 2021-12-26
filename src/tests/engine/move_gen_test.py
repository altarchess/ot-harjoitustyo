import unittest
import copy
from entity.internal_board import Board
from engine.move_gen import MoveGen

def perft(board, depth):
    if depth == 0:
        return 1
    gen = MoveGen()
    gen.generate(board)
    node_count = 0
    for move in gen.move_list:
        new_board = copy.deepcopy(board)
        new_board.make_move(move)
        node_count += perft(new_board, depth - 1)
    return max(1, node_count)

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    # Idea on etta generoinnin pitaa tasmata taysin kaikissa asemissa tiettyyn syvyteen, joten tama
    # lienee erittain tehokas tapa testata
    def test_generate(self):
        self.assertEqual(perft(self.board, 3), 64)
        self.assertEqual(perft(self.board, 4), 340)