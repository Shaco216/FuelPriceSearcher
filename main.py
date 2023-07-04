import EnumTags
from PreisAblauf import PreisAblauf
from SortierServicePreis import SortierServicePreis

p_ablauf = PreisAblauf("https://ich-tanke.de/tankstellen/super-e5/umkreis/lauingen-donau/",EnumTags.Tags.underscore_class.value,"preis1")
p_ablauf.ablauf()
daten = p_ablauf._results
print(daten)
sorter = SortierServicePreis(daten)
sorter.sortiere_datensaetze()
print(sorter.ausgabe_preis())
print(sorter.ausgabe_datum())
print(sorter.ausgabe_uhrzeit())
