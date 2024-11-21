import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self) -> None:
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()

        # palautetaan uusi arvo
        self.viitegeneraattori_mock.uusi.side_effect = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        self.varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 100
            if tuote_id == 2:
                return 25
            if tuote_id == 3:
                return 30
            if tuote_id == 4:
                return 40
            if tuote_id == 5:
                return 15
            return 0
        
        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "Koff Portteri", 3)
            if tuote_id == 2:
                return Tuote(2, "Fink Bräu I", 1)
            if tuote_id == 3:
                return Tuote(3, "Sierra Nevada Pale Ale", 5)
            if tuote_id == 4:
                return Tuote(4, "Mikkeller not just another Wit", 7)
            if tuote_id == 5:
                return Tuote(5, "Weihenstephaner Hefeweisse", 4)
            return None

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

    # tehdään testia
    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self): # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoksen_paaytyttya_tilisiirto_kutsutaan_oikeilla_arovoilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 1, "12345", "33333-44455", 3)

    def test_kahden_eri_tuotteen_ostoksen_paaytyttya_tilisiirto_kutsutaan_oikeilla_arvoilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 1, "12345", "33333-44455", 4)

    def test_kahden_saman_tuotteen_ostoksen_paaytyttya_tilisiirto_kutsutaan_oikeilla_arvoilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 1, "12345", "33333-44455", 6)

    def test_tuote_joka_on_loppu_ei_lisata_ostoskoriin(self):
        # jokin tuotteen varasto on 0
        def varasto_saldo_loppu(tuote_id):
            if tuote_id == 1:
                return 100
            if tuote_id == 2:
                return 0 # Fink Bräu varasto on 0
            return 0
        
        self.varasto_mock.saldo.side_effect = varasto_saldo_loppu

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)  # varastossa
        self.kauppa.lisaa_koriin(2)  # loppuu
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 1, "12345", "33333-44455", 3)
    
    def test_aloitta_asiointi_nollaa_ostokorin(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        
        #aloitetaan uusi osto
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 1, "12345", "33333-44455", 1)
    
    def test_kauppa_pyytaa_uuden_viitenumeron_jokaiselle_maksutapahtumalle(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")
        self.assertEqual(self.pankki_mock.tilisiirto.call_args_list[0][0][1], 1)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")
        self.assertEqual(self.pankki_mock.tilisiirto.call_args_list[1][0][1], 2)

    # luoka KAUPPA testauskattavuus 100%
    def test_poista_tuoetteet_korista(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.poista_korista(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 1, "12345", "33333-44455", 1)

