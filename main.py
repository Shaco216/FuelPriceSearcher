import EnumTags
from AblaufPreis import AblaufPreis
from SortierServicePreis import SortierServicePreis
from AblaufTankstelle import AblaufTankstelle
from SortierServiceTankstellendaten import SortierServiceTankstellendaten

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
t_ablauf = AblaufTankstelle(EnumTags.Tags.underscore_class.value,"tankstelle")
t_ablauf.ablauf(repo)
tankstelle_daten = t_ablauf._results
print(tankstelle_daten)
tankstellen_sorter = SortierServiceTankstellendaten(tankstelle_daten)