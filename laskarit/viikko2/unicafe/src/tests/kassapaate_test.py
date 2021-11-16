import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
        
    def test_oikea_kuin_aloittaa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset+self.kassapaate.maukkaat, 0)

    def test_kateistoimii_ed(self):
        vaihto = self.kassapaate.syo_edullisesti_kateisella(440)
        self.assertEqual(100240, self.kassapaate.kassassa_rahaa)
        self.assertEqual(vaihto, 200)
        self.assertEqual(self.kassapaate.maukkaat+self.kassapaate.edulliset, 1)
        self.kassapaate.syo_edullisesti_kateisella(20)

    def test_kateistoimii_maukas(self):
        vaihto = self.kassapaate.syo_maukkaasti_kateisella(440)
        self.assertEqual(100400, self.kassapaate.kassassa_rahaa)
        self.assertEqual(vaihto, 40)
        self.assertEqual(self.kassapaate.maukkaat+self.kassapaate.edulliset, 1)
        self.kassapaate.syo_maukkaasti_kateisella(20)


    def test_kateistoimii_joseitomii(self):
        vaihto = self.kassapaate.syo_edullisesti_kateisella(190)    
        self.assertEqual(190, vaihto)
        self.assertEqual(self.kassapaate.maukkaat+self.kassapaate.edulliset, 0)

    def test_kortti_ed(self):
        Onistuiko = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(Onistuiko, True)
        self.assertEqual(self.maksukortti.saldo, 760)
        self.assertEqual(self.kassapaate.edulliset+self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.maksukortti.saldo = 10
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

    def test_kortti_maukas(self):
        Onistuiko = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(Onistuiko, True)
        self.assertEqual(self.maksukortti.saldo, 600)
        self.assertEqual(self.kassapaate.edulliset+self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortti_ei_tarpkeeksi(self):
        self.maksukortti.saldo = 2
        Onistuiko = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(Onistuiko, False)
        self.assertEqual(self.kassapaate.edulliset+self.kassapaate.maukkaat, 0)
        self.assertEqual(self.maksukortti.saldo, 2)

    def test_lataa_kortille(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.maksukortti.saldo, 1100)
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1)
        self.assertEqual(self.maksukortti.saldo, 1100)