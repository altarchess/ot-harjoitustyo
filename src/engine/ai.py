import copy
from misc.defs import *
from engine.move_gen import MoveGen


def alpha_beta(depth, ply, board, alpha, beta):
    """
    Alpha-Beta on minimaxin algoritmin tehostus (https://www.chessprogramming.org/Alpha-Beta).
    Tarkkaan ottaen tama on Alpha-Beta negamaxin paalla (https://www.chessprogramming.org/Negamax).

    Args: 
        depth: kuinka paljon syvemalle meidan on viela tutkailtava puuta
        ply: kuinka syvalla ollaan puun juureen verrattuna
        board: othello-lauta objekti
        Alpha & Beta: Alpha-Beta algoritmin Alpha ja Beta


    Returns:
        Puun minimax optimaalinen arvo. Sijoittaa myös parhaan siirron emolautaan board.best_move
    """

    if depth == 0:
        return evaluate(board)
    score = -10**11
    gen = MoveGen()
    gen.generate(board)
    if len(gen.move_list) == 0:
        new_board = copy.deepcopy(board)
        new_board.make_null_move()
        return -alpha_beta(depth - 1, ply + 1, new_board, -beta, -alpha)
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
    """
    Aseman arviointi. Asema arvioidaan yksinkertaisella idealla jossa ns asemallisesta
    pelista vastaa ns. Piece Square Tables (https://www.chessprogramming.org/Piece-Square_Tables).

    Returns:
        Arvion aseman laadusta sille pelaajalle jonka siirtovuoro on. Esim jos musta on voittamaisillaan,
        ja on mustan vuoro, palauttaisi funktio todennakoisesti positiivisen luvun.
    """

    pst_score = 0
    for i in range(N_SQUARES):
        pst_score += board.get_piece_on_square(i) * (PST[i] + 50)
    return pst_score * board.get_active_player()
