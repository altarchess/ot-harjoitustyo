from gui import gui_helpers
from misc.defs import ENGINE_MOVE_X, ENGINE_MOVE_Y, X_OFFSET
from misc.defs import OPTIONS_Y_OFFSET, BUTTON_FONT


def render(screen, events, settings):
    """
    Piirtaa asetusmenuun

    Args:
        Screen: pygame ruutu johon piirretaan
        events: pygame tapahtumat
        settings: asetukset jotka halutaan piirtaa
    """

    gui_helpers.draw_button(screen, ENGINE_MOVE_X, ENGINE_MOVE_Y, "Go Back", gui_helpers.cursor_on_text_box(
        ENGINE_MOVE_X, ENGINE_MOVE_Y, "Go Back", BUTTON_FONT))

    for i in range(len(settings.settings)):
        gui_helpers.draw_button(screen, X_OFFSET, OPTIONS_Y_OFFSET * (i + 1), settings.settings[i].name + " " + str(settings.settings[i].value_array[settings.settings[i].index]), gui_helpers.cursor_on_text_box(
            X_OFFSET, OPTIONS_Y_OFFSET * (i + 1), str(settings.settings[i].value_array[settings.settings[i].index]), BUTTON_FONT))
