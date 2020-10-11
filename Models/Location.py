# class location
class Location:

    def __init__(self, index, title, address, zipCode):
        self._index = index
        self._title = title
        self._address = address
        self._city = "Salt Lake City"
        self._zipCode = zipCode

    def getAddress(self):
        return self._address

    def getIndex(self):
        return self._index

    def getTitle(self):
        return self._title
