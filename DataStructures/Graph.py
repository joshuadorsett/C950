class Graph:
    def __init__(self, locations, distances):
        # takes a hash table of locations with the key being index and the value being the location object
        self._vertices = locations
        self._size = locations.getSize()
        # take a hash table of distances with key being VertA and value being list of distance to vertB
        self._edges = distances

    def getDistance(self, vertA, vertB):
        # each location object carries with it a list of distances to all other vertices
        return self._edges.getValue(vertA)[vertB]