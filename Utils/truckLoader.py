from Models.Truck import Truck
from Utils.dataHandler import makeHashTableOfPackages


def truckLoader():
    # trucks loaded manually based on priority and special notes
    packages = makeHashTableOfPackages()

    truckOne = Truck(1, '8:00')
    # 12 packages in truck 1
    truckOneCargo = [13, 14, 15, 33, 20, 22, 10, 9, 11, 16, 18, 19]
    for i in range(len(truckOneCargo)):
        package = packages.getValue(truckOneCargo[i])
        truckOne.addCargo(package)
        package.setTruck(truckOne)

    truckTwo = Truck(2, '8:00')
    # 16 packages loaded in truck 2
    truckTwoCargo = [35, 36, 37, 4, 2, 17, 29, 12, 38, 39, 26, 34, 3, 7, 28, 6]
    for i in range(len(truckTwoCargo)):
        package = packages.getValue(truckTwoCargo[i])
        truckTwo.addCargo(package)
        package.setTruck(truckTwo)

    truckThree = Truck(3, '9:05')
    # 12 packages in truck 3
    truckThreeCargo = [24, 25, 27, 31, 5, 30, 8, 32, 1, 23, 21, 0]

    for i in range(len(truckThreeCargo)):
        package = packages.getValue(truckThreeCargo[i])
        truckThree.addCargo(package)
        package.setTruck(truckThree)

    trucks = [truckOne, truckTwo, truckThree]

    return trucks
