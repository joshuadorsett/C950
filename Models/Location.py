# location class defines a location/vertices inside of the graph class
class Location:
    # constructor initializes given argument values
    def __init__(self, index, title, address, zipCode):
        self._index = index
        self._title = title
        self._address = address
        self._zipCode = zipCode

    # getters
    def getAddress(self):
        return self._address

    def getIndex(self):
        return self._index

    def getTitle(self):
        return self._title
