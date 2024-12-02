KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = self._tarkistaa_parametri(kapasiteetti, KAPASITEETTI, "Väärä kapasiteetti")
        self.kasvatuskoko = self._tarkistaa_parametri(kasvatuskoko, OLETUSKASVATUS, "kapasiteetti2") 
        self.luvut = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0
    
    def _tarkistaa_parametri(self, arvo, oletus, virheviesti):
        if arvo is None:
            return oletus
        if not isinstance(arvo, int) or arvo < 0:
            raise Exception(virheviesti)
        return arvo

    def kuuluu(self, luku):
        return luku in self.luvut[:self.alkioiden_lkm]

    def lisaa(self, luku):
        if self.kuuluu(luku):
            return False
            
        if self.alkioiden_lkm >= len(self.luvut):
            uusi_lista = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
            self._kopioi_lista(self.luvut, uusi_lista)
            self.luvut = uusi_lista
            
        self.luvut[self.alkioiden_lkm] = luku
        self.alkioiden_lkm += 1
        return True
    
    def poista(self, luku):
        for i in range(self.alkioiden_lkm):
            if self.luvut[i] == luku:
                self._siirra_alkioita_vasemmalle(i)
                self.alkioiden_lkm -= 1
                return True
        return False
    
    def _siirra_alkioita_vasemmalle(self, alkuindeksi):
        for i in range(alkuindeksi, self.alkioiden_lkm - 1):
            self.luvut[i] = self.luvut[i + 1]
        self.luvut[self.alkioiden_lkm - 1] = 0

    def _kopioi_lista(self, lahde, kohde):
        for i in range(len(lahde)):
            kohde[i] = lahde[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.luvut[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def yhdiste(a, b):
        tulos = IntJoukko()
        for alkio in a.to_int_list() + b.to_int_list():
            tulos.lisaa(alkio)
        return tulos

    @staticmethod
    def leikkaus(a, b):
        tulos = IntJoukko()
        for alkio in a.to_int_list():
            if b.kuuluu(alkio):
                tulos.lisaa(alkio)
        return tulos

    @staticmethod
    def erotus(a, b):
        tulos = IntJoukko()
        for alkio in a.to_int_list():
            if not b.kuuluu(alkio):
                tulos.lisaa(alkio)
        return tulos

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        return "{" + ", ".join(str(x) for x in self.luvut[:self.alkioiden_lkm]) + "}"