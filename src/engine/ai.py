import copy
from defs import *
from engine.move_gen import MoveGen


def alpha_beta(depth, ply, board, alpha, beta):
    if depth == 0:
        return evaluate(board)
    score = -10**11
    gen = MoveGen()
    gen.generate(board)
    best_move = -1
    for move in gen.move_list:
        new_board = copy.deepcopy(board)
        new_board.make_move(move)
        new_score = -alpha_beta(depth - 1, ply + 1, new_board, -beta, -alpha)
        if new_score > score:
            score = new_score
            best_move = move
        alpha = max(score, alpha)
        if alpha >= beta:
            return alpha
    if ply == 0:
        board.best_move = best_move
    return score


def evaluate(board):
    pst_score = 0
    for i in range(N_SQUARES):
        pst_score += board.get_piece_on_square(i) * (PST[i] + 50)
    return pst_score * board.get_active_player()
