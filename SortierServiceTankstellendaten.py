from ISortService import ISortService
import logging


class SortierServiceTankstellendaten(ISortService):
    _name = []
    _strase = []
    _ort = []
    def __init__(self,tankstellendaten):
        self._unsortierte_datensaetze = tankstellendaten
    def sortiere_datensaetze(self):
        for item in self._unsoertierte_datensaetze:
            try:

