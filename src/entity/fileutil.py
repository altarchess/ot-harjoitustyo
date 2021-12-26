import copy
import os
import entity.internalboard
from defs import *


class Loader():
    def __init__(self):
        self.states = []
        if os.path.isfile(SAVE_FILE):
            savefile = open(SAVE_FILE, "r")
            rivit = savefile.readlines()
            for rivi in rivit:
                board = entity.internalboard.Board()
                for i in range(N_SQUARES):
                    board.set_piece(i, int(rivi[i]) - 1)
                self.states.append(copy.deepcopy(board))
            savefile.close()
        if len(self.states) == 0:
            self.states.append(entity.internalboard.Board())
        self.cursor = len(self.states) - 1

    def add(self, board):
        self.states.append(copy.deepcopy(board))

    def save(self):
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
        self.cursor -= 1
        self.cursor = max(self.cursor, 0)

    def inc_cursor(self):
        self.cursor += 1
        if self.cursor > len(self.states) - 1:
            self.cursor = len(self.states) - 1