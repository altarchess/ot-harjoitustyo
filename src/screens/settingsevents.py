import pygame
import entity.settings
import gui.externalsettings
import guihelpers
from defs import *

class SettingsEvents:
    def __init__(self):
        self.settings = entity.settings.Settings()

    def tick(self, screen, events):
        gui.externalsettings.render(screen, events, self.settings)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(self.settings.settings)):
                    if guihelpers.cursor_on_text_box(X_OFFSET, OPTIONS_Y_OFFSET * (i + 1), self.settings.settings[i].name + " " + str(self.settings.settings[i].value_array[self.settings.settings[i].index]), BUTTON_FONT):
                        self.settings.settings[i].index += 1
                        if self.settings.settings[i].index >= len(self.settings.settings[i].value_array):
                            self.settings.settings[i].index = 0