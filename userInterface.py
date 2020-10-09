from DataStructures.Graph import Graph
from Models.Truck import routeMiles
from Utils.dataHandler import *
from Utils.timeHandler import timestampToMinutes
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
    trucks[0].createRoute(saltLakeCity, locations.getValue(0), locations)
    trucks[1].createRoute(saltLakeCity, locations.getValue(0), locations)
    trucks[2].createRoute(saltLakeCity, locations.getValue(0), locations)

    while running:

        inputStream = input("enter 'p' to print all package information for a certain time.\n"
                            "enter 'r' to lookup routes.\n"
                            "enter 'e' to end program.\n")

        if inputStream == 'r':
            inputStream = input("enter index of truck '0', '1', or '2'")
            routeMiles1 = routeMiles(trucks[0].getRoute(), saltLakeCity)
            routeMiles2 = routeMiles(trucks[1].getRoute(), saltLakeCity)
            routeMiles3 = routeMiles(trucks[2].getRoute(), saltLakeCity)
            totalMiles = routeMiles1 + routeMiles2 + routeMiles3
            if inputStream == '0':
                route = trucks[0].getRoute()
                print("=========Route for truck one===========")
                for i in range(len(route)):
                    print(route[i][0].getAddress())
                print("\n")
                print(routeMiles(route, saltLakeCity), "total miles in this route.\n")
            elif inputStream == '1':
                route = trucks[1].getRoute()
                print("=========Route for truck two===========")
                for i in range(len(route)):
                    print(route[i][0].getAddress())
                print("\n")
                print(routeMiles(route, saltLakeCity), "total miles in this route.\n")
            elif inputStream == '2':
                route = trucks[2].getRoute()
                print("========Route for truck three============")
                for i in range(len(route)):
                    print(route[i][0].getAddress())
                print("\n")
                print(routeMiles(route, saltLakeCity), "total miles in this route.\n")
            print("The total miles for all routes is", totalMiles)
            print("------------------------------------\n")

        elif inputStream == 'p':
            currentTime = input("enter a time to lookup in the format 'hh:mm'."
                                "\nplease use 24 hour time.\n")
            for truck in trucks:
                truck.startRoute(currentTime, saltLakeCity, locations)
                for p in truck.getPackages():
                    p.print()
            running = False
        elif inputStream == 'e':
            running = False
