from DataStructures.Graph import Graph
from Models.Truck import routeMiles
from Utils.dataHandler import *
from Utils.truckLoader import truckLoader


def userInterface(running):
    print("------------------------------------")
    print("C950")
    print("WGUPS Project")
    print("Joshua Dorsett")
    print("------------------------------------\n")

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
    saltLakeCity = Graph(locations, distances)
    trucks = truckLoader(packages)
    highPriorityTruck = trucks[0]
    mediumPriorityTruck = trucks[1]
    lowPriorityTruck = trucks[2]

    route1 = highPriorityTruck.createRoute(saltLakeCity, locations.getValue(0), locations)
    routeMiles1 = routeMiles(route1, saltLakeCity)
    route2 = mediumPriorityTruck.createRoute(saltLakeCity, locations.getValue(0), locations)
    routeMiles2 = routeMiles(route2, saltLakeCity)
    route3 = lowPriorityTruck.createRoute(saltLakeCity, locations.getValue(0), locations)
    routeMiles3 = routeMiles(route3, saltLakeCity)
    totalMiles = routeMiles1 + routeMiles2 + routeMiles3

    while running:

        inputStream = input("enter 'package' to lookup package information.\n"
                            "enter 'route' to lookup route information.\n"
                            "enter 'stop' to end program.\n")

        if inputStream == 'package':
            inputstream = input("type index of package\n")
            print(packages.getValue(inputStream))
            print("------------------------------------\n")

        elif inputStream == 'route':
            print("=========Route for truck one===========")
            print(routeMiles1, "miles\n")
            for i in range(len(route1)):
                print(route1[i].getTitle())
            print("\n")
            print("=========Route for truck two===========")
            print(routeMiles2, "miles\n")
            for i in range(len(route2)):
                print(route2[i].getTitle())
            print("\n")
            print("========Route for truck three============")
            print(routeMiles3, "miles\n")
            for i in range(len(route3)):
                print(route3[i].getTitle())
            print("\n")
            print("The total miles for all routes is", totalMiles)
            print("------------------------------------\n")


        elif inputStream == 'stop':
            running = False
