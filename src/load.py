import pygame, sudoku, defs, copy, os
class Loader():
    def __init__(self):
        self.sudokut= []
        self.cursor = 0
        if os.path.isfile(defs.SAVE_FILE):
            savefile    = open(defs.SAVE_FILE, "r")
            rivit       = savefile.readlines()
            for rivi in rivit:
                s = sudoku.Sudoku(0,0)
                for i in range(defs.RUUTU_MAARA):
                    s.cursor_x = int(i / 9)
                    s.cursor_y = int(i % 9)
                    s.cursor_active = True
                    s.forceInsert(int(rivi[i]))
                self.sudokut.append(copy.deepcopy(s))
            savefile.close()
        if len(self.sudokut) == 0:
            self.sudokut.append(copy.deepcopy(sudoku.Sudoku(0,0)))

    def tick(self, screen, events):
        #kasitellaan tapahtuman moodi specifissa koodissa. Ikkuna sulkeminen kasiteltiin jo main.py tiedostossa
        for event in events:
            #Tarkistetaan painettiinko load moodille specifeija nappeja
            if event.type == pygame.MOUSEBUTTONDOWN:
                pressed_button = defs.getButtonBelowCursor(defs.mode.LOAD)
                if pressed_button == defs.button.EDELLINEN:
                    self.kasvataCursoria()
                if pressed_button == defs.button.SEURAAVA:
                    self.laskeCursoria()

        self.sudokut[self.cursor].draw(screen)

        #piirretaan seuraava nappula
        defs.drawButton(screen, defs.NAPPULA_SEURAAVA_X, defs.NAPPULA_SEURAAVA_Y, defs.NAPPULA_SEURAAVA_STR, defs.getButtonBelowCursor(defs.mode.LOAD) == defs.button.SEURAAVA)

        #piirretaan edellinen nappula
        defs.drawButton(screen, defs.NAPPULA_EDELLINEN_X, defs.NAPPULA_EDELLINEN_Y, defs.NAPPULA_EDELLINEN_STR, defs.getButtonBelowCursor(defs.mode.LOAD) == defs.button.EDELLINEN)

        #piirretaan ratkaise tama nappula
        defs.drawButton(screen, defs.NAPPULA_RATKAISE_TAMA_X, defs.NAPPULA_RATKAISE_TAMA_Y, defs.NAPPULA_RATKAISE_TAMA_STR, defs.getButtonBelowCursor(defs.mode.LOAD) == defs.button.TAMA)

    def switch(self, s):
        pygame.display.set_caption('Sudoku Solver - ' + defs.NAPPULA_LOAD_STR) 
        self.cursor = len(self.sudokut) - 1
        return True

    def add(self, sudoku):
        self.sudokut.append(copy.deepcopy(sudoku))
            
    def save(self):
        savefile    = open(defs.SAVE_FILE, "w+")
        lines = []
        for s in self.sudokut:
            sudoku_info = ""
            for x in range (9):
                for y in range(9):
                    sudoku_info += str(s.ruudukko[x][y])
            lines.append(sudoku_info + "\n")
        
        savefile.writelines(lines)
        savefile.close()

    def laskeCursoria(self):
        self.cursor -= 1
        if self.cursor < 0:
            self.cursor = 0

    def kasvataCursoria(self):
        self.cursor += 1
        if self.cursor > len(self.sudokut) - 1:
            self.cursor = len(self.sudokut) - 1
        
        
