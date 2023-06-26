import EnumTags
from PreisAblauf import PreisAblauf

p_ablauf = PreisAblauf("https://ich-tanke.de/tankstellen/super-e5/umkreis/lauingen-donau/",EnumTags.Tags.underscore_class.value,"preis1")
p_ablauf.ablauf()