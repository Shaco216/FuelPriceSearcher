from ISortService import ISortService
import logging


class SortierServiceTankstellendaten(ISortService):
    _namen = []
    _strasen = []
    _plz = []
    _ortsname = []
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
                    laenge_name_end = len("-Tankstelle anzeigen")
                    temporaerer_name = item[name_start+laenge_start:name_end]
                    self._namen.append(temporaerer_name)
                    item = item[laenge_name_end+name_end:]
                    #print(item)
            except:
                fehlermeldung = "Es gab einen Fehler bei der Namensfindung"
                logging.exception(fehlermeldung)
                print(fehlermeldung)
            #endregion
            #region strase
            try:
                if '</h4><p>' in item:
                    start_strase = item.find("</h4><p>")
                    laenge_start_strase = len("</h4><p>")
                    end_strase = item.find(' · <a href="/tankstellen')
                    laenge_end_strase = len(' · <a href="/tankstellen')
                    temporaere_strase = item[start_strase+laenge_start_strase:end_strase]
                    self._strasen.append(temporaere_strase)
                    item = item[end_strase+laenge_end_strase:]
            except:
                fehlermeldung = "Es gab einen Fehler bei der Strasenfindung"
                logging.exception(fehlermeldung)
                print(fehlermeldung)
            #endregion
            #region ort
            ort_eingrenzung = item.find('title="')
            ort_ende = item.find('</a></p><p>')
            #item weiter eingrenzen
            ort_anfang = item.find('">')
            laenge_ort_anfang = len('">')
            temporaerer_ort = item[ort_anfang+laenge_ort_anfang:ort_anfang+laenge_ort_anfang+5]
            gepruefter_ort = ''
            laenge_gepruefter_ort = 0
            for i in temporaerer_ort:
                try:
                    i = int(i)
                    if type(i) is int:
                        gepruefter_ort = gepruefter_ort + str(i)
                except:
                    fehlermeldung = f'Konvertierungsfehler bei {i}'
                    logging.exception(fehlermeldung)
                    print(fehlermeldung)
            if gepruefter_ort != '':
                self._plz.append(gepruefter_ort)
                # Name der Ortschaft wird extrahiert
                laenge_gepruefter_ort = len(gepruefter_ort)

                item = item[ort_eingrenzung:]

                ende_plz = item.find(gepruefter_ort)
                #3 stellen von plz und leerzeichen
                reststellen = 4
                ort_ende_nach_verkürzung = item.find('</a></p><p>')
                ortsname = item[ende_plz+laenge_ort_anfang+reststellen:ort_ende_nach_verkürzung]
                #print(ortsname)
                self._ortsname.append(ortsname)
            #endregion
    def ausgabe_unsortierte_datensaetze(self):
        return self._unsortierte_datensaetze
    def ausgabe_namen_liste(self):
        return self._namen
    def ausgabe_strasen_liste(self):
        return self._strasen
    def ausgabe_plz_liste(self):
        return self._plz
    def ausgabe_ortsname_liste(self):
        return self._ortsname
    def ausgabe_sortierte_datensaetze(self):
        ausgabe = {"namen": self.ausgabe_namen_liste(),
                   "strasen": self.ausgabe_strasen_liste(),
                   "plz": self.ausgabe_plz_liste(),
                   "ortsname": self.ausgabe_ortsname_liste()}
        return ausgabe