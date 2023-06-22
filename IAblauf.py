from Crawler import Crawler
from HTML_SearchEngine import HTML_SearchEngine


class IAblauf:

    _crawli = Crawler()
    _filter = HTML_SearchEngine()
    _URL = ""
    _tag = ""
    _searchword = ""
    def crawling(self, URL):
        pass

    def filtering(self):
        pass

    def collecting_data(self):
        pass

    def ablauf(self):
        self.crawling(self._URL)
        self.filtering()
        self.collecting_data()
