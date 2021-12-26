import gui.guihelpers as guihelpers
from defs import *
def render(screen):
    guihelpers.draw_button(screen, PREVIOUS_X, PREVIOUS_Y, PREVIOUS_T, guihelpers.cursor_on_text_box(
        PREVIOUS_X, PREVIOUS_Y, PREVIOUS_T, BUTTON_FONT))
    guihelpers.draw_button(screen, NEXT_X, NEXT_Y, NEXT_T, guihelpers.cursor_on_text_box(
        NEXT_X, NEXT_Y, NEXT_T, BUTTON_FONT))
    guihelpers.draw_button(screen, LOAD_X, LOAD_Y, LOAD_T, guihelpers.cursor_on_text_box(
        LOAD_X, LOAD_Y, LOAD_T, BUTTON_FONT))