from gui import guihelpers
from defs import ENGINE_MOVE_X, ENGINE_MOVE_Y, X_OFFSET
from defs import OPTIONS_Y_OFFSET, BUTTON_FONT


def render(screen, events, settings):
    guihelpers.draw_button(screen, ENGINE_MOVE_X, ENGINE_MOVE_Y, "Go Back", guihelpers.cursor_on_text_box(
        ENGINE_MOVE_X, ENGINE_MOVE_Y, "Go Back", BUTTON_FONT))

    for i in range(len(settings.settings)):
        guihelpers.draw_button(screen, X_OFFSET, OPTIONS_Y_OFFSET * (i + 1), settings.settings[i].name + " " + str(settings.settings[i].value_array[settings.settings[i].index]), guihelpers.cursor_on_text_box(
            X_OFFSET, OPTIONS_Y_OFFSET * (i + 1), str(settings.settings[i].value_array[settings.settings[i].index]), BUTTON_FONT))
