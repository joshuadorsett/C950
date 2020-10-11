

# converts 24 hour hh:mm to total minutes from midnight
# returns an int
def timestampToMinutes(time24):
    timeString = str(time24).split(':')
    hourToMinutes = int(timeString[0]) * 60
    minutes = int(timeString[1])
    return hourToMinutes + minutes


# converts total minutes from midnight to 24 hour hh:mm
# returns a string
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
def milesToTime(startTime, distanceFromStart):
    totalStartingMinutes = timestampToMinutes(startTime)
    minutesFromStart = distanceFromStart / 0.3
    minutesFromMidnight = totalStartingMinutes + minutesFromStart
    return minutesToTimestamp(minutesFromMidnight)
