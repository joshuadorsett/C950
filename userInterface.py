from DataStructures.Graph import Graph
from Models.Truck import routeMiles
from Utils.dataHandler import *
from Utils.truckLoader import truckLoader
from Utils.time import getRouteListVisited


#  Provide an interface for the insert and look-up functions to view the status of any package at any time.
#  This function should return all information about each package, including delivery status.

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

        inputStream = input("enter 'p' to lookup a package at a certain time.\n"
                            "enter 'r' to lookup routes.\n"
                            "enter 'a' to print all package information for a certain time.\n"
                            "enter 'e' to end program.\n")

        # if inputStream == 'package':
        #     inputStream = input("type index of package\n")
        #     packages.getValue(inputStream).print()
        #     print("------------------------------------\n")
        if inputStream == 'p':
            packageIndex = input("type index of package\n")
            package = None
            if int(packageIndex) < 40:
                package = packages.getValue(packageIndex)
            else:
                print("package not found, please enter number less than 40.")
                packageIndex = input("type index of package\n")
                package = packages.getValue(packageIndex)

            time = input("enter a time to lookup in the format 'hh:mm'."
                         "\nplease use 24 hour time.\n")

            truck = package.getTruck()
            route = truck.getRoute()
            timeTruckLeftHub = truck.getTimeLeftHub()
            routeListVisited = getRouteListVisited(timeTruckLeftHub, time, route)
            numberOfLocationsVisited = len(routeListVisited)
            packagesDelivered = []
            for p in truck.getPackages():
                for i in range(numberOfLocationsVisited):
                    if p.getAddress() == routeListVisited[i][0].getAddress():
                        p.setDeliveryStatus("delivered at " + routeListVisited[i][1])
                        packagesDelivered.append(p)
                        break
            package.print()

        elif inputStream == 'r':
            inputStream = input("enter index of truck '0', '1', or '2'")
            if inputStream == '0':
                print("=========Route for truck one===========")
                print(routeMiles1, "miles\n")
                for i in range(len(route1)):
                    print(route1[i][0].getTitle())
                print("\n")
            elif inputStream == '1':
                print("=========Route for truck two===========")
                print(routeMiles2, "miles\n")
                for i in range(len(route2)):
                    print(route2[i][0].getTitle())
                print("\n")
            elif inputStream == '2':
                print("========Route for truck three============")
                print(routeMiles3, "miles\n")
                for i in range(len(route3)):
                    print(route3[i][0].getTitle())
                print("\n")

            print("The total miles for all routes is", totalMiles)
            print("------------------------------------\n")

        elif inputStream == 'e':
            running = False
