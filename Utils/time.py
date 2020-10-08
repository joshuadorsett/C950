# converts 24 hour hh:mm to total minutes from midnight
def timestampToMinutes(time24):
    timeString = str(time24).split(':')
    hourToMinutes = int(timeString[0]) * 60
    minutes = int(timeString[1])
    return hourToMinutes + minutes


# converts total minutes from midnight to 24 hour hh:mm
def minutesToTimestamp(minutesFromMidnight):
    # finds the number of hours have passed from midnight and rounds down
    hour = str(int(minutesFromMidnight / 60))
    # finds the number of minutes that have passed since the start of hour
    minute = int(minutesFromMidnight % 60)
    if minute < 10:
        minute = '0' + str(minute)
    else:
        minute = str(minute)
    return hour + ":" + minute


# this returns the time after a certain amount of miles
def time(startTime, distanceFromStart):
    totalStartingMinutes = timestampToMinutes(startTime)
    minutesFromStart = distanceFromStart / 0.3
    minutesFromMidnight = totalStartingMinutes + minutesFromStart
    return minutesToTimestamp(minutesFromMidnight)


def getRouteListVisited(startTime, currentTime, route):
    # convert hour to 60 minutes and add total starting minutes from midnight
    totalStartingMinutes = timestampToMinutes(startTime)
    # convert hour to 60 minutes and add total current minutes from midnight
    totalCurrentMinutes = timestampToMinutes(currentTime)
    # subtract starting minutes from current minutes
    minutesSinceStart = totalCurrentMinutes - totalStartingMinutes
    # calculate the amount of miles driven at this point
    currentCost = minutesSinceStart * (18 / 60)
    # calculate current location based on miles driven and the route list of location objects
    miles = 0
    currentLocation = route[0]
    locationsVisited = []
    for nextLocation in route:
        if miles < currentCost:
            miles += currentLocation[0].getDistance(nextLocation)
            currentLocation = nextLocation
            locationsVisited.append(nextLocation)
        elif miles == currentCost:
            print("truck is currently at ", currentLocation.getTitle(),
                  "\nmiles this truck has driven: ", currentCost)
            return locationsVisited
        else:
            print("truck is currently on the way to ", currentLocation[0].getTitle(),
                  "\nmiles this truck has driven: ", currentCost)
            return locationsVisited
