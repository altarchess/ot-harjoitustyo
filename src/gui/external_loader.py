from gui import gui_helpers
from misc.defs import *
def render(screen):
    gui_helpers.draw_button(screen, PREVIOUS_X, PREVIOUS_Y, PREVIOUS_T, gui_helpers.cursor_on_text_box(
        PREVIOUS_X, PREVIOUS_Y, PREVIOUS_T, BUTTON_FONT))
    gui_helpers.draw_button(screen, NEXT_X, NEXT_Y, NEXT_T, gui_helpers.cursor_on_text_box(
        NEXT_X, NEXT_Y, NEXT_T, BUTTON_FONT))
    gui_helpers.draw_button(screen, LOAD_X, LOAD_Y, LOAD_T, gui_helpers.cursor_on_text_box(
        LOAD_X, LOAD_Y, LOAD_T, BUTTON_FONT))
        