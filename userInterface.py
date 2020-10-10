from DataStructures.Graph import Graph
from Models.Truck import routeMiles
from Utils.truckLoader import truckLoader


def userInterface(running):
    print("------------------------------------")
    print("C950")
    print("WGUPS Project")
    print("Joshua Dorsett")
    print("------------------------------------\n")

    # build a graph of locations
    saltLakeCity = Graph()
    Hub = saltLakeCity.getLocations().getValue(0)
    # load trucks and return list of trucks
    trucks = truckLoader()
    # create routes and calculate cost of each route
    trucks[0].createRoute(saltLakeCity, Hub)
    trucks[1].createRoute(saltLakeCity, Hub)
    trucks[2].createRoute(saltLakeCity, Hub)
    # get routes from trucks and calculate total miles
    routeMiles1 = routeMiles(trucks[0].getRoute(), saltLakeCity)
    routeMiles2 = routeMiles(trucks[1].getRoute(), saltLakeCity)
    routeMiles3 = routeMiles(trucks[2].getRoute(), saltLakeCity)
    totalMiles = routeMiles1 + routeMiles2 + routeMiles3

    while running:
        inputStream = input("enter 'p' to print all package information for a certain time.\n"
                            "enter 'l' to lookup a specific package by index for a certain time.\n"
                            "enter 'e' to end program.\n")

        if inputStream == 'p':
            currentTime = input("enter a time to lookup in the format 'hh:mm' or enter 'eod' for end of day."
                                "\nplease use 24 hour time.\n")

            if currentTime != 'eod':
                for truck in trucks:
                    truck.startRoute(currentTime, saltLakeCity)
                    for p in truck.getPackages():
                        p.print()
            elif currentTime == 'eod':
                for truck in trucks:
                    truck.startRoute('24:00', saltLakeCity)
                    for p in truck.getPackages():
                        p.print()

            if inputStream == 'l':

                currentTime = input("enter a time to lookup in the format 'hh:mm' or enter 'eod' for end of day."
                                    "\nplease use 24 hour time.\n")
                searchType = input("enter 'id' to search by package ID.\n"
                                   "enter 'address' to search by package address.\n"
                                   "enter 'deadline' to search by deadline.\n"
                                   "enter 'city' to search by city.\n"
                                   "enter 'zip' to search by zipcode.\n"
                                   "enter 'weight' to search by weight.\n"
                                   "enter 'status' tp search by delivery status.\n")

                if currentTime != 'eod':
                    for truck in trucks:
                        truck.startRoute(currentTime, saltLakeCity)
                        for p in truck.getPackages():
                            p.print()
                elif currentTime == 'eod':
                    for truck in trucks:
                        truck.startRoute('24:00', saltLakeCity)
                        for p in truck.getPackages():
                            p.print()

            print("The total miles for all completed routes is", totalMiles)
            print("------------------------------------\n")
            running = False

        elif inputStream == 'e':
            running = False
