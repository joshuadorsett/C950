from DataStructures.Graph import Graph
from Models.Truck import routeMiles
from Utils.truckLoader import truckLoader

# defines the user interface function
def userInterface(running):
    # prints project information as the heading to the console interface
    print("          ---------------------------------------- \n"
          "         |                 C950                   |\n"
          "         |   Data Structures and Algorithms II    |\n"
          "         |         WGUPS ROUTING PROGRAM          |\n"
          "         |             Joshua Dorsett             |\n"
          "         |          Student ID: jdors43           |\n"
          "          ---------------------------------------- \n")
    # starts a while loop with a bool value names 'running' set to true in the argument
    while running:

        # builds a map of locations using the graph data structure in DataStructures.Graph.py
        # time - O(N^2)
        deliveryMap = Graph()

        # sets the starting point of the graph to the Hub inside of the graph's vertices Hash table
        # time - O(N)
        Hub = deliveryMap.getLocations().getValue(0)

        # loads trucks in Utils.truckLoader.py and returns a list of 3 trucks
        # time - O(N)
        trucks = truckLoader()

        # creates routes for each truck using a modified Dijkstra's shortest path algorithm
        # time- O(N)
        trucks[0].createRoute(deliveryMap, Hub)
        trucks[1].createRoute(deliveryMap, Hub)
        trucks[2].createRoute(deliveryMap, Hub)

        # calculates route cost from each truck
        routeMiles1 = routeMiles(trucks[0].getRoute(), deliveryMap)
        routeMiles2 = routeMiles(trucks[1].getRoute(), deliveryMap)
        routeMiles3 = routeMiles(trucks[2].getRoute(), deliveryMap)

        # calculates a total cost for all trucks
        totalMiles = routeMiles1 + routeMiles2 + routeMiles3

        # asks user how they want to proceed into program with the following choices
        inputStream = input("enter 'p' to print all package information for a certain time.\n"
                            "enter 'l' to lookup a specific package by index for a certain time.\n"
                            "enter 'e' to end program.\n")

        # if user chose to print all package info, this branch is selected
        if inputStream == 'p':

            # asks user to enter the time fo day they want the delivery status for
            currentTime = input(
                "enter a time to lookup in the format 'hh:mm' or leave blank and hit enter for end of day.\n"
                "please use 24 hour time.\n")

            # if user left the choice blank to see end of day status, this branch is selected
            if currentTime == '':

                # the current time is set to midnight
                currentTime = '24:00'
            # if previous input function was not left blank, currentTime is the value the user entered


            for truck in trucks:
                truck.startRoute(currentTime, deliveryMap)
                for package in truck.getPackages():
                    package.print()
            print("    The total miles for all completed routes is", totalMiles,
                  "\n\n")
        # if user chose to find a  specific package, this branch is selected
        if inputStream == 'l':
            # asks user to enter the time fo day they want the delivery status for
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
                compareKey = input("enter 5 digit zipcode with no spaces.\n")
            elif searchType == 'w':
                compareKey = input("enter integer value of package weight.\n")
            elif searchType == 's':
                compareKey = input("enter 'd' for delivered and 'n' for not delivered.\n")
            else:
                continue
            for truck in trucks:
                truck.startRoute(currentTime, deliveryMap)
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
            print("    The total miles for all completed routes is", totalMiles,
                  "\n\n")

        elif inputStream == 'e':
            running = False
        else:
            continue
