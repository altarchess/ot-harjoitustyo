import pygame, othello, copy, os, helpers
from defs import *
class Loader():
    def __init__(self):
        self.states = []
        if os.path.isfile(SAVE_FILE):
            savefile    = open(SAVE_FILE, "r")
            rivit       = savefile.readlines()
            for rivi in rivit:
                board = othello.Board()
                for i in range(N_SQUARES):
                    board.setPiece(i, int(rivi[i]) - 1)
                self.states.append(copy.deepcopy(board))
            savefile.close()
        if len(self.states) == 0:
            self.states.append(othello.Board())
        self.cursor = len(self.states) - 1

    def tick(self, screen, events):
        self.states[self.cursor].render(screen)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if helpers.cursorOnTextBox(PREVIOUS_X, PREVIOUS_Y, PREVIOUS_T, BUTTON_FONT):
                    self.incCursor()
                
                if helpers.cursorOnTextBox(NEXT_X, NEXT_Y, NEXT_T, BUTTON_FONT):
                    self.decCursor()

        helpers.drawButton(screen, PREVIOUS_X, PREVIOUS_Y, PREVIOUS_T, helpers.cursorOnTextBox(PREVIOUS_X, PREVIOUS_Y, PREVIOUS_T, BUTTON_FONT))
        helpers.drawButton(screen, NEXT_X, NEXT_Y, NEXT_T, helpers.cursorOnTextBox(NEXT_X, NEXT_Y, NEXT_T, BUTTON_FONT))
        helpers.drawButton(screen, LOAD_X, LOAD_Y, LOAD_T, helpers.cursorOnTextBox(LOAD_X, LOAD_Y, LOAD_T, BUTTON_FONT))

    def add(self, board):
        self.states.append(copy.deepcopy(board))
            
    def save(self):
        savefile    = open(SAVE_FILE, "w+")
        lines = []
        for board in self.states:
            state_info = ""
            for i in range(N_SQUARES):
                state_info += str(1 + board.getPieceOnSquare(i))
            lines.append(state_info + "\n")
        
        savefile.writelines(lines)
        savefile.close()

    def decCursor(self):
        self.cursor -= 1
        if self.cursor < 0:
            self.cursor = 0

    def incCursor(self):
        self.cursor += 1
        if self.cursor > len(self.states) - 1:
            self.cursor = len(self.states) - 1