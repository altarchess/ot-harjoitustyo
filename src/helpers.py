import pygame
from defs import *

#Piirra nappula tekstilla
def drawButton(screen, x, y, text, active):
    #muutetaan napin varia jos cursori on napin paalla
    color = GRAY
    if active:
        color = RED
    #luodaan teksti
    text = BUTTON_FONT.render(text, True, BLACK) 

    #piiretaan laatikko
    width  = text.get_width()
    height = text.get_height()
    pygame.draw.rect(screen, color, (x, y, width + 10, height + 10))

    #piirretaan teksti
    screen.blit(text,(x + 5, y + 5))  

    return width + 10 #text + empty space

#tarkistaa onko cursori laatikon paalla
def cursorOnBox(x, y, width, height):
    #hiiren kordinaatit
    cord = pygame.mouse.get_pos()
    #tarkistetaan onko laatikon sisalla
    if cord[0] > x and cord[0] < x + width and cord[1] > y and cord[1] < y + height:
        return True
    return False

#tarkistaa onko cursori tekstilaatikon paalla
def cursorOnTextBox(x, y, text, font):
    #luodaan teksti
    text = font.render(text, True, BLACK) 

    #tarkistetaan leveys ja korkeus
    width  = text.get_width()
    height = text.get_height()

    return cursorOnBox(x, y, width + 10, height + 10)