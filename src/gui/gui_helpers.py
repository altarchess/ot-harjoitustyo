import pygame
from misc.defs import GRAY, RED, BLACK, BUTTON_FONT


def draw_button(screen, x_cord, y_cord, text, active):
    """
    Piirtaa textilaatikon, eli nappulan

    Args:
        x_cord: textiboxin x alkukordinaatti
        y_cord: textiboxin y alkukordinaatti
        text: texti joka ruutuun piirretaan
        active: onko ruutu aktiivinen, jos on piirretaan punaisella!

    Returns:
        Laatikon leveys pixeleina
    """

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


def cursor_on_box(x_cord, y_cord, width, height):
    """
    Tarkistaa onko cursori laatikon paalla

    Args:
        x_cord: laatikon x alkukordinaatti
        y_cord: laatikon y alkukordinaatti
        width: laatikon leveys
        height: laatikon korkeus

    Returns:
        Tosi jos on laatikon paalla, Epatosi jos ei ole
    """

    # hiiren kordinaatit
    cord = pygame.mouse.get_pos()
    # tarkistetaan onko laatikon sisalla
    if cord[0] > x_cord and cord[0] < x_cord + width and cord[1] > y_cord and cord[1] < y_cord + height:
        return True
    return False


def cursor_on_text_box(x_cord, y_cord, text, font):
    """
    Tarkistaa onko cursori laatikon paalla

    Args:
        x_cord: laatikon x alkukordinaatti
        y_cord: laatikon y alkukordinaatti
        text: laatikon texti
        font: textin fontti

    Returns:
        Tosi jos on laatikon paalla, Epatosi jos ei ole
    """

    # luodaan teksti
    text = font.render(text, True, BLACK)

    # tarkistetaan leveys ja korkeus
    width = text.get_width()
    height = text.get_height()

    return cursor_on_box(x_cord, y_cord, width + 10, height + 10)
