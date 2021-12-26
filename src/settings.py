import pygame
import guihelpers
from defs import *


class Setting:
    def __init__(self, name, value_array, index=0):
        self.name = name
        self.value_array = value_array
        self.index = index


class Settings:
    def __init__(self):
        self.settings = []
        self.settings.append(Setting(AI_LEVEL, [1, 2, 3, 4, 5], 2))
        self.settings.append(Setting(SHOW_LEGAL, ["ON", "OFF"]))

    def get_setting(self, name):
        for setting in self.settings:
            if name == setting.name:
                return setting.value_array[setting.index]

    def render(self, screen, events):
        guihelpers.draw_button(screen, ENGINE_MOVE_X, ENGINE_MOVE_Y, "Go Back", guihelpers.cursor_on_text_box(
            ENGINE_MOVE_X, ENGINE_MOVE_Y, "Go Back", BUTTON_FONT))

        for i in range(len(self.settings)):
            guihelpers.draw_button(screen, X_OFFSET, OPTIONS_Y_OFFSET * (i + 1), self.settings[i].name + " " + str(self.settings[i].value_array[self.settings[i].index]), guihelpers.cursor_on_text_box(
                X_OFFSET, OPTIONS_Y_OFFSET * (i + 1), str(self.settings[i].value_array[self.settings[i].index]), BUTTON_FONT))

    def tick(self, screen, events):
        self.render(screen, events)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(self.settings)):
                    if guihelpers.cursor_on_text_box(X_OFFSET, OPTIONS_Y_OFFSET * (i + 1), self.settings[i].name + " " + str(self.settings[i].value_array[self.settings[i].index]), BUTTON_FONT):
                        self.settings[i].index += 1
                        if self.settings[i].index >= len(self.settings[i].value_array):
                            self.settings[i].index = 0
