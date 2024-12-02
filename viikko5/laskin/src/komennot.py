class Komento():
    def __init__(self, sovelluslogiikka, lue_syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._lue_syote = lue_syote

class Summa(Komento):
    def suorita(self):
        arvo = 0
        try:
            arvo = int(self._lue_syote())
        except Exception:
            pass
        self._sovelluslogiikka.plus(arvo)

class Erotus(Komento):
    def suorita(self):
        arvo = 0
        try:
            arvo = int(self._lue_syote())
        except Exception:
            pass
        self._sovelluslogiikka.miinus(arvo)

class Nollaus(Komento):
    def suorita(self):
        self._sovelluslogiikka.nollaa()

class Kumoa(Komento):
    def suorita(self):
        pass  # ei toteutettu vielä