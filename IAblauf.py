from Crawler import Crawler
from HTML_SearchEngine import HTML_SearchEngine
from HTMLCodeRepository import *

class IAblauf:

    _crawli = Crawler()
    _filter = HTML_SearchEngine()
    #_htmlcode = "" vermutlich nicht mehr nötig
    _URL = ""
    _tag = ""
    _searchword = ""
    _results = []
    repository = HTMLCodeRepository()

    def __init__(self, URL,Tag,Searchword):
        self._URL = URL
        self._tag = Tag
        self._searchword = Searchword

    def __crawling(self):
        pass

    def __filtering(self):
        pass

    def __collecting_data(self):
        pass

    def ablauf(self):
        self.__crawling()
        self.__filtering()
        self.__collecting_data()
