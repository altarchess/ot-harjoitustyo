import unittest
from entity.settings import Settings
from misc.defs import SHOW_LEGAL

class TestSettings(unittest.TestCase):
    def setUp(self):
        self.settings = Settings()

    def test_get_setting(self):
        self.assertEqual(self.settings.get_setting(SHOW_LEGAL), "ON")