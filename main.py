from DataStructures.Graph import *
from Data.dataHandler import *
from Models.Truck import Truck

if __name__ == "__main__":
    # make 3 hash tables of locations, distances and packages
    locations = makeHashTableOfLocations()
    distances = makeHashTableOfDistances()
    packages = makeHashTableOfPackages()

    # distance lists added to each location
    for i in range(len(distances.getValue(0))):
        location = locations.getValue(i)
        distancesList = distances.getValue(i)
        location.setListOfDistances(distancesList)

    # build a graph of locations
    # each location is responsible for its own list of distances
    map = Graph(locations)

    #create truck objects
    truck1 = Truck(1)
    truck2 = Truck(2)

    #load trucks
    for i in range(16):
        package = packages.getValue(i)
        truck1.addCargo(package)
        package2 = packages.getValue(i+16)
        truck2.addCargo(package2)

    p = truck1.getPackages().getValue(15)
    print(p._address)
