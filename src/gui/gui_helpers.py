import pygame
from misc.defs import GRAY, RED, BLACK, BUTTON_FONT

# Piirra nappula tekstilla


def draw_button(screen, x_cord, y_cord, text, active):
    # muutetaan napin varia jos cursori on napin paalla
    color = GRAY
    if active:
        color = RED
    # luodaan teksti
    text = BUTTON_FONT.render(text, True, BLACK)

    # piiretaan laatikko
    width = text.get_width()
    height = text.get_height()
    pygame.draw.rect(screen, color, (x_cord, y_cord, width + 10, height + 10))

    # piirretaan teksti
    screen.blit(text, (x_cord + 5, y_cord + 5))

    return width + 10  # text + empty space

# tarkistaa onko cursori laatikon paalla


def cursor_on_box(x_cord, y_cord, width, height):
    # hiiren kordinaatit
    cord = pygame.mouse.get_pos()
    # tarkistetaan onko laatikon sisalla
    if cord[0] > x_cord and cord[0] < x_cord + width and cord[1] > y_cord and cord[1] < y_cord + height:
        return True
    return False

# tarkistaa onko cursori tekstilaatikon paalla


def cursor_on_text_box(x_cord, y_cord, text, font):
    # luodaan teksti
    text = font.render(text, True, BLACK)

    # tarkistetaan leveys ja korkeus
    width = text.get_width()
    height = text.get_height()

    return cursor_on_box(x_cord, y_cord, width + 10, height + 10)
