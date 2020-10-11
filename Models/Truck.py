from Utils.timeHandler import *


def routeMiles(route, graph):
    previousDestination = None
    miles = 0.0
    for destination in route:
        if previousDestination is None:
            previousDestination = destination
            continue
        miles = round(miles + graph.getDistance(previousDestination[0].getIndex(), destination[0].getIndex()))
        previousDestination = destination
    return miles


class Truck:
    def __init__(self, truckId, timeLeftHub):
        self._truckId = truckId
        self._maxCargo = 16
        self._cargoSize = 0
        self._packages = []
        self._route = []
        self._miles = 0.0
        self._timeLeftHub = timeLeftHub
        self._clock = timeLeftHub

    def getId(self):
        return self._truckId

    def getTimeLeftHub(self):
        return self._timeLeftHub

    def getRoute(self):
        return self._route

    def getPackages(self):
        return self._packages

    def addCargo(self, package):
        if self._cargoSize < self._maxCargo:
            self._packages.append(package)
            self._cargoSize += 1
        else:
            print("cargo is full. :", self._truckId)

    def startRoute(self, currentTime, graph):

        # set the starting time to total minutes from midnight
        startTimeMinutes = timestampToMinutes(self._timeLeftHub)
        # convert current time to minutes from midnight
        # then subtract startTimeMinutes to find total minutes from time left hub
        currentTimeMinutes = timestampToMinutes(currentTime) - startTimeMinutes
        # set delivery status and correct package number 8 to correct address at 10:20
        for p in self._packages:
            packageId = p.getId()
            if currentTimeMinutes < 620 and packageId == 8:
                p.setValidity(False)
            elif currentTimeMinutes > 620 and packageId == 8:
                routesLastLocationList = self.getRoute()[len(self.getRoute()) - 1]
                address = '410 S State St'
                p._address = address
                p._zipCode = 84111
                city = 'Salt Lake City'
                p._city = city
                p.setValidity(True)
                self.appendRoute(graph, routesLastLocationList, p)

        # loop through truck route and set condition to advance only for locations before current time
        for i in range(len(self._route)):
            deliveryLocation = self._route[i][0]
            deliveryTime = self._route[i][1]
            deliveryTimeMinutes = timestampToMinutes(deliveryTime) - startTimeMinutes
            if currentTimeMinutes > deliveryTimeMinutes:
                for p in self._packages:
                    if p.getAddress() == deliveryLocation.getAddress() and p.valid():
                        p.setDeliveryStatus("delivered to " +
                                            deliveryLocation.getTitle() +
                                            " at " + deliveryTime)

    def appendRoute(self, graph, lastLocationList, package):
        # total distance from lastLocation
        locations = graph.getLocations()
        lastLocation = lastLocationList[0]
        lastDeliveryTime = lastLocationList[1]
        for l in range(locations.getSize()):
            if package.getAddress() == locations.getValue(l).getAddress():
                location = locations.getValue(l)
                u = lastLocationList[0].getIndex()
                v = location.getIndex()
                distanceFromLastLocation = graph.getDistance(u, v)
                deliveryTime = milesToTime(lastDeliveryTime, distanceFromLastLocation)
                self._route.append([location, deliveryTime])

    # greedy algo customized to to route eraly morning deadlines first
    def createRoute(self, graph, Hub):
        locations = graph.getLocations()

        # create a list of locations that need to be visited before 10:30
        priorityDestinations = []

        # create a list of locations that need to be visited by EOD
        eodDestinations = []

        # if deadline is not EOD add location to priorityDestinations and if it EOD add it to eodDestinations
        # O(N^2)
        for i in range(locations.getSize()):
            for j in range(len(self._packages)):
                package = self._packages[j]
                deadline = package.getDeadline()
                if deadline != 'EOD':
                    if locations.getValue(i).getAddress() == package.getAddress():
                        priorityDestinations.append(locations.getValue(i))
                else:
                    if locations.getValue(i).getAddress() == package.getAddress():
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
        # O(NLOGN) - every time it appends the route the queue pops the locations so the queue's size is log
        while len(priorityDestinations) > 0:
            closestLocation = Hub
            closestLocationIndex = 0
            shortestDistance = 100

            # uses the shortest path algorithm to find next shortest distance in the queue
            # O(N)
            for i in range(len(priorityDestinations)):
                u = currentLocation.getIndex()
                v = priorityDestinations[i].getIndex()
                # calls the get distance method in the Graph class

                distance = graph.getDistance(u, v)
                if shortestDistance > distance:
                    closestLocation = priorityDestinations[i]
                    closestLocationIndex = i
                    shortestDistance = distance
                    distanceFromStart += distance

            # checks to see if this is a repeated address by looping through route
            # O(N)
            for loc in route:
                if priorityDestinations[closestLocationIndex].getIndex() == loc[0].getIndex():
                    # since the location has been visited it is popped from queue w/o being appended to route
                    repeatAddress = True
                    priorityDestinations.pop(closestLocationIndex)
                    break

            # if this is a unique address the location is popped from queue and added to route
            if not repeatAddress:
                route.append(
                    [priorityDestinations.pop(closestLocationIndex), milesToTime(self._timeLeftHub, distanceFromStart)])
                currentLocation = closestLocation
            repeatAddress = False

        # runs through the algorithm again for the second list of packages with an eod deadline
        # this ensures that priority packages are delivered first
        # if the eod package location has been visited in previous algorithm then it will not be repeated
        # O(NLOGN) - every time it appends the route the queue pops the locations so the queue's size is log
        while len(eodDestinations) > 0:
            closestLocation = currentLocation
            closestLocationIndex = currentLocation.getIndex()
            shortestDistance = 100
            for i in range(len(eodDestinations)):
                u = currentLocation.getIndex()
                v = eodDestinations[i].getIndex()
                distance = graph.getDistance(u, v)
                if shortestDistance > distance:
                    closestLocation = eodDestinations[i]
                    closestLocationIndex = i
                    shortestDistance = distance
                    distanceFromStart += distance
            for loc in route:
                if eodDestinations[closestLocationIndex].getIndex() == loc[0].getIndex():
                    repeatAddress = True
                    eodDestinations.pop(closestLocationIndex)
                    break
            if not repeatAddress:
                route.append(
                    [eodDestinations.pop(closestLocationIndex), milesToTime(self._timeLeftHub, distanceFromStart)])
                currentLocation = closestLocation
            repeatAddress = False

        self._route = route
        return route
