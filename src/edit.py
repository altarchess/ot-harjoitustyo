import pygame, defs
class Edit():
        
    def tick(self, screen, s, events):
        #kasitellaan tapahtuman moodi specifissa koodissa. Ikkuna sulkeminen kasiteltiin jo main.py tiedostossa
        for event in events:
            #Tarkistetaan painettiinko editointi moodille specifeija nappeja
            if event.type == pygame.MOUSEBUTTONDOWN:
                pressed_button = defs.getButtonBelowCursor(defs.mode.EDIT)
                if pressed_button == defs.button.GENEROI:
                    s.generate()
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
                s.forceInsert(defs.getNumberKeyPressed(event.key))

        #Piirretaan sudoku
        s.draw(screen)

        #piirretaan generoi sudoku nappula
        defs.drawButton(screen, defs.NAPPULA_GENEROI_X, defs.NAPPULA_GENEROI_Y, defs.NAPPULA_GENEROI_STR, defs.getButtonBelowCursor(defs.mode.EDIT) == defs.button.GENEROI)

    def switch(self):
        #asetetaan ruudun nimeksi "Sudoku Solver ja mode"
        pygame.display.set_caption('Sudoku Solver - ' + defs.NAPPULA_EDITOR_STR) 
        return True

        