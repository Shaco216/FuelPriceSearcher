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
            #region name
            try:
                item = str(item)
                first_tankstelle_item_startpoint = item.find("/tankstelle/")
                end_of_string = len(item)
                item = item[first_tankstelle_item_startpoint:end_of_string]

            except:
                pass
            #endregion