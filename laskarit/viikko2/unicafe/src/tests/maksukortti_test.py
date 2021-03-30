import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_on_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 10)

    def test_lataaminen_kasvattaa_oikein(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(self.maksukortti.saldo, 20)

    def test_lataaminen_kasvattaa_oikein(self):
        self.assertEqual(self.maksukortti.ota_rahaa(5), True)
        self.assertEqual(self.maksukortti.ota_rahaa(10), False)

    def test_str(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")