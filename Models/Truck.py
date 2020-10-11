from Utils.timeHandler import *


# class defining truck object responsible for calculating routes, delivering packages, and keeping track of time
class Truck:
    # constructor initializes argument values and set values
    def __init__(self, truckId, timeLeftHub):
        self._truckId = truckId
        self._maxCargo = 16
        self._cargoSize = 0
        self._cargo = []
        self._route = []
        self._miles = 0.0
        self._timeLeftHub = timeLeftHub
        self._clock = timeLeftHub

    # getters
    def getId(self):
        return self._truckId

    def getTimeLeftHub(self):
        return self._timeLeftHub

    def getRoute(self):
        return self._route

    def getCargo(self):
        return self._cargo

    # adds a package object into trucks cargo list
    def addCargo(self, package):
        if self._cargoSize < self._maxCargo:
            self._cargo.append(package)
            self._cargoSize += 1
        else:
            print("cargo is full. :", self._truckId)

    # creates routes for each truck using a modified Dijkstra's shortest path algorithm
    def createRoute(self, graph, Hub):
        locations = graph.getLocations()

        # create a list of locations that need to be visited before 10:30
        priorityDestinations = []

        # create a list of locations that need to be visited by EOD
        eodDestinations = []

        # if deadline is not EOD add location to priorityDestinations and if it EOD add it to eodDestinations
        # O(N^2)
        for i in range(locations.getSize()):
            for j in range(len(self._cargo)):
                # set variable to current package in loop
                package = self._cargo[j]
                # set variable to curret packages deadline
                deadline = package.getDeadline()
                # if the deadline is not EOD
                if deadline != 'EOD':
                    # if current location and package in the loop have the same address
                    if locations.getValue(i).getAddress() == package.getAddress():
                        # append location to priority list
                        priorityDestinations.append(locations.getValue(i))
                # if deadline is EOD
                else:
                    # if current location and package in loop have the same address
                    if locations.getValue(i).getAddress() == package.getAddress():
                        # append location to eod list
                        eodDestinations.append(locations.getValue(i))
        # total distance from start point
        distanceFromStart = 0
        # list of locations and times to be there in order of selected route
        route = [[Hub, self._timeLeftHub]]
        # location the algorithm is currently calculating from
        currentLocation = Hub
        # bool used to remove repeated addresses in the route
        repeatAddress = False
        # shortest path algo loop for priority destinations only
        # this ensures that priority packages are delivered first
        # time - O(NLOGN) - every time it appends the route the queue pops the locations so the queue's size is log
        # while the priority list is not empty
        while len(priorityDestinations) > 0:
            # set closestLocation to the hub (this is an argument)
            closestLocation = Hub
            # initialize an integer variable for containing the index of locations
            closestLocationIndex = 0
            # initialize an integer variable to a large number to allow the loop to run the first time
            shortestDistance = 100
            # uses the shortest path algorithm to find next shortest distance in the queue
            # time - O(N)
            # loop through each location in priority list
            for i in range(len(priorityDestinations)):
                # set variable to index of current location
                u = currentLocation.getIndex()
                # set variable to index of first location in iteration from priority list
                v = priorityDestinations[i].getIndex()
                # calls the get distance method in the Graph class comparing current location and iteration in list
                distance = graph.getDistance(u, v)
                # if shortest distance so far is longer than the current distance calculation
                if shortestDistance > distance:
                    # set closest location to current iteration location
                    closestLocation = priorityDestinations[i]
                    # set closest location index to to the current iteration count
                    closestLocationIndex = i
                    # set the shortest distance to the current distance calculation
                    shortestDistance = distance
                    # increment total distance with the current distance calculation
                    distanceFromStart += distance
            # checks to see if this is a repeated address by looping through route
            # time - O(N)
            for loc in route:
                # if the current closest location is already in the route
                if priorityDestinations[closestLocationIndex].getIndex() == loc[0].getIndex():
                    # since the location has been visited it is popped from queue w/o being appended to route
                    repeatAddress = True
                    priorityDestinations.pop(closestLocationIndex)
                    # if location is found this breaks this current for loop to save time since value is found
                    break

            # if this is a unique address
            if not repeatAddress:
                # the location is popped from queue and added to route
                route.append(
                    [priorityDestinations.pop(closestLocationIndex), milesToTime(self._timeLeftHub, distanceFromStart)])
                currentLocation = closestLocation
            # repeat address variable is reset to false for the next iteration in the while loop
            repeatAddress = False

        # runs through the algorithm again for the second list of packages with an eod deadline
        # this ensures that priority packages are delivered first
        # if the eod package location has been visited in previous algorithm then it will not be repeated
        # O(NLOGN) - every time it appends the route the queue pops the locations so the queue's size is log
        while len(eodDestinations) > 0:
            # set closestLocation to the last location added to the route
            closestLocation = currentLocation
            # initialize an integer variable with index of last location added to route
            closestLocationIndex = currentLocation.getIndex()
            # initialize an integer variable to a large number to allow the loop to run the first time
            shortestDistance = 100
            # uses the shortest path algorithm to find next shortest distance in the queue
            # time - O(N)
            # loop through each location in eod list
            for i in range(len(eodDestinations)):
                # set variable to index of current location
                u = currentLocation.getIndex()
                # set variable to index of first location in iteration from eod list
                v = eodDestinations[i].getIndex()
                # calls the get distance method in the Graph class comparing current location and iteration in list
                distance = graph.getDistance(u, v)
                # if shortest distance so far is longer than the current distance calculation
                if shortestDistance > distance:
                    # set closest location to current iteration location
                    closestLocation = eodDestinations[i]
                    # set closest location index to to the current iteration count
                    closestLocationIndex = i
                    # set the shortest distance to the current distance calculation
                    shortestDistance = distance
                    # increment total distance with the current distance calculation
                    distanceFromStart += distance
            # checks to see if this is a repeated address by looping through route
            # time - O(N)
            for loc in route:
                # if the current closest location is already in the route
                if eodDestinations[closestLocationIndex].getIndex() == loc[0].getIndex():
                    # since the location has been visited it is popped from queue w/o being appended to route
                    repeatAddress = True
                    eodDestinations.pop(closestLocationIndex)
                    # if location is found this breaks this current for loop to save time since value is found
                    break
            # if this is a unique address
            if not repeatAddress:
                # the location is popped from queue and added to route
                route.append(
                    [eodDestinations.pop(closestLocationIndex), milesToTime(self._timeLeftHub, distanceFromStart)])
                currentLocation = closestLocation
            # repeat address variable is reset to false for the next iteration in the while loop
            repeatAddress = False
        # sets the functions route list to this truck object's 'self._route' list
        self._route = route

    # this method virtually delivers packages in trucks route up to given time
    def startRoute(self, currentTime, graph):
        # set the starting time to total minutes from midnight
        startTimeMinutes = timestampToMinutes(self._timeLeftHub)
        # convert current time to minutes from midnight
        # then subtract startTimeMinutes to find total minutes from time left hub
        currentTimeMinutes = timestampToMinutes(currentTime) - startTimeMinutes
        # this block of code corrects package number 8 to correct address at 10:20
        # loops through this trucks cargo
        for p in self._cargo:
            # sets variable to current package iteration's ID
            packageId = p.getId()
            # if current time is earlier than 10:20
            if currentTimeMinutes < 620 and packageId == 8:
                # set package to invalid because the new address si not given until 10:20
                p.setValidity(False)
            # if current time is later than 10:20
            elif currentTimeMinutes > 620 and packageId == 8:
                # gets last location in route list's sublist ( the route sublist is [ location, deliveryTime ] )
                routesLastLocationList = self.getRoute()[len(self.getRoute()) - 1]
                # sets corrected address information
                p._address = '410 S State St'
                p._zipCode = '84111'
                city = 'Salt Lake City'
                p._city = city
                # sets validity to true
                p.setValidity(True)
                # appends new address to end of route using append route method
                self.appendRoute(graph, routesLastLocationList, p)

        # loop through truck route
        # time - O(N^2)
        for i in range(len(self._route)):
            # sets variable to current iterations route sublist location object
            deliveryLocation = self._route[i][0]
            # set variable to current iterations route sublist time string
            deliveryTime = self._route[i][1]
            # converts timestamp into minutes accumulated from start time
            deliveryTimeMinutes = timestampToMinutes(deliveryTime) - startTimeMinutes
            # if current time is later than delivery time
            if currentTimeMinutes > deliveryTimeMinutes:
                # loop through cargo
                for p in self._cargo:
                    # if packages address equals location address and if package has a valid address
                    if p.getAddress() == deliveryLocation.getAddress() and p.getValidity():
                        # set delivery status to delivered with delivery time and location title
                        p.setDeliveryStatus("delivered to " + deliveryLocation.getTitle()
                                            + " at " + deliveryTime)

    # this method appends the route if a new location is needed like with package 8
    def appendRoute(self, graph, lastLocationSubList, package):
        # set variable locations hash table in graph
        locations = graph.getLocations()
        # setting variable to location from the route sublist [ location, deliveryTime ]
        lastLocation = lastLocationSubList[0]
        # setting variable to time from the route sublist [ location, deliveryTime ]
        lastDeliveryTime = lastLocationSubList[1]
        # loop through locations
        for l in range(locations.getSize()):
            # set variable to current iteration's location
            location = locations.getValue(l)
            # if package and location have same address
            if package.getAddress() == location.getAddress():
                # set variable to last locations index
                u = lastLocation.getIndex()
                # set variable to iteration's location index
                v = location.getIndex()
                # set variable to the distance between u and v using getDistance method in graph
                distanceFromLastLocation = graph.getDistance(u, v)
                # set variable to time of delivery using the milesToTime method converting distance to time
                deliveryTime = milesToTime(lastDeliveryTime, distanceFromLastLocation)
                # append new route sublist [ location, delivery time ] to this trucks route
                self._route.append([location, deliveryTime])


# static function used to return the 'cost' of a route
# time - O(N)
def routeCost(route, graph):
    # initializes a location variable to None
    previousDestination = None
    # initializes a cost variable to 0
    cost = 0.0
    # loops through each sublist '[ location, deliveryTime ]' in route
    for subList in route:
        # if this is the first iteration
        if previousDestination is None:
            # sets previousDestination variable to current route sublist
            previousDestination = subList
            # jumps to next iteration since there is no previous destination
            continue
        # increments cost using the get distance method in graph
        cost = cost + graph.getDistance(previousDestination[0].getIndex(), subList[0].getIndex())
        # sets previousDestination variable to current route sublist
        previousDestination = subList
    # returns total cost of route
    return cost
