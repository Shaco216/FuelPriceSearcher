from IAblauf import IAblauf

class PreisAblauf(IAblauf):

    def _crawling(self):
        self._crawli.set_URL(self._URL)

    def _filtering(self):
        self._filter.choose_Tag(self._tag)
        self._filter.change_multiple_values(True)
        self._filter.search_for(self._searchword)

    def _collecting_data(self):
        for item in self._filter.get_current_results():
            self._results.append(item)

    def ablauf(self):
        self._crawling()
        self._filtering()
        self._collecting_data()