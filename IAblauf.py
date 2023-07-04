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

    def _crawling(self):
        pass

    def _filtering(self):
        pass

    def _collecting_data(self):
        pass

    def ablauf(self):
        self.crawling()
        self.filtering()
        self.collecting_data()
