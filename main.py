from DataStructures.Graph import *
from Utils.dataHandler import *
from Utils.truckLoader import truckLoader

if __name__ == "__main__":
    # make 3 hash tables of locations, distances and packages
    locations = makeHashTableOfLocations()
    distances = makeHashTableOfDistances()
    packages = makeHashTableOfPackages()

    # distance lists added to each location
    # each location is responsible for its own distances to all other locations
    for i in range(len(distances.getValue(0))):
        location = locations.getValue(i)
        distancesList = distances.getValue(i)
        location.setListOfDistances(distancesList)

    # build a graph of locations
    saltLakeCity = Graph(locations)

    # setting the graph index of each package
    for i in range(locations.getSize()):
        packages.getValue(i).setGraphIndex(locations)

    # create and load trucks
    # returns a list of all trucks
    trucks = truckLoader(packages)
    truck1 = trucks[0]
    truck2 = trucks[1]
    truck3 = trucks[2]

    p = truck2.getPackages().getValue(16)
    print(p.getId())
