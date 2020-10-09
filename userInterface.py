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
    # build a graph of locations
    saltLakeCity = Graph(locations, distances)
    # load trucks and return list of trucks
    trucks = truckLoader(packages)
    # create routes and calculate cost of each route
    route1 = trucks[0].createRoute(saltLakeCity, locations.getValue(0), locations)
    routeMiles1 = routeMiles(route1, saltLakeCity)
    route2 = trucks[1].createRoute(saltLakeCity, locations.getValue(0), locations)
    routeMiles2 = routeMiles(route2, saltLakeCity)
    route3 = trucks[2].createRoute(saltLakeCity, locations.getValue(0), locations)
    routeMiles3 = routeMiles(route3, saltLakeCity)
    totalMiles = routeMiles1 + routeMiles2 + routeMiles3

    while running:

        inputStream = input("enter 'p' to print all package information for a certain time.\n"
                            "enter 'r' to lookup routes.\n"
                            "enter 'e' to end program.\n")

        if inputStream == 'r':
            inputStream = input("enter index of truck '0', '1', or '2'")
            if inputStream == '0':
                print("=========Route for truck one===========")
                for i in range(len(route1)):
                    print(route1[i][0].getAddress())
                print("\n")
                print(routeMiles1, "total miles in this route.\n")
            elif inputStream == '1':
                print("=========Route for truck two===========")
                for i in range(len(route2)):
                    print(route2[i][0].getAddress())
                print("\n")
                print(routeMiles2, "total miles in this route.\n")
            elif inputStream == '2':
                print("========Route for truck three============")
                for i in range(len(route3)):
                    print(route3[i][0].getAddress())
                print("\n")
                print(routeMiles3, "total miles in this route.\n")
            print("The total miles for all routes is", totalMiles)
            print("------------------------------------\n")

        elif inputStream == 'p':
            currentTime = input("enter a time to lookup in the format 'hh:mm'."
                                "\nplease use 24 hour time.\n")
            inputStream = input("enter 'a' for all packages.\n"
                                "enter 'i' for a specific package")
            if inputStream == 'a':
                for truck in trucks:
                    truck.startRoute(currentTime)
                    for p in truck.getPackages():
                        p.print()
            elif inputStream == 'i':
                index = input("enter integer from 0-39 of package index")
                for truck in trucks:
                    for p in truck.getPackages():
                        if p.getId == int(index):
                            p.print()

        elif inputStream == 'e':
            running = False
