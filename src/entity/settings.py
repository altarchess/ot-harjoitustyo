from misc.defs import *


class Setting:

    """
    Luokka kuvaa yksittaista asetusta
    """

    def __init__(self, name, value_array, index=0):
        self.name = name
        self.value_array = value_array
        self.index = index


class Settings:

    """
    Luokka kasittelee asetuksia yhtenaisesti.
    """

    def __init__(self):
        """
        Listataan asetukset joita voi muuttaa
        """

        self.settings = []
        self.settings.append(Setting(AI_LEVEL, [1, 2, 3, 4, 5], 2))
        self.settings.append(Setting(SHOW_LEGAL, ["ON", "OFF"], 0))

    def get_setting(self, name):
        """
        Palauttaa asetuksen arvon kun kysytaan asetuksen nimella

        Args:
            name: Asetuksen nimi

        Returns:
            Asetuksen arvo
        """

        for setting in self.settings:
            if name == setting.name:
                return setting.value_array[setting.index]
        return 0
