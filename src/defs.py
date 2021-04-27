import pygame
from enum import Enum

pygame.init()

#Tiedosto jonne jatka myohemmin sudokut tallennetaan
SAVE_FILE   = "saved.sudoku"

#fontit
SUDOKU_FONT = pygame.font.SysFont(None, 62)
BUTTON_FONT = pygame.font.SysFont(None, 25)

#varit
VALKOINEN       = (255, 255, 255)
MUSTA           = (0, 0, 0)
HARMAA          = (100, 100, 100)
VAALEAN_HARMAA  = (150, 150, 150)
PUNAINEN        = (255, 0, 0)

#ruudukon kordinaatteja
X_ALKU              = 25
Y_ALKU              = 125
RUUTU_KOKO          = 50
RUUTU_MAARA         = 81
RUUTUJA_SIVUTTAIN   = 9

#Sudokun tulostettavia
SUDOKU_SOULTION_Y   = 10
SUDOKU_TYHJAT_Y     = 40
SUDOKU_MAHDOLLINEN  = "Ratkaistavissa: "
SUDOKULLA_RATK      = "Kyllä"
SUDOKULLA_EI_RATK   = "Ei"
SUDOKULLA_TYHJIA    = "Täytettäviä ruutuja: "

#tyhja ruudukko kokoa 9x9
TYHJA_RUUDUKKO = [[0] * RUUTU_KOKO for i in range(RUUTU_KOKO)]

#enumeraatio modeille kuten https://github.com/altarchess/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md#k%C3%A4ytt%C3%B6liittym%C3%A4luonnos
class mode(Enum):
    EDIT    = 1
    SOLVE   = 2
    LOAD    = 3

#enumeraatio nappuloille
class button(Enum):
    NO_BUTTON   = 0
    EDIT        = 1
    SOLVE       = 2
    LOAD        = 3
    GENEROI     = 4
    TALLENNA    = 5
    RATKAISU    = 6
    SEURAAVA    = 7
    EDELLINEN   = 8
    TAMA        = 9

#Mode nappulat
NAPPULA_EDITOR_X    = 350
NAPPULA_EDITOR_Y    = 10
NAPPULA_SOLVE_X     = 350
NAPPULA_SOLVE_Y     = 40
NAPPULA_LOAD_X      = 350
NAPPULA_LOAD_Y      = 70
NAPPULA_EDITOR_STR  = "Editoi"
NAPPULA_SOLVE_STR   = "Ratkaise"
NAPPULA_LOAD_STR    = "Lataa"

#Muita nappuloita
NAPPULA_GENEROI_STR         = "Generoi Sudoku"
NAPPULA_GENEROI_X           = X_ALKU
NAPPULA_GENEROI_Y           = 70
NAPPULA_TALLENNA_STR        = "Jatka myöhemmin"
NAPPULA_TALLENNA_X          = X_ALKU
NAPPULA_TALLENNA_Y          = 70
NAPPULA_RATKAISU_STR        = "Ratkaisu"
NAPPULA_RATKAISU_X          = X_ALKU + 170
NAPPULA_RATKAISU_Y          = 70
NAPPULA_SEURAAVA_STR        = "Seuraava"
NAPPULA_SEURAAVA_X          = X_ALKU
NAPPULA_SEURAAVA_Y          = 70
NAPPULA_EDELLINEN_STR       = "Edellinen"
NAPPULA_EDELLINEN_X         = X_ALKU + 90
NAPPULA_EDELLINEN_Y         = 70
NAPPULA_RATKAISE_TAMA_STR   = "Ratkaise tämä"
NAPPULA_RATKAISE_TAMA_X     = NAPPULA_EDELLINEN_X + 90
NAPPULA_RATKAISE_TAMA_Y     = 70
#Helpereita

