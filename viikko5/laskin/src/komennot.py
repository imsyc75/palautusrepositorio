class Komento:
    def __init__(self, sovelluslogiikka, lue_syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._lue_syote = lue_syote
        self._edellinen_arvo = 0

class Summa(Komento):
    def suorita(self):
        self._edellinen_arvo = self._sovelluslogiikka.arvo()
        arvo = 0
        try:
            arvo = int(self._lue_syote())
        except Exception:
            pass
        self._sovelluslogiikka.plus(arvo)

    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self._edellinen_arvo)

class Erotus(Komento):
    def suorita(self):
        self._edellinen_arvo = self._sovelluslogiikka.arvo()
        arvo = 0
        try:
            arvo = int(self._lue_syote())
        except Exception:
            pass
        self._sovelluslogiikka.miinus(arvo)

    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self._edellinen_arvo)

class Nollaus(Komento):
    def suorita(self):
        self._edellinen_arvo = self._sovelluslogiikka.arvo()
        self._sovelluslogiikka.nollaa()

    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self._edellinen_arvo)