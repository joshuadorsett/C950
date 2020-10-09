from Models.Truck import Truck


def truckLoader(packages):
    # trucks loaded manually based on priority and special notes

    truckOne = Truck(1, '8:00')
    truckOneCargo = [13, 14, 15, 33, 19, 20, 0, 22, 10, 9, 11, 16, 18]
    for i in range(len(truckOneCargo)):
        package = packages.getValue(truckOneCargo[i])
        truckOne.addCargo(package)
        package.setTruck(truckOne)

    truckTwo = Truck(2, '8:00')
    truckTwoCargo = [35, 36, 37, 4, 2, 17, 29, 12, 38, 39, 26, 34, 3, 7, 28, 6]
    for i in range(len(truckTwoCargo)):
        package = packages.getValue(truckTwoCargo[i])
        truckTwo.addCargo(package)
        package.setTruck(truckTwo)

    truckThree = Truck(3, '9:05')
    packages.getValue(8).setAddress = '410 S State St.'
    truckThreeCargo = [24, 25, 27, 31, 5, 30, 8, 32, 1, 23, 11, 21]

    for i in range(len(truckThreeCargo)):
        package = packages.getValue(truckThreeCargo[i])
        truckThree.addCargo(package)
        package.setTruck(truckThree)

    trucks = [truckOne, truckTwo, truckThree]

    return trucks
