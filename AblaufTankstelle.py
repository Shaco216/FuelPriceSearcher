from IAblauf import IAblauf

class AblaufTankstelle(IAblauf):

    def __init__(self,tag,searchword):
        self._tag = tag
        self._searchword = searchword
    def __crawling(self, htmlcode):
        self.repository.set_code(htmlcode)
    def __filtering(self):
        self._filter.choose_Tag(self._tag)
        self._filter.change_multiple_values(True)
        self._filter.set_HTML_Code(self.repository.get_code())
        self._filter.search_for(self._searchword)
    def __collecting_data(self):
        for item in self._filter.get_current_results():
            self._results.append(item)
    def ablauf(self,htmlcode):
        self.__crawling(htmlcode)
        self.__filtering()
        self.__collecting_data()