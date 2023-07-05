from IAblauf import IAblauf

class AblaufPreis(IAblauf):

    def __crawling(self):
        self._crawli.set_URL(self._URL)
        self._crawli.Generate_HTML_Code_without_searchword()
        self.repository.set_code(self._crawli.get_html_code())

    def __filtering(self):
        self._filter.choose_Tag(self._tag)
        self._filter.change_multiple_values(True)
        self._filter.set_HTML_Code(self.repository.get_code())
        self._filter.search_for(self._searchword)

    def __collecting_data(self):
        for item in self._filter.get_current_results():
            self._results.append(item)

    def ablauf(self):
        self.__crawling()
        self.__filtering()
        self.__collecting_data()