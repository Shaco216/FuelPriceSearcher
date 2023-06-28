from PreisAblauf import PreisAblauf


class ISortService:
    _unsoertierte_datensaetze = []
    _sortierte_datensaetze = {}



    def  __init__(self, daten):
        self._unsoertierte_datensaetze = daten

    def sortiere_datensaetze(self):
        pass

    def ausgabe_sortierte_datensaetze(self):
        pass

    def ausgabe_unsortierte_datensaetze(self):
        pass