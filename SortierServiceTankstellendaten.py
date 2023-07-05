from ISortService import ISortService
import logging


class SortierServiceTankstellendaten(ISortService):
    _name = []
    _strase = []
    _ort = []
    def __init__(self,preisdaten,tankstellendaten):
        tempdata = []
        iterationen_tankstellendaten = len(tankstellendaten)-len(preisdaten)
        for t_daten_pos in range(iterationen_tankstellendaten):
            tempdata.append(tankstellendaten[range(preisdaten)+t_daten_pos])
        self._unsortierte_datensaetze = tempdata
        print(tempdata)
    def sortiere_datensaetze(self):
        for item in self._unsoertierte_datensaetze:
            pass
