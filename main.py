import platform

import EnumTags
from AblaufPreis import AblaufPreis
from DBConnDataGatherer import DBConnDataGatherer
from Datenbankverbindung_Ort import Datenbankverbindung_Ort
from Datenbankverbindung_Tankstelle import Datenbankverbindung_Tankstelle
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
print(tankstellen_sorter.ausgabe_plz_liste())
#endregion

#region DBservice starten
operationsystem = platform.system()
if operationsystem == 'Windows' or operationsystem == 'windows':
    DBServManagement_windows = DBServiceManagement()
    status = DBServManagement_windows.check_service_is_running()
    print(f"Status des Datenbankprozesses: {status}")
    if status != "Running":
        DBServManagement_windows.start_service('MySQL80')
        print(f"Status des Datenbankprozesses: {status}")
#endregion

#region DBLoginData
dbLoginDaten = DBConnDataGatherer()
dbLoginDaten.set_port(3306)
dbLoginDaten.set_host("localhost")
dbLoginDaten.set_user("root")
dbLoginDaten.set_password("root")
dbLoginDaten.set_dbName("fuelpricesearcher")

host = dbLoginDaten.get_host()
user = dbLoginDaten.get_user()
port = dbLoginDaten.get_port()
password = dbLoginDaten.get_password()
dbname = dbLoginDaten.get_dbName()
#endregion

#region DBDataspeichern Ort
DB_Speicherbot_Ort = Datenbankverbindung_Ort(host=host,port=port,user=user,password=password,databasename=dbname)
print(tankstellen_sorter.sortiere_datensaetze())
for i in range(tankstellen_sorter.ausgabe_plz_liste()):
    plz = tankstellen_sorter.ausgabe_plz_liste()[i]
    orts_name = tankstellen_sorter.ausgabe_ortsname_liste()[i]
    DB_Speicherbot_Ort.insert_sql_command([plz, orts_name])
#endregion

#region DBDataspeichern Tankstelle
DB_Speicherbot_Tankstelle = Datenbankverbindung_Tankstelle(host=host,port=port,user=user,password=password,databasename=dbname)
for i in range(tankstellen_sorter.ausgabe_namen_liste()):
    tankstellen_name = tankstellen_sorter.ausgabe_namen_liste()[i]
    plz = tankstellen_sorter.ausgabe_plz_liste()[i]
#endregion

