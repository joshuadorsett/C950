from Models.Truck import Truck
from Utils.dataHandler import makeHashTableOfPackages


# trucks loaded manually based on priority, cities/zip, matching addresses, and special notes
def truckLoader():
    # reads data and creates hashtable of 40 package objects
    packages = makeHashTableOfPackages()
    # creates truck object 1 set to leave Hub at 8:00
    truckOne = Truck(1, '8:00')
    # 12 packages in a list for truck 1
    truckOneCargo = [13, 14, 15, 33, 20, 22, 10, 9, 11, 16, 18, 19]
    # loops through list and adds each one to trucks cargo
    for i in range(len(truckOneCargo)):
        package = packages.getValue(truckOneCargo[i])
        truckOne.addCargo(package)
        # sets package attribute truck to the truck 1 object
        package.setTruck(truckOne)
    # creates truck object 2 set to leave Hub at 8:00
    truckTwo = Truck(2, '8:00')
    # 16 packages in a list for truck 2
    truckTwoCargo = [35, 36, 37, 4, 2, 17, 29, 12, 38, 39, 26, 34, 3, 7, 28, 6]
    # loops through list and adds each one to trucks cargo
    for i in range(len(truckTwoCargo)):
        package = packages.getValue(truckTwoCargo[i])
        truckTwo.addCargo(package)
        # sets package attribute truck to the truck 2 object
        package.setTruck(truckTwo)
    # creates truck object 3 set to leave Hub at 9:05 to wait for packages arriving late to hub
    truckThree = Truck(3, '9:05')
    # 12 packages in a list for truck 3
    truckThreeCargo = [24, 25, 27, 31, 5, 30, 8, 32, 1, 23, 21, 0]
    # loops through list and adds each one to trucks cargo
    for i in range(len(truckThreeCargo)):
        package = packages.getValue(truckThreeCargo[i])
        truckThree.addCargo(package)
        # sets package attribute truck to the truck 3 object
        package.setTruck(truckThree)
    # puts truck objects into a single list
    trucks = [truckOne, truckTwo, truckThree]
    # returns list of trucks
    return trucks
