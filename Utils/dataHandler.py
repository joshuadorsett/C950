from DataStructures.HashTable import *
from Models.Location import *
from Models.Package import *


# returns a hash table of package objects
# time - O(N)
def makeHashTableOfPackages():
    packageLists = readPackages()
    packages = HashTable(len(packageLists))
    for i in range(len(packageLists)):
        packageLists[i][0] = int(packageLists[i][0])
        packageLists[i][4] = int(packageLists[i][4])
        packageLists[i][6] = int(packageLists[i][6])
        current = packageLists[i]
        p = Package(current[0], current[1], current[2], current[4], current[5], current[6], current[7])
        packages.insert(current[0], p)
    return packages


# returns a hash table of location objects
# time - O(N)
def makeHashTableOfLocations():
    locationLists = readLocations()
    locations = HashTable(len(locationLists))
    for i in range(len(locationLists)):
        locationLists[i][0] = int(locationLists[i][0])
        locationLists[i][3] = int(locationLists[i][3])
        current = locationLists[i]
        l = Location(current[0], current[1], current[2], current[3])
        locations.insert(l.getIndex(), l)
    return locations


# returns a hash table with the key being LocationA and the key is a list of distances to any LocationB
# by using the getIndex method in the Location class we can access any distance once this list is created
# time - O(N)
def makeHashTableOfDistances():
    distanceLists = readDistances()
    distances = HashTable(len(distanceLists))
    for i in range(len(distanceLists)):
        ListOfDistancesFromLocationA = distanceLists[i]
        distances.insert(i, ListOfDistancesFromLocationA)
    return distances


# time - O(N^2)
def readDistances():
    distanceFile = open('Data/distances.txt')
    try:
        strings = distanceFile.readlines()
    finally:
        distanceFile.close()
    distanceLists = []
    for i in range(len(strings)):
        distanceLists.append(strings[i].split(','))
    return distanceLists


# time - O(N^2)
def readLocations():
    locationFile = open('Data/locations.txt')
    try:
        strings = locationFile.readlines()
    finally:
        locationFile.close()
    locationLists = []
    for i in range(len(strings)):
        locationLists.append(strings[i].split(','))
    return locationLists


# time - O(N^2)
def readPackages():
    # opens the data file
    packageFile = open('Data/packages.txt')
    try:
        # tries to read each line
        # returns a list of lines to the strings list
        strings = packageFile.readlines()
    finally:
        # closes the data file
        packageFile.close()
    # initializes a list for packages to append to
    packages = []
    # loops through each line in strings list
    for i in range(len(strings)):
        # split function returns a list of every value split by a ',' for that string
        # split list is appended to i'th element in the packages list
        packages.append(strings[i].split(','))
    # returns the list of package information
    return packages
