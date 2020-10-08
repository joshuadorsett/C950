from Models.Truck import Truck


def truckLoader(packages):
    # trucks loaded manually based on priority and special notes

    truckOne = Truck(1, '8:30')
    truckOneCargo = [packages.getValue(14), packages.getValue(13), packages.getValue(15),
                     packages.getValue(19), packages.getValue(0), packages.getValue(3),
                     packages.getValue(6), packages.getValue(8), packages.getValue(10),
                     packages.getValue(16), packages.getValue(20), packages.getValue(23),
                     packages.getValue(25), packages.getValue(28), packages.getValue(29)]
    for i in range(len(truckOneCargo)):
        package = truckOneCargo[i]
        truckOne.addCargo(package)
        package.setTruck(truckOne)

    truckTwo = Truck(2, '8:30')
    truckTwoCargo = [packages.getValue(37), packages.getValue(35), packages.getValue(17),
                     packages.getValue(2), packages.getValue(1), packages.getValue(4),
                     packages.getValue(7), packages.getValue(9), packages.getValue(11),
                     packages.getValue(12), packages.getValue(18), packages.getValue(21),
                     packages.getValue(22), packages.getValue(26), packages.getValue(30)]
    for i in range(len(truckTwoCargo)):
        package = truckTwoCargo[i]
        truckTwo.addCargo(package)
        package.setTruck(truckTwo)

    truckThree = Truck(3, '9:05')
    truckThreeCargo = [packages.getValue(31), packages.getValue(27), packages.getValue(24),
                       packages.getValue(5), packages.getValue(32), packages.getValue(33),
                       packages.getValue(34), packages.getValue(36), packages.getValue(38),
                       packages.getValue(39)]
    for i in range(len(truckThreeCargo)):
        package = truckThreeCargo[i]
        truckThree.addCargo(package)
        package.setTruck(truckThree)

    trucks = [truckOne, truckTwo, truckThree]

    return trucks
