import copy
import os
import entity.internal_board
from misc.defs import *


class Loader():

    """
    Luokan vastuulla on asemien tallennusta ja lataamista

    Attributes:
        self.states: lista tallenetuista asemista
        self.cursor: mita asemaa katsotaan
    """

    def __init__(self):
        """
        Lataa tallenustiedostosta aijemmin tallenetut asemat muistiin
        """

        self.states = []
        if os.path.isfile(SAVE_FILE):
            savefile = open(SAVE_FILE, "r")
            rivit = savefile.readlines()
            for rivi in rivit:
                board = entity.internal_board.Board()
                for i in range(N_SQUARES):
                    board.set_piece(i, int(rivi[i]) - 1)
                self.states.append(copy.deepcopy(board))
            savefile.close()
        if len(self.states) == 0:
            self.states.append(entity.internal_board.Board())
        self.cursor = len(self.states) - 1

    def add(self, board):
        """
        lisaa annetun aseman muistiin

        Args: 
            board: othello-lauta objekti
        """

        self.states.append(copy.deepcopy(board))

    def save(self):
        """
        Tallentaa listassa olevat asemat levylle.
        """

        savefile = open(SAVE_FILE, "w+")
        lines = []
        for board in self.states:
            state_info = ""
            for i in range(N_SQUARES):
                state_info += str(1 + board.get_piece_on_square(i))
            lines.append(state_info + "\n")

        savefile.writelines(lines)
        savefile.close()

    def dec_cursor(self):
        """
        Kasvattaa indexia jota vastaavaa olevaa asemaa tarkastelemme kayttoliittymassa
        """

        self.cursor -= 1
        self.cursor = max(self.cursor, 0)

    def inc_cursor(self):
        """
        Laskee indexia jota vastaavaa olevaa asemaa tarkastelemme kayttoliittymassa
        """

        self.cursor += 1
        if self.cursor > len(self.states) - 1:
            self.cursor = len(self.states) - 1
