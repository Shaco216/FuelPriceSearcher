from ISortService import ISortService
import logging


class SortierServicePreis(ISortService):
    _preis = []
    _datum = []
    _uhrzeit = []

    def __add_to_list(self, preis, datum, uhrzeit):
        self._preis.append(preis)
        self._datum.append(datum)
        self._uhrzeit.append(uhrzeit)

    def sortiere_datensaetze(self):
        preis = ''
        datum = ''
        uhrzeit = ''
        for item in self._unsoertierte_datensaetze:
            #region preis
            try:
                item = str(item)
                item = item.replace('<div class="preis1"><span class="zahl" title="Preisangabe in Euro">', "")
                preis = item[0:4]
            except:
                logging.exception("Fehler bei Preisfilterung")
            #endregion
            #region datum
            try:
                laenge_item = len(item)
                zeichenanzahl_preis = 4
                item = item[4:laenge_item]
                title_start_position = item.find(":")
                laenge_datum_string = 10
                start_von_datum = 2
                datum = item[title_start_position + start_von_datum:title_start_position + laenge_datum_string]
            except:
                logging.exception("Fehler bei Datumfilterung")
            #endregion
            #region uhrzeit
            try:
                after_date_position = item.find(",")
                uhrzeit_start = after_date_position + 2
                uhrzeit_ende = uhrzeit_start + 5
                uhrzeit = item[uhrzeit_start:uhrzeit_ende]
            except:
                logging.exception("Fehler bei Uhrzeitfilterung")
            #endregion
            self.__add_to_list(preis, datum, uhrzeit)

    def ausgabe_preis(self):
        return self._preis

    def ausgabe_datum(self):
        return self._datum

    def ausgabe_uhrzeit(self):
        return self._uhrzeit

    def ausgabe_sortierte_datensaetze(self):
        ausgabe = {"preise": self.ausgabe_preis(),
                   "datum": self.ausgabe_datum(),
                   "uhrzeit": self.ausgabe_uhrzeit()}
        return ausgabe

    def ausgabe_unsortierte_datensaetze(self):
        return self._unsoertierte_datensaetze
