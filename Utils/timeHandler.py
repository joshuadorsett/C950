# a group of static functions related to time


# converts 24 hour hh:mm to total minutes accumulated from midnight
# returns an int
def timestampToMinutes(time24):
    # creates string list and splits up given time into two strings
    timeString = str(time24).split(':')
    # calculates the total minutes from from the hours integer
    hourToMinutes = int(timeString[0]) * 60
    # calculates the total minutes from from the minutes integer
    minutes = int(timeString[1])
    # returns total minutes
    return hourToMinutes + minutes


# converts total minutes accumulated from midnight to 24 hour hh:mm
# returns a string
def minutesToTimestamp(minutesFromMidnight):
    # finds the number of hours have accumulated from midnight and rounds down with int conversion
    hour = str(int(minutesFromMidnight / 60))
    # finds the number of minutes that have accumulated since the start of hour and rounds down with int conversion
    minute = int(minutesFromMidnight % 60)
    # adds a '0' value before number if minute is less than 10 to get two minute digits for hh:mm
    # converts int minute to string
    if minute < 10:
        minute = '0' + str(minute)
    else:
        minute = str(minute)
    # returns string value in 2 hour time format hh:mm
    return hour + ":" + minute


# this returns the 24 hour time after a certain distance of miles at 18 mph (0.3 miles per min)
def milesToTime(startTime, distanceFromStart):
    # converts start time to minutes accumulated from midnight
    totalStartingMinutes = timestampToMinutes(startTime)
    # converts miles to total minutes since start time
    minutesFromStart = distanceFromStart / 0.3
    # adds time since start and start since midnight
    minutesFromMidnight = totalStartingMinutes + minutesFromStart
    # returns the converted current time in minutes from midnight to 24 hour time hh:mm
    return minutesToTimestamp(minutesFromMidnight)
