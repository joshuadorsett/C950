from DataStructures.Graph import Graph
from Models.Truck import routeCost
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
        route1Cost = routeCost(trucks[0].getRoute(), deliveryMap)
        route2Cost = routeCost(trucks[1].getRoute(), deliveryMap)
        route3Cost = routeCost(trucks[2].getRoute(), deliveryMap)
        # calculates a total cost for all trucks and rounds up to integer value
        totalCostOfRoutes = int(route1Cost + route2Cost + route3Cost) + 1
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
            # loops through list of 3 trucks
            for truck in trucks:
                # start route for current truck with user inputted time
                truck.startRoute(currentTime, deliveryMap)
                # loop through truck's cargo
                for package in truck.getCargo():
                    # use print method to print out current package information
                    package.print()
            # print total cost for all routes
            print("    The total mileage for all completed routes is", totalCostOfRoutes, "\n"
                  "    All deadlines met.\n\n")
        # if user chose to find a  specific package, this branch is selected
        if inputStream == 'l':
            # asks user to enter the time fo day they want the delivery status for
            currentTime = input(
                "enter a time to lookup in the format 'hh:mm' or leave blank and hit enter for end of day.\n"
                "please use 24 hour time.\n")
            # if eod
            if currentTime == '':
                # set current time to midnight
                currentTime = '24:00'
            # asks user how they want to search for a package
            searchType = input("enter 'i' to search by package ID.\n"
                               "enter 'a' to search by package address.\n"
                               "enter 'd' to search by deadline.\n"
                               "enter 'c' to search by city.\n"
                               "enter 'z' to search by zipcode.\n"
                               "enter 'w' to search by weight.\n"
                               "enter 's' tp search by delivery status.\n")
            # if user chose index
            if searchType == 'i':
                # ask user to enter index
                compareKey = input("enter package ID number (0-39).\n")
            # if user chose address
            elif searchType == 'a':
                #  ask user to enter address
                compareKey = input("enter exact package street address.\n")
            # if user chose deadline
            elif searchType == 'd':
                # ask user to enter deadline
                compareKey = input("enter '1' for 9:00.\n"
                                   "enter '2' for 10:30.\n"
                                   "enter '3' for eod.\n")
                # if user chose 1
                if compareKey == '1':
                    # set key to 9 am
                    compareKey = '9:00 AM'
                # if user chose 2
                elif compareKey == '2':
                    # set key to 10:30 am
                    compareKey = '10:30 AM'
                # if user chose 3
                elif compareKey == '3':
                    # set ket to eod
                    compareKey = 'EOD'
            # if user chose city
            elif searchType == 'c':
                # ask user to enter a city to search for
                compareKey = input("enter '1' for Salt Lake City.\n"
                                   "enter '2' for West Valley City.\n"
                                   "enter '3' for Millcreek.\n"
                                   "enter '4' for Holladay.\n"
                                   "enter '5' for Murray.\n")
                # if user chose 1
                if compareKey == '1':
                    # set ket to city
                    compareKey = 'Salt Lake City'
                # if user chose 2
                elif compareKey == '2':
                    # set key to city
                    compareKey = 'West Valley City'
                # if user chose 3
                elif compareKey == '3':
                    # set key to city
                    compareKey = 'Millcreek'
                # if user chose 4
                elif compareKey == '4':
                    # set key to city
                    compareKey = 'Holladay'
                # if user chose 5
                elif compareKey == '5':
                    # set ket to city
                    compareKey = 'Murray'
            # if user chose zip code
            elif searchType == 'z':
                # ask user to enter zip code
                compareKey = input("enter 5 digit zipcode with no spaces.\n")
            # if user chose weight
            elif searchType == 'w':
                # ask user to enter weight
                compareKey = input("enter integer value of package weight.\n")
            # if user chose status
            elif searchType == 's':
                # ask user to enter a status to search for
                compareKey = input("enter 'd' for delivered and 'n' for not delivered.\n")
            # if user entered something else continue loop
            else:
                continue
            # loop through 3 trucks
            for truck in trucks:
                # start the current trucks route
                truck.startRoute(currentTime, deliveryMap)
                # loop through trucks cargo
                for package in truck.getCargo():
                    # if searching with index
                    if searchType == 'i':
                        # if current package's ID equals the user desired ID
                        if package.getId() == int(compareKey):
                            # print package
                            package.print()
                    # if searching with address
                    elif searchType == 'a':
                        # if current package's address equals user desired address
                        if package.getAddress() == compareKey:
                            # print package
                            package.print()
                    # if searching with deadline
                    elif searchType == 'd':
                        # if current package deadline equals user desired deadline
                        if package.getDeadline() == compareKey:
                            # print package
                            package.print()
                    # if searching with city
                    elif searchType == 'c':
                        # if current package city equals user desired city
                        if package.getCity() == compareKey:
                            # print package
                            package.print()
                    # if searching with zip
                    elif searchType == 'z':
                        # if current package zip equals user desired zip
                        if package.getZipCode() == compareKey:
                            # print package
                            package.print()
                    # if searching with weight
                    elif searchType == 'w':
                        # if current package weight equals user desired weight
                        if package.getWeight() == compareKey:
                            # print package
                            package.print()
                    # if searching with status
                    elif searchType == 's':
                        # if user chose delivered
                        if compareKey == 'd':
                            # is current package status equals NOT not delivered
                            if package.getDeliveryStatus() != 'not delivered':
                                # print package
                                package.print()
                        # if user chose not delivered
                        elif compareKey == 'n':
                            # if current package equals not delivered
                            if package.getDeliveryStatus() == 'not delivered':
                                # print package
                                package.print()
            # print total cost of all routes
            print("    The total mileage for all completed routes is", totalCostOfRoutes, "\n"
                  "    All deadlines met.\n\n")
        # if user chose to end program
        elif inputStream == 'e':
            # set running to false which will end while loop
            running = False
        # if user entered something else than requested input, continue while loop
        else:
            continue