#Selvittaa mita numeronappia on painettu. Palauttaa 0 jos ei mitaan
def getNumberKeyPressed(key):
    if key == pygame.K_1:
        return 1
    if key == pygame.K_2:
        return 2
    if key == pygame.K_3:
        return 3
    if key == pygame.K_4:
        return 4
    if key == pygame.K_5:
        return 5
    if key == pygame.K_6:
        return 6
    if key == pygame.K_7:
        return 7
    if key == pygame.K_8:
        return 8
    if key == pygame.K_9:
        return 9
    return 0

#Piirra nappula tekstilla
def drawButton(screen, x, y, teksti, active):
    #muutetaan napin varia jos cursori on napin paalla
    color = VAALEAN_HARMAA
    if active:
        color = PUNAINEN
    #luodaan teksti
    text = BUTTON_FONT.render(teksti, True, MUSTA) 

    #piiretaan laatikko
    width  = text.get_width()
    height = text.get_height()
    pygame.draw.rect(screen, color, (x, y, width+10, height + 10))

    #piirretaan teksti
    screen.blit(text,(x+5, y+5))  

    return width + 10 #text + empty space

#tarkistaa onko cursori laatikon paalla
def cursorOnBox(x, y, width, height):
    #hiiren kordinaatit
    kordinaatti = pygame.mouse.get_pos()
    #tarkistetaan onko laatikon sisalla
    if kordinaatti[0] > x and kordinaatti[0] < x + width and kordinaatti[1] > y and kordinaatti[1] < y + height:
        return True
    return False

#tarkistaa onko cursori tekstilaatikon paalla
def cursorOnTextBox(x, y, teksti, font):
    #luodaan teksti
    text = font.render(teksti, True, MUSTA) 

    #tarkistetaan leveys ja korkeus
    width  = text.get_width()
    height = text.get_height()

    return cursorOnBox(x, y, width + 10, height + 10)

#tarkistaa onko hiiri napilla
def getButtonBelowCursor(m):
    if cursorOnTextBox(NAPPULA_EDITOR_X, NAPPULA_EDITOR_Y, NAPPULA_EDITOR_STR, BUTTON_FONT):
        return button.EDIT
    if cursorOnTextBox(NAPPULA_SOLVE_X, NAPPULA_SOLVE_Y, NAPPULA_SOLVE_STR, BUTTON_FONT):
        return button.SOLVE
    if cursorOnTextBox(NAPPULA_LOAD_X, NAPPULA_LOAD_Y, NAPPULA_LOAD_STR, BUTTON_FONT):
        return button.LOAD
    if m == mode.EDIT and cursorOnTextBox(NAPPULA_GENEROI_X, NAPPULA_GENEROI_Y, NAPPULA_GENEROI_STR, BUTTON_FONT):
        return button.GENEROI
    if m == mode.SOLVE and cursorOnTextBox(NAPPULA_TALLENNA_X, NAPPULA_TALLENNA_Y, NAPPULA_TALLENNA_STR, BUTTON_FONT):
        return button.TALLENNA
    if m == mode.SOLVE and cursorOnTextBox(NAPPULA_RATKAISU_X, NAPPULA_RATKAISU_Y, NAPPULA_RATKAISU_STR, BUTTON_FONT):
        return button.RATKAISU
    if m == mode.LOAD and cursorOnTextBox(NAPPULA_SEURAAVA_X, NAPPULA_SEURAAVA_Y, NAPPULA_SEURAAVA_STR, BUTTON_FONT):
        return button.SEURAAVA
    if m == mode.LOAD and cursorOnTextBox(NAPPULA_EDELLINEN_X, NAPPULA_EDELLINEN_Y, NAPPULA_EDELLINEN_STR, BUTTON_FONT):
        return button.EDELLINEN
    if m == mode.LOAD and cursorOnTextBox(NAPPULA_RATKAISE_TAMA_X, NAPPULA_RATKAISE_TAMA_Y, NAPPULA_RATKAISE_TAMA_STR, BUTTON_FONT):
        return button.TAMA
    return button.NO_BUTTON
