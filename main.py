import platform

import EnumTags
from AblaufPreis import AblaufPreis
from SortierServicePreis import SortierServicePreis
from AblaufTankstelle import AblaufTankstelle
from SortierServiceTankstellendaten import SortierServiceTankstellendaten
from DBServiceManagement_Windows import DBServiceManagement

#region preisdatenHolen
p_ablauf = AblaufPreis("https://ich-tanke.de/tankstellen/super-e5/umkreis/lauingen-donau/", EnumTags.Tags.underscore_class.value, "preis1")
p_ablauf.ablauf()
preis_daten = p_ablauf._results
print(preis_daten)
repo = p_ablauf.repository.get_code()
preis_sorter = SortierServicePreis(preis_daten)
preis_sorter.sortiere_datensaetze()
print(preis_sorter.ausgabe_preis())
print(preis_sorter.ausgabe_datum())
print(preis_sorter.ausgabe_uhrzeit())
#endregion

#region tankstellenDatenHolen
t_ablauf = AblaufTankstelle(EnumTags.Tags.underscore_class.value,"tankstelle")
t_ablauf.ablauf(repo)
tankstelle_daten = t_ablauf._results
print(tankstelle_daten)
tankstellen_sorter = SortierServiceTankstellendaten(tankstelle_daten)
tankstellen_sorter.sortiere_datensaetze()
print(tankstellen_sorter.ausgabe_namen_liste())
print(tankstellen_sorter.ausgabe_strasen_liste())
print(tankstellen_sorter.ausgabe_orte_liste())
#endregion

#region DBservice starten
operationsystem = platform.system()
if operationsystem == 'Windows' or operationsystem == 'windows':
    DBServManagement_windows = DBServiceManagement()
    status = DBServManagement_windows.check_service_is_running('MySQL80')
    if status != 0 or status != '0':
        DBServManagement_windows.start_service('MySQL80')
    else:
        print('Service läuft bereits.')
#endregion