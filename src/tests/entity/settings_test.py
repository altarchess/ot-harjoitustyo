import unittest
from entity.settings import Settings
from misc.defs import SHOW_LEGAL

class TestSettings(unittest.TestCase):

    """
    Testaa asetuksista vastaavaa luokkaa
    """

    def setUp(self):

        """
        Luodaan testeissa kaytettava Settings objekti
        """

        self.settings = Settings()

    def test_get_setting(self):

        """
        Testaa palauttaako get_setting funktio oikean arvon
        """
        self.assertEqual(self.settings.get_setting(SHOW_LEGAL), "ON")