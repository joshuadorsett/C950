from DataStructures.Graph import Graph
from Models.Truck import routeMiles
from Utils.truckLoader import truckLoader


def userInterface(running):
    print("--------------------------------------------\n"
          "|                   C950                   |\n"
          "|          WGUPS Console Interface         |\n"
          "|              Joshua Dorsett              |\n"
          "--------------------------------------------\n")

    while running:

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
        inputStream = input("enter 'p' to print all package information for a certain time.\n"
                            "enter 'l' to lookup a specific package by index for a certain time.\n"
                            "enter 'e' to end program.\n")

        if inputStream == 'p':
            currentTime = input(
                "enter a time to lookup in the format 'hh:mm' or leave blank and hit enter for end of day.\n"
                "please use 24 hour time.\n")
            if currentTime == '':
                currentTime = '24:00'
            for truck in trucks:
                truck.startRoute(currentTime, saltLakeCity)
                for package in truck.getPackages():
                    package.print()
            print("The total miles for all completed routes is", totalMiles,
                  "\n--------------------------------------------\n")

        if inputStream == 'l':

            currentTime = input(
                "enter a time to lookup in the format 'hh:mm' or leave blank and hit enter for end of day.\n"
                "please use 24 hour time.\n")
            if currentTime == '':
                currentTime = '24:00'
            searchType = input("enter 'i' to search by package ID.\n"
                               "enter 'a' to search by package address.\n"
                               "enter 'd' to search by deadline.\n"
                               "enter 'c' to search by city.\n"
                               "enter 'z' to search by zipcode.\n"
                               "enter 'w' to search by weight.\n"
                               "enter 's' tp search by delivery status.\n")
            compareKey = None
            if searchType == 'i':
                compareKey = input("enter package ID number (0-39).\n")
            elif searchType == 'a':
                compareKey = input("enter exact package street address.\n")
            elif searchType == 'd':
                compareKey = input("enter '1' for 9:00.\n"
                                   "enter '2' for 10:30.\n"
                                   "enter '3' for eod.\n")
                if compareKey == '1':
                    compareKey = '9:00 AM'
                elif compareKey == '2':
                    compareKey = '10:30 AM'
                elif compareKey == '3':
                    compareKey = 'EOD'
            elif searchType == 'c':
                compareKey = input("enter '1' for Salt Lake City.\n"
                                   "enter '2' for West Valley City.\n"
                                   "enter '3' for Millcreek.\n"
                                   "enter '4' for Holladay.\n"
                                   "enter '5' for Murray.\n")
                if compareKey == '1':
                    compareKey = 'Salt Lake City'
                elif compareKey == '2':
                    compareKey = 'West Valley City'
                elif compareKey == '3':
                    compareKey = 'Millcreek'
                elif compareKey == '4':
                    compareKey = 'Holladay'
                elif compareKey == '5':
                    compareKey = 'Murray'
            elif searchType == 'z':
                compareKey = input("enter 5 digit zipcode with no spaces.")
            elif searchType == 'w':
                compareKey = input("enter integer value of package weight.")
            elif searchType == 's':
                compareKey = input("enter 'd' for delivered and 'n' for not delivered.")
            else:
                continue
            for truck in trucks:
                truck.startRoute(currentTime, saltLakeCity)
                for package in truck.getPackages():
                    if searchType == 'i':
                        if package.getId() == int(compareKey):
                            package.print()
                    elif searchType == 'a':
                        if package.getAddress() == compareKey:
                            package.print()
                    elif searchType == 'd':
                        if package.getDeadline() == compareKey:
                            package.print()
                    elif searchType == 'c':
                        if package.getCity() == compareKey:
                            package.print()
                    elif searchType == 'z':
                        if package.getZipCode() == int(compareKey):
                            package.print()
                    elif searchType == 'w':
                        if package.getWeight() == int(compareKey):
                            package.print()
                    elif searchType == 's':
                        if compareKey == 'd':
                            if package.getDeliveryStatus() != 'not delivered':
                                package.print()
                        elif compareKey == 'n':
                            if package.getDeliveryStatus() == 'not delivered':
                                package.print()
            print("The total miles for all completed routes is", totalMiles,
                  "\n--------------------------------------------\n")

        elif inputStream == 'e':
            running = False
        else:
            continue
