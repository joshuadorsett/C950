from Utils.dataHandler import makeHashTableOfDistances, makeHashTableOfLocations


# the Graph class has two hash tables of all vertices and edges
class Graph:
    def __init__(self):
        # vertices are initialized by calling the function below
        # this function returns a hash table of all locations
        # time - O(n^2)
        self._vertices = makeHashTableOfLocations()

        # edges are initialized by calling the function below
        # this function returns a hash table of all distances
        # the Key is the starting point
        # the Value is a list of distances to all other location indexes
        # time - O(n^2)
        self._edges = makeHashTableOfDistances()

    # returns a distance value from the hash table of distances
    # time - O(1)
    def getDistance(self, vertA, vertB):
        # returns distance value from the matrix of distances in the hash table distances
        # converts it to from string to float here to avoid a nested loop of converting them in dataHandler.py
        return float(self._edges.getValue(vertA)[vertB])

    # returns the hash table of locations
    # time - O(1)
    def getLocations(self):
        return self._vertices
