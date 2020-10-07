class Location:

    def __init__(self, index, title, address, zipCode):
        self._index = index
        self._title = title
        self._address = address
        self._city = "Salt Lake City"
        self._zipCode = zipCode
        self._listOfDistances = []
        self._packages = []

    def setListOfDistances(self, list):
        self._listOfDistances = list

    def dropOffPackage(self, package):
        self._packages.append(package)

    def getPackages(self):
        return self._packages

    def getAddress(self):
        return self._address

    def getIndex(self):
        return self._index

    def getTitle(self):
        return self._title

    def getDistance(self, locationBIndex):
        return self._listOfDistances[locationBIndex]