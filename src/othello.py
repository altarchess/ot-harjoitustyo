import math
import copy
import pygame
from defs import *
import helpers

# Auttaja funktiot


def x_from_square(square):
    return square % COLUMNS


def y_from_square(square):
    return math.floor(square/COLUMNS)


def square_from_xy(square_x, square_y):
    return square_x + square_y * COLUMNS


class MoveGen:
    def __init__(self):
        self.move_list = []

    def slider(self, board, square: int, direction):
        square_x = x_from_square(square)
        square_y = y_from_square(square)
        xmod = 0
        ymod = 0

        if direction in (NW, N, NE):
            ymod += 1
        if direction in (SW, S, SE):
            ymod -= 1
        if direction in (NE, E, SE):
            xmod += 1
        if direction in (NW, W, SW):
            xmod -= 1

        steps = 0
        while True:
            steps += 1
            square_x += xmod
            square_y += ymod
            piece = board.get_piece_on_cord(square_x, square_y)
            if piece == EMPTY_PIECE:
                return Move(-1, 0, 0, EMPTY_PIECE)
            if piece == board.get_active_player():
                if steps > 1:
                    return Move(square, steps, xmod + ymod * COLUMNS, board.get_active_player())
                return Move(-1, 0, 0, EMPTY_PIECE)

    def generate(self, board):
        for i in range(N_SQUARES):
            if (board.get_piece_on_square(i) == EMPTY_PIECE):
                # Jos ruutu on tyhja, tarkista onko siirto ruutuun mahdollinen tarkistamalla eri suunnassa olevat nappulat.
                for dir in range(DIRECTIONS):
                    m = self.slider(board, i, dir)
                    if m.steps > 0:
                        self.move_list.append(m)

# Siirto luokka


class Move:
    def __init__(self, start, steps, direction, color):
        self.start = start
        self.steps = steps
        self.direction = direction
        self.color = color


def evaluate(board):
    pst_score = 0
    for i in range(N_SQUARES):
        pst_score += board.get_piece_on_square(i) * (PST[i] + 50)
    return pst_score * board.get_active_player()


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

# Laudan luokka


