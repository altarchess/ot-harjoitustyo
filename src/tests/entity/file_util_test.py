import unittest
import copy
from entity.file_util import Loader
from entity.internal_board import Board
from misc.defs import N_SQUARES

class TestLoader(unittest.TestCase):

    """
    Testaa aseman tallenuksesta ja lataamisesta vastaavaa luokkaa
    """


    def setUp(self):

        """
        Kaikkissa testeissa kaytettava tallennus- ja lataus-luokka
        """
        self.loader = Loader()

    def test_dec_cursor(self):

        """
        Tallenettujen aseman listassa olevan cursorin pienennys funktion testaus. 
        Tarkistetaan kaikki mahdolliset pienennykset.
        """

        for i in range (len(self.loader.states)):
            self.loader.dec_cursor()
            self.assertEqual(self.loader.cursor, max(0, len(self.loader.states) - i - 2))

    def test_inc_cursor(self):
        
        """
        Tallenettujen aseman listassa olevan cursorin kasvatus funktion testaus. 
        Tarkistetaan kaikki mahdolliset kasvatukset.
        """

        for i in range (len(self.loader.states)):
            self.loader.dec_cursor()
        for i in range (len(self.loader.states) + 1):
            self.loader.inc_cursor()
            self.assertEqual(self.loader.cursor, min(len(self.loader.states) - 1 , i + 1))

    def test_add(self):
        
        """
        Testaa etta aseman lisays luokkaan toimii oikein. Tarkistaa etta kaikki ruudut tasmaavat.
        """

        board = Board()
        self.loader.add(board)
        for i in range(N_SQUARES):
            self.assertEqual(board.get_piece_on_square(i), self.loader.states[len(self.loader.states) - 1].get_piece_on_square(i))
