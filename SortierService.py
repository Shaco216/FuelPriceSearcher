from ISortService import ISortService


class SortierService(ISortService):

    def sortiere_datensaetze(self):
        preis = ''
        datum = ''
        uhrzeit = ''
        for item in self._unsoertierte_datensaetze:
            try:
                item = str(item)
                item.replace('<div class="preis1"><span class="zahl" title="Preisangabe in Euro">',"")
                preis = item[0:4]
            except:
                print("Ein Fehler ist beim Preisauslesen passiert")
                with()
