class Graph:
    def __init__(self, locations):
        # takes a hash table of locations with the key being index and the value being the location object
        self._vertices = locations

    def getDistance(self, locationAIndex, locationBIndex):
        # each location object carries with it a list of distances to all other vertices
        location = self._vertices.getValue(locationAIndex)
        return location.getDistance(locationBIndex)