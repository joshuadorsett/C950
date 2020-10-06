def importAllData():
    print (importDistances())
    print (importLocations())
    print (importPackages())

def importDistances():
    distanceFile = open('Data/distances.txt')
    try:
        strings = distanceFile.readlines()
    finally:
        distanceFile.close()
    distances = []
    for i in range(len(strings)):
        distances.append(strings[i].split(','))
    for i in range(len(distances)):
        for j in range(len(distances[0])):
            distances[i][j] = float(distances[i][j])
    return distances

def importLocations():
    locationFile = open('Data/locations.txt')
    try:
        strings = locationFile.readlines()
    finally:
        locationFile.close()
    locations = []
    for i in range(len(strings)):
        locations.append(strings[i].split(','))
    for i in range(len(locations)):
        for j in range(len(locations[0])):
            locations[i][0] = int(locations[i][0])
            locations[i][3] = int(locations[i][3])
    return locations

def importPackages():
    packageFile = open('Data/packages.txt')
    try:
        strings = packageFile.readlines()
    finally:
        packageFile.close()
    packages = []
    for i in range(len(strings)):
        packages.append(strings[i].split(','))
    for i in range(len(packages)):
        for j in range(len(packages[0])):
            packages[i][0] = int(packages[i][0])
            packages[i][4] = int(packages[i][4])
            packages[i][6] = int(packages[i][6])
    return packages
