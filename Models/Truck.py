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
        amDestinations = []
        # create a list of locations that need to be visited by EOD
        eodDestinations = []
        # if deadline is not EOD add location to amDestinations and if it EOD add it to eodDestinations
        for i in range(locations.getSize()):
            for j in range(len(self._packages)):
                repeat = False
                package = self._packages[j]
                deadline = package.getDeadline()
                # this code changes the address for package 8
                for l in amDestinations:
                    if package.getAddress() == l.getAddress():
                        repeat = True
                for l in eodDestinations:
                    if package.getAddress() == l.getAddress():
                        repeat = True
                if not repeat:
                    if deadline != 'EOD' or package.getId() == 25:
                        if locations.getValue(i).getAddress() == package.getAddress():
                            amDestinations.append(locations.getValue(i))
                    else:
                        if locations.getValue(i).getAddress() == package.getAddress():
                            eodDestinations.append(locations.getValue(i))

        # total distance from start point
        distanceFromStart = 0
        # list of locations and times to be there in order of selected route
        route = [[Hub, self._timeLeftHub]]
        # location the algorithm is currently calculating from
        currentLocation = Hub

        # greedy algo for morning destinations
        while len(amDestinations) > 0:
            closestLocation = Hub
            closestLocationIndex = 0
            shortestDistance = 100
            for i in range(len(amDestinations)):
                u = currentLocation.getIndex()
                v = amDestinations[i].getIndex()
                distance = graph.getDistance(u, v)
                if shortestDistance > distance:
                    closestLocation = amDestinations[i]
                    closestLocationIndex = i
                    shortestDistance = distance
                    distanceFromStart += distance
            route.append([amDestinations.pop(closestLocationIndex), milesToTime(self._timeLeftHub, distanceFromStart)])
            currentLocation = closestLocation

        # greedy algo for eod destinations
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
            route.append([eodDestinations.pop(closestLocationIndex), milesToTime(self._timeLeftHub, distanceFromStart)])
            currentLocation = closestLocation

        self._route = route
        return route
