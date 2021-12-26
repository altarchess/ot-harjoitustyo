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
        return 0