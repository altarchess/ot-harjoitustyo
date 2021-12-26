import pygame
import entity.settings
import gui.external_settings
from gui import gui_helpers
from misc.defs import X_OFFSET, OPTIONS_Y_OFFSET, BUTTON_FONT


class SettingsEvents:

    """
    Luokka kasittelee asetusvalikon specifeja tapahtumia

    Attributes:
        settings: asetukset joita muokataan tapahtumien mukaan
    """

    def __init__(self):
        self.settings = entity.settings.Settings()

    def tick(self, screen, events):
        """
        Jokaisen ruudun piiroksen aikana kasitellaan hiirinappauspainallukset 
        mikali painetaan jotain nappulaa.

        Args:
            screen: pygame ruutu johon lauta halutaan pirtaa
            events: pygamen tapahtumat joita kasitellaan
        """

        gui.external_settings.render(screen, events, self.settings)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(self.settings.settings)):
                    if gui_helpers.cursor_on_text_box(X_OFFSET, OPTIONS_Y_OFFSET * (i + 1), self.settings.settings[i].name + " " + str(self.settings.settings[i].value_array[self.settings.settings[i].index]), BUTTON_FONT):
                        self.settings.settings[i].index += 1
                        if self.settings.settings[i].index >= len(self.settings.settings[i].value_array):
                            self.settings.settings[i].index = 0
