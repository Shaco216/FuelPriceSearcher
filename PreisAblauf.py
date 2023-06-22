from IAblauf import IAblauf


class PreisAblauf(IAblauf):

    def __init__(self, URL,Tag):
        self._URL = URL
        self._tag = Tag

    def crawling(self):
        self._crawli.set_URL(self._URL)

    def filtering(self):
        self._filter.choose_Tag(self._tag)
