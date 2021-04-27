import pygame, load, defs
class Solve():
        
    def tick(self, screen, s, events, loader):
        #kasitellaan tapahtuman moodi specifissa koodissa. Ikkuna sulkeminen kasiteltiin jo main.py tiedostossa
        for event in events:
            #Tarkistetaan painettiinko solve moodille specifeija nappeja
            if event.type == pygame.MOUSEBUTTONDOWN:
                pressed_button = defs.getButtonBelowCursor(defs.mode.SOLVE)
                if pressed_button == defs.button.RATKAISU:
                    s.findSolution()
                    s.ruudukko = [row[:] for row in s.ratkaisu]
                if pressed_button == defs.button.TALLENNA:
                    loader.add(s)
            #Kasitellaan hiiren painallus
            if event.type == pygame.MOUSEBUTTONDOWN:
                #hiiren kordinaatit
                kordinaatti = pygame.mouse.get_pos()
                #Tarkistetaan osuiko laudalle ja jos osui niin aktivoidaan ruutu
                if s.getPressedSquare(kordinaatti[0], kordinaatti[1]) != None:
                    s.activate(s.getPressedSquare(kordinaatti[0], kordinaatti[1]))
                else:
                    s.deactivate()

            if event.type == pygame.KEYDOWN and s.cursor_active:
                key = defs.getNumberKeyPressed(event.key)
                if s.checkLegalityNumberOnSquare(s.cursor_x, s.cursor_y, key, s.ruudukko):
                    s.insert(key)
                    if not s.findSolution:
                        s.forceInsert(0)

        #Piirretaan sudoku
        s.draw(screen)

        #piirretaan sudoku jatka myohemmin nappula
        defs.drawButton(screen, defs.NAPPULA_TALLENNA_X, defs.NAPPULA_TALLENNA_Y, defs.NAPPULA_TALLENNA_STR, defs.getButtonBelowCursor(defs.mode.SOLVE) == defs.button.TALLENNA)

        #piirretaan ratkaisu nappula
        defs.drawButton(screen, defs.NAPPULA_RATKAISU_X, defs.NAPPULA_RATKAISU_Y, defs.NAPPULA_RATKAISU_STR, defs.getButtonBelowCursor(defs.mode.SOLVE) == defs.button.RATKAISU)

    def switch(self, s):
        if s.findSolution():
            #asetetaan ruudun nimeksi "Sudoku Solver ja mode"
            pygame.display.set_caption('Sudoku Solver - ' + defs.NAPPULA_SOLVE_STR) 
            return True
        return False