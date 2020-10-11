from DataStructures.HashTable import *
from Models.Location import *
from Models.Package import *
# a group of static functions related to handling data files


# returns a hash table of package objects
# time - O(N)
def makeHashTableOfPackages():
    # sets variable to list returned from the read function
    packageLists = readPackages()
    # sets variable to a new Hash Table object
    packages = HashTable(len(packageLists))
    # loops through package list
    for i in range(len(packageLists)):
        # converts the iteration's package index string to an int for index searching
        packageLists[i][0] = int(packageLists[i][0])
        # sets variable to current list of package info
        current = packageLists[i]
        # creates a package object with arguments from the package information from list
        p = Package(current[0], current[1], current[2], current[4], current[5], current[6], current[7])
        # insert package object into hash table
        packages.insert(current[0], p)
    # returns the hash table
    return packages


# returns a hash table of location objects
# time - O(N)
def makeHashTableOfLocations():
    # sets variable to list returned from the read function
    locationLists = readLocations()
    # sets variable to a new Hash Table object
    locations = HashTable(len(locationLists))
    # loops through location list
    for i in range(len(locationLists)):
        # converts the iteration's locatin index string to an int for index searching
        locationLists[i][0] = int(locationLists[i][0])
        # sets variable to current list of location info
        current = locationLists[i]
        # creates a location object with arguments from the location information from list
        l = Location(current[0], current[1], current[2], current[3])
        # insert location object into hash table
        locations.insert(l.getIndex(), l)
    # returns the hash table
    return locations


# returns a hash table with the key being LocationA and the key is a list of distances to any LocationB
# by using the getIndex method in the Location class we can access any distance once this list is created
# time - O(N)
def makeHashTableOfDistances():
    # sets variable to list returned from the read function
    distanceLists = readDistances()
    # sets variable to a new Hash Table object
    distances = HashTable(len(distanceLists))
    # loops through distance list
    for i in range(len(distanceLists)):
        # sets variable to current list of distances
        ListOfDistancesFromLocationA = distanceLists[i]
        # insert current list of distances into hash table with current index
        distances.insert(i, ListOfDistancesFromLocationA)
    # returns the hash table
    return distances


# time - O(N^2)
def readDistances():
    # opens the data file
    distanceFile = open('Data/distances.txt')
    try:
        # tries to read each line
        # returns a list of lines to the strings list
        strings = distanceFile.readlines()
    finally:
        # closes the data file
        distanceFile.close()
    # initializes a list for distance lists to append to
    distanceLists = []
    # loops through each line in strings list
    for i in range(len(strings)):
        # split function returns a list of every value split by a ',' for that string
        # split list is appended to i'th element in the distance list
        distanceLists.append(strings[i].split(','))
    # returns the list of distances lists
    return distanceLists


# time - O(N^2)
def readLocations():
    # opens the data file
    locationFile = open('Data/locations.txt')
    try:
        # tries to read each line
        # returns a list of lines to the strings list
        strings = locationFile.readlines()
    finally:
        # closes the data file
        locationFile.close()
    # initializes a list for locations to append to
    locationLists = []
    # loops through each line in strings list
    for i in range(len(strings)):
        # split function returns a list of every value split by a ',' for that string
        # split list is appended to i'th element in the location list
        locationLists.append(strings[i].split(','))
    # returns the list of location information
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
