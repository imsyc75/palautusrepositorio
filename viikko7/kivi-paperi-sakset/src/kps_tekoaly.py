from kps_base import KiviPaperiSakset
from tekoaly import Tekoaly

class KPSTekoaly(KiviPaperiSakset):
    def __init__(self):
        self.tekoaly = self._luo_tekoaly()

    def _luo_tekoaly(self):
        return Tekoaly()

    def _toisen_siirto(self, ensimmaisen_siirto):
        siirto = self.tekoaly.anna_siirto()
        self.tekoaly.aseta_siirto(ensimmaisen_siirto)
        print(f"Tietokone valitsi: {siirto}")
        return siirto