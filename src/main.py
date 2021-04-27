import pygame, sudoku, edit, solve, load, defs, copy

#enumeraatio modeille kuten https://github.com/altarchess/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md#k%C3%A4ytt%C3%B6liittym%C3%A4luonnos
ohjelman_mode = defs.mode.EDIT

#luodaan ruutu
screen = pygame.display.set_mode((500, 600)) 
#asetetaan ruudun nimeksi "Sudoku Solver ja mode"
pygame.display.set_caption('Sudoku Solver - ' + defs.NAPPULA_EDITOR_STR) 

#Luodaan sudoku objekti jota kaytetaan ympari ohjelmaa
s = sudoku.Sudoku(0,0)

#Luodan mode luokat
edit_mode = edit.Edit()
solve_mode = solve.Solve()
load_mode = load.Loader()

#ns. Pelilooppi.
running = True
while running: 
    #Tarkistetaan vain yrittaako kayttaja sulkea ohjelman. Events lista kasitellaan uudestaan moodi specifissa koodissa
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            load_mode.save()
            running = False
        #Tarkistetaan painettiinko kaikille modeille yhteisia nappeja
        if event.type == pygame.MOUSEBUTTONDOWN:
            pressed_button = defs.getButtonBelowCursor(ohjelman_mode)
            if pressed_button == defs.button.EDIT:
                #tarkistetaan voiko modeen vaihtaa
                if edit_mode.switch():
                    ohjelman_mode = defs.mode.EDIT
            if pressed_button == defs.button.SOLVE:
                #tarkistetaan voiko modeen vaihtaa
                if solve_mode.switch(s):
                    ohjelman_mode = defs.mode.SOLVE
            if pressed_button == defs.button.LOAD:
                #tarkistetaan voiko modeen vaihtaa
                if load_mode.switch(s):
                    ohjelman_mode = defs.mode.LOAD
            if pressed_button == defs.button.TAMA:
                s = copy.deepcopy(load_mode.sudokut[load_mode.cursor])
                ohjelman_mode = defs.mode.SOLVE
                continue
    
    #Asetetaan se taustavariksi
    screen.fill(defs.VALKOINEN)

    #piirretaan mode nappulat
    defs.drawButton(screen, defs.NAPPULA_EDITOR_X, defs.NAPPULA_EDITOR_Y, defs.NAPPULA_EDITOR_STR, defs.getButtonBelowCursor(ohjelman_mode) == defs.button.EDIT)
    defs.drawButton(screen, defs.NAPPULA_SOLVE_X, defs.NAPPULA_SOLVE_Y, defs.NAPPULA_SOLVE_STR, defs.getButtonBelowCursor(ohjelman_mode) == defs.button.SOLVE)
    defs.drawButton(screen, defs.NAPPULA_LOAD_X, defs.NAPPULA_LOAD_Y, defs.NAPPULA_LOAD_STR, defs.getButtonBelowCursor(ohjelman_mode) == defs.button.LOAD)

    #Jasennelty eri modejen koodi eri tiedostoihin selkeyden vuoksi.
    if ohjelman_mode == defs.mode.EDIT:
        edit_mode.tick(screen, s, events)

    if ohjelman_mode == defs.mode.SOLVE:
        solve_mode.tick(screen, s, events, load_mode)

    if ohjelman_mode == defs.mode.LOAD:
        load_mode.tick(screen, events)

    #piirra!
    pygame.display.flip() 

pygame.quit() 