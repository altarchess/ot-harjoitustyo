import math
from misc.defs import *
import engine.move_gen

# Auttaja funktiot


def x_from_square(square):
    """
    Palauttaa x kordinaatin othello laudalla kun annetaan ruutu

    Args: 
        square: ruutu jonka x kordinaatti halutaan tietaa

    Returns: 
        x kordinaatti joka vastaa rutua othello laudalla
    """

    return square % COLUMNS


def y_from_square(square):
    """
    Palauttaa y kordinaatin othello laudalla kun annetaan ruutu

    Args: 
        square: ruutu jonka y kordinaatti halutaan tietaa

    Returns: 
        y kordinaatti joka vastaa rutua othello laudalla
    """

    return math.floor(square/COLUMNS)


def square_from_xy(square_x, square_y):
    """
    Palauttaa ruudun othello laudalla kun sille annetaan x ja y

    Args: 
        square_x: ruudun x komponentti
        square_y: ruudun y komponentti

    Returns: 
        Ruudun joka vastaa x ja y kordinaattia
    """
    return square_x + square_y * COLUMNS

# Laudan luokka


class Board:

    """
    Luokka joka kuvaa othello lautaa
    """

    def __init__(self):
        """
        Asetetaan lauta tyhjasta aloitusasemaan
        """

        self.__piece_list = [0] * N_SQUARES
        self.__piece_list[D4] = BLACK_PIECE
        self.__piece_list[E4] = WHITE_PIECE
        self.__piece_list[D5] = WHITE_PIECE
        self.__piece_list[E5] = BLACK_PIECE
        self.__active_player = WHITE_PIECE
        self.best_move = 0  # temp value set by alpha_beta

    def set_piece(self, square, piece):
        """
        Asettaa nappulan ruutuun

        Args:
            square: ruutu johon halutaan asettaa nappula
            piece: nappula joka siihen halutaan asettaa
        """

        self.__piece_list[square] = piece

    def get_piece_on_square(self, square):
        """
        Palauttaa nappulan joka on anetussa ruudussa

        Args:
            square: ruutu jonka nappula halutaan tietaa

        Returns:
            Nappulan joka on ruudussa
        """

        if square < 0 or square >= N_SQUARES:
            return 0
        return self.__piece_list[square]

    def get_piece_on_cord(self, x, y):
        """
        Palauttaa nappulan joka on anetussa x ja y kordinaatissa

        Args:
            x: ruudun x komponentti
            y: ruudun y komponentti

        Returns:
            Nappulan joka on ruudussa anettujen x ja y kordinaattien mukaan
        """

        if x >= COLUMNS or x < 0 or y >= ROWS or y < 0:
            return 0
        return self.__piece_list[y * ROWS + x]

    def get_active_player(self):
        """
        Palauttaa pelaajan jonka siirtovuoro on

        Returns:
            -1 tai 1 riippuen vuorosta
        """
        return self.__active_player

    def make_move(self, move: engine.move_gen.Move):
        """
        tekee siirron laudalla

        Args:
            move: Move objekti, jossa maarritelty siirto tehdaan
        """

        for i in range(move.steps):
            self.__piece_list[move.start + i * move.direction] = move.color
        self.__active_player = 0 - move.color

    def make_null_move(self):
        """
        Vaihtaa siirtovuoroa
        """

        self.__active_player = 0 - self.__active_player

    def is_win(self):
        """
        Tarkistaa onko asema valkoisen voitto, tasan vai mustan voitto

        Returns:
            2 jos valkoisen voitto, 1 jos mustan, ja 0 jos tasan
        """

        gen = engine.move_gen.MoveGen()
        gen.generate(self)
        if len(gen.move_list) == 0:
            self.__active_player = 0 - self.__active_player
            gen = engine.move_gen.MoveGen()
            gen.generate(self)
            if len(gen.move_list) == 0:
                score = 0
                for i in range(N_SQUARES):
                    score += self.get_piece_on_square(i)
                return 2 + max(-1, min(1, score))
            return ONGOING
        return ONGOING