class Board:

    def __init__(self):
        self.__piece_list = [0] * N_SQUARES
        self.__piece_list[D4] = BLACK_PIECE
        self.__piece_list[E4] = WHITE_PIECE
        self.__piece_list[D5] = WHITE_PIECE
        self.__piece_list[E5] = BLACK_PIECE
        self.__active_player = WHITE_PIECE
        self.best_move = 0  # temp value set by alpha_beta

    def set_piece(self, square, piece):
        self.__piece_list[square] = piece

    def get_piece_on_square(self, square):
        if square < 0 or square >= N_SQUARES:
            return 0
        return self.__piece_list[square]

    def get_piece_on_cord(self, x, y):
        if x >= COLUMNS or x < 0 or y >= ROWS or y < 0:
            return 0
        return self.__piece_list[y * ROWS + x]

    def get_active_player(self):
        return self.__active_player

    def make_move(self, move: Move):
        # We asume that the move is legal
        for i in range(move.steps):
            self.__piece_list[move.start + i * move.direction] = move.color
        self.__active_player = 0 - move.color

    def is_win(self):
        gen = MoveGen()
        gen.generate(self)
        if len(gen.move_list) == 0:
            self.__active_player = 0 - self.__active_player
            gen = MoveGen()
            gen.generate(self)
            if len(gen.move_list) == 0:
                score = 0
                for i in range(N_SQUARES):
                    score += self.get_piece_on_square(i)
                return 2 + max(-1, min(1, score))
            return ONGOING
        return ONGOING

    def render(self, screen):
        # piirra tausta
        pygame.draw.rect(screen, GREEN, (X_OFFSET, Y_OFFSET,
                         CELL_SIZE * COLUMNS, CELL_SIZE * ROWS))

        # Piirra ruudukko
        for i in range(COLUMNS + 1):
            pygame.draw.line(screen, DARK_GREEN, (X_OFFSET,  Y_OFFSET + CELL_SIZE * i),
                             (X_OFFSET + CELL_SIZE * COLUMNS,  Y_OFFSET + CELL_SIZE * i), 5)
            pygame.draw.line(screen, DARK_GREEN, (X_OFFSET + CELL_SIZE * i, Y_OFFSET),
                             (X_OFFSET + CELL_SIZE * i, Y_OFFSET + CELL_SIZE * ROWS), 5)

        # Piirra siirtovuoronappula
        if self.__active_player == WHITE_PIECE:
            pygame.draw.circle(
                screen, WHITE, (X_OFFSET + CELL_SIZE * COLUMNS, Y_OFFSET + CELL_SIZE * ROWS), 4)
        else:
            pygame.draw.circle(
                screen, BLACK, (X_OFFSET + CELL_SIZE * COLUMNS, Y_OFFSET + CELL_SIZE * ROWS), 4)

        for x in range(COLUMNS):
            for y in range(ROWS):
                if self.__piece_list[y * COLUMNS + x] == 0:
                    pass
                elif self.__piece_list[y * COLUMNS + x] == WHITE_PIECE:
                    pygame.draw.circle(screen, WHITE, (X_OFFSET + x * CELL_SIZE + CELL_SIZE /
                                       2, Y_OFFSET + y * CELL_SIZE + CELL_SIZE / 2), PIECE_SIZE)
                elif self.__piece_list[y * COLUMNS + x] == BLACK_PIECE:
                    pygame.draw.circle(screen, BLACK, (X_OFFSET + x * CELL_SIZE + CELL_SIZE /
                                       2, Y_OFFSET + y * CELL_SIZE + CELL_SIZE / 2), PIECE_SIZE)

        win_state = self.is_win()
        helpers.draw_button(screen, WIN_X, WIN_Y, WINSTATES[win_state], helpers.cursor_on_text_box(
            WIN_X, WIN_Y, WINSTATES[win_state], BUTTON_FONT))

    def tick(self, screen, events, loader):
        self.render(screen)

        helpers.draw_button(screen, ENGINE_MOVE_X, ENGINE_MOVE_Y, ENGINE_MOVE_T, helpers.cursor_on_text_box(
            ENGINE_MOVE_X, ENGINE_MOVE_Y, ENGINE_MOVE_T, BUTTON_FONT))
        helpers.draw_button(screen, SAVE_X, SAVE_Y, SAVE_T, helpers.cursor_on_text_box(
            SAVE_X, SAVE_Y, SAVE_T, BUTTON_FONT))
        helpers.draw_button(screen, NEW_X, NEW_Y, NEW_T, helpers.cursor_on_text_box(
            NEW_X, NEW_Y, NEW_T, BUTTON_FONT))
        helpers.draw_button(screen, LOAD_X, LOAD_Y, LOAD_T, helpers.cursor_on_text_box(
            LOAD_X, LOAD_Y, LOAD_T, BUTTON_FONT))

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                cord = pygame.mouse.get_pos()
                x = cord[0]
                y = cord[1]
                lauta_x = math.floor((x-X_OFFSET)/CELL_SIZE)
                lauta_y = math.floor((y-Y_OFFSET)/CELL_SIZE)
                if not (lauta_x >= COLUMNS or lauta_x < 0 or lauta_y >= ROWS or lauta_y < 0):
                    gen = MoveGen()
                    gen.generate(self)
                    for move in gen.move_list:
                        if move.start == square_from_xy(lauta_x, lauta_y):
                            self.make_move(move)
                if helpers.cursor_on_text_box(ENGINE_MOVE_X, ENGINE_MOVE_Y, ENGINE_MOVE_T, BUTTON_FONT):
                    alpha_beta(5, 0, self, -10**20, 10**20)
                    if self.best_move != -1:
                        self.make_move(self.best_move)

                if helpers.cursor_on_text_box(NEW_X, NEW_Y, NEW_T, BUTTON_FONT):
                    self.__init__()

                if helpers.cursor_on_text_box(SAVE_X, SAVE_Y, SAVE_T, BUTTON_FONT):
                    loader.add(self)
