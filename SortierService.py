from ISortService import ISortService
import logging


class SortierService(ISortService):

    def sortiere_datensaetze(self):
        preis = ''
        datum = ''
        uhrzeit = ''
        for item in self._unsoertierte_datensaetze:
            try:
                item = str(item)
                item.replace('<div class="preis1"><span class="zahl" title="Preisangabe in Euro">',"")
                preis = item[0:3]
            except:
                logging.exception("Fehler bei Preisfilterung")
            try:
                laenge_item_ohne_preis = len(item) - 4
                item = item[-laenge_item_ohne_preis]
                item.find
            except:


