import unittest
import random
from misc.defs import BLACK_PIECE, ONGOING, WHITE_WIN, BLACK_WIN, N_SQUARES
from entity.internal_board import Board, x_from_square, y_from_square
from entity.internal_board import square_from_xy
from engine.move_gen import Move

class TestBoard(unittest.TestCase):

    """
    Testaa othello laudasta vastaavaa luokkaa. Huom. Vain logiikka, 
    ei grafiikkaa. Testaa myos muita tiedostossa olevia lautaan
    liittyvia funktioita.
    """

    def setUp(self):

        """
        Luodaan monessa testissa kaytettava lauta
        """

        self.board = Board()

    def test_x_from_square(self):

        """
        Tarkistaa vaakasuoran kordinaatin laskennan korrektiutta
        kahden esimerkin avulla. (Kordinaattit ja ruudut othello
        laudalla)
        """

        self.assertEqual(x_from_square(12), 4)
        self.assertEqual(x_from_square(25), 1)

    def test_y_from_square(self):

        """
        Tarkistaa pystysuoran kordinaatin laskennan korrektiutta
        kahden esimerkin avulla. (Kordinaattit ja ruudut othello
        laudalla)
        """

        self.assertEqual(y_from_square(12), 1)
        self.assertEqual(y_from_square(25), 3)

    def test_square_from_xy(self):

        
        """
        Tarkistaa vaaka- ja pysty-suoran kordinaattien muuntamista
        ruuduksi othello laudalla.
        """

        self.assertEqual(square_from_xy(4, 1), 12)
        self.assertEqual(square_from_xy(1, 3), 25)

    def test_set_piece(self):
        
        """
        Tarkistaa satunnaisilla arvoilla, toimiiko othello nappulan asetus oikein
        ristikkoon.
        """

        for i in range(N_SQUARES):
            random_piece = random.randint(-1, 1)
            self.board.set_piece(i, random_piece)
            self.assertEqual(random_piece, self.board.get_piece_on_square(i))


    def test_get_piece_on_cord(self):

        """
        Tarkistaa satunnaislukuja kayttaen, toimiiko nappulan ruutua kohti
        palauttava funktio oikein. Oletuksena on etta muut funktiot toimivat oikein,
        silla testaus tapahtuu ristiin
        """

        self.assertEqual(0, self.board.get_piece_on_cord(-1, -1))
        for i in range(N_SQUARES):
            random_piece = random.randint(-1, 1)
            self.board.set_piece(i, random_piece)
            self.assertEqual(random_piece, self.board.get_piece_on_cord(x_from_square(i), y_from_square(i)))

    def test_make_move(self):

        """
        Testaa kahden eri siirron jalkeen taytettyja ruutuja ja siten siirron teon toimivuutta.
        """

        self.board.make_move(Move(0, 2, 1, 1))
        self.assertEqual(1, self.board.get_piece_on_square(1))
        self.assertEqual(0, self.board.get_piece_on_square(3))
        self.board.make_move(Move(0, 5, 1, 1))
        self.assertEqual(1, self.board.get_piece_on_square(3))

    def test_is_win(self):

        """
        Testaa funktiota joka ilmoittaa onko asema voittava, tayttamalla ruudukko tayteen tiettya varia.
        Tai myoskin jattamalla viela tyhjia ruutuja niin etta sen tulisi ilmoittaa etta peli on viela 
        kaynissa
        """

        self.assertEqual(ONGOING, self.board.is_win())
        for i in range(N_SQUARES):
            self.board.set_piece(i, 1)
        self.assertEqual(WHITE_WIN, self.board.is_win())
        for i in range(N_SQUARES):
            self.board.set_piece(i, -1)
        self.assertEqual(BLACK_WIN, self.board.is_win())

    def test_make_null_move(self):

        """"
        Testaa tyhjan siirron pelaamista varten tehtya funktiota. Tyhja siirto muuttaa vain
        siirtovuoroa
        """

        self.board.make_null_move()
        self.assertEqual(self.board.get_active_player(), BLACK_PIECE)
