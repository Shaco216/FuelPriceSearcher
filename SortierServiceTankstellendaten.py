from ISortService import ISortService
import logging


class SortierServiceTankstellendaten(ISortService):
    _namen = []
    _strase = []
    _ort = []
    def __init__(self,tankstellendaten):
        self._unsortierte_datensaetze = tankstellendaten
    def sortiere_datensaetze(self):
        for item in self._unsortierte_datensaetze:
            #region name
            try:
                item = str(item)
                if "/tankstelle/" in item:
                    first_tankstelle_item_startpoint = item.find("/tankstelle/")
                    end_of_string = len(item)
                    item = item[first_tankstelle_item_startpoint:end_of_string]
                    print("first: " + str(first_tankstelle_item_startpoint) +
                        " last: " + str(end_of_string) +
                        " text: " + str(item))
                    name_start = item.find("Preise und Details der ")
                    laenge_start = len("Preise und Details der ")
                    name_end = item.find("-Tankstelle anzeigen")
                    temporaerer_name = item[name_start+laenge_start:name_end]
                    self._namen.append(temporaerer_name)
            except:
                fehlermeldung = "Es gab einen Fehler bei der Namensfindung"
                logging.exception(fehlermeldung)
                print(fehlermeldung)
            #endregion
    def ausgabe_unsortierte_datensaetze(self):
        return self._unsortierte_datensaetze
    def ausgabe_namen_liste(self):
        return self._namen