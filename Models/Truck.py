def routeMiles(route, graph):
    finalDestination = None
    miles = 0.0
    for destination in route:
        if finalDestination is None:
            finalDestination = destination
            continue
        miles = round(miles + graph.getDistance(finalDestination.getIndex(), destination.getIndex()))
        finalDestination = destination
    return miles


class Truck:
    def __init__(self, truckId):
        self._truckId = truckId
        self._maxCargo = 16
        self._speed = 18
        self._cargoSize = 0
        self._packages = []
        self._route = []
        self._miles = 0.0
        self._time = None

    def addCargo(self, package):
        if self._cargoSize < self._maxCargo:
            self._packages.append(package)
            self._cargoSize += 1
        else:
            print("cargo is full. :", self._truckId)

    # greedy algo
    def createRoute(self, graph, Hub, locations):
        destinations = []
        for i in range(locations.getSize()):
            for j in range(len(self._packages)):
                if locations.getValue(i).getAddress() == self._packages[j]._address:
                    destinations.append(locations.getValue(i))
        route = [Hub]
        currentLocation = Hub
        while len(destinations) > 0:
            closestLocation = Hub
            closestLocationIndex = 0
            shortestDistance = 100
            for i in range(len(destinations)):
                u = currentLocation.getIndex()
                v = destinations[i].getIndex()
                distance = graph.getDistance(u, v)
                if shortestDistance > distance:
                    closestLocation = destinations[i]
                    closestLocationIndex = i
                    shortestDistance = distance
            route.append(destinations.pop(closestLocationIndex))
            currentLocation = closestLocation
        route.append(Hub)
        self._route = route
        return route



