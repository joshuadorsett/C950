class Graph:
    def __init__(self, locations, distances):
        # takes a hash table of locations with the key being index and the value being the location object
        self._vertices = locations
        # take a hash table of distances with key being VertA and value being list of distance to vertB
        self._edges = distances

    def getDistance(self, vertA, vertB):
        # returns value from the matrix of distances in the hash table distances
        return self._edges.getValue(vertA)[vertB]