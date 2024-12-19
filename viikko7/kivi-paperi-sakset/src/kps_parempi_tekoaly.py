from kps_tekoaly import KPSTekoaly
from tekoaly_parannettu import TekoalyParannettu

class KPSParempiTekoaly(KPSTekoaly):
    def _luo_tekoaly(self):
        return TekoalyParannettu(10)
