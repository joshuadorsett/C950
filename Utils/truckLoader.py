from Models.Truck import Truck


def truckLoader(packages):
    highPriorityTruck = Truck(1)

    # trucks loaded manually based on priority and special notes
    highPriorityTruck.addCargo(packages.getValue(14))
    highPriorityTruck.addCargo(packages.getValue(13))
    highPriorityTruck.addCargo(packages.getValue(15))
    highPriorityTruck.addCargo(packages.getValue(19))
    highPriorityTruck.addCargo(packages.getValue(0))
    highPriorityTruck.addCargo(packages.getValue(3))
    highPriorityTruck.addCargo(packages.getValue(6))
    highPriorityTruck.addCargo(packages.getValue(8))
    highPriorityTruck.addCargo(packages.getValue(10))
    highPriorityTruck.addCargo(packages.getValue(16))
    highPriorityTruck.addCargo(packages.getValue(20))
    highPriorityTruck.addCargo(packages.getValue(23))
    highPriorityTruck.addCargo(packages.getValue(25))
    highPriorityTruck.addCargo(packages.getValue(28))
    highPriorityTruck.addCargo(packages.getValue(29))

    mediumPriorityTruck = Truck(2)

    mediumPriorityTruck.addCargo(packages.getValue(37))
    mediumPriorityTruck.addCargo(packages.getValue(35))
    mediumPriorityTruck.addCargo(packages.getValue(17))
    mediumPriorityTruck.addCargo(packages.getValue(2))
    mediumPriorityTruck.addCargo(packages.getValue(1))
    mediumPriorityTruck.addCargo(packages.getValue(4))
    mediumPriorityTruck.addCargo(packages.getValue(7))
    mediumPriorityTruck.addCargo(packages.getValue(9))
    mediumPriorityTruck.addCargo(packages.getValue(11))
    mediumPriorityTruck.addCargo(packages.getValue(12))
    mediumPriorityTruck.addCargo(packages.getValue(18))
    mediumPriorityTruck.addCargo(packages.getValue(21))
    mediumPriorityTruck.addCargo(packages.getValue(22))
    mediumPriorityTruck.addCargo(packages.getValue(26))
    mediumPriorityTruck.addCargo(packages.getValue(30))

    lowPriorityTruck = Truck(3)

    lowPriorityTruck.addCargo(packages.getValue(31))
    lowPriorityTruck.addCargo(packages.getValue(27))
    lowPriorityTruck.addCargo(packages.getValue(24))
    lowPriorityTruck.addCargo(packages.getValue(5))
    lowPriorityTruck.addCargo(packages.getValue(32))
    lowPriorityTruck.addCargo(packages.getValue(33))
    lowPriorityTruck.addCargo(packages.getValue(34))
    lowPriorityTruck.addCargo(packages.getValue(36))
    lowPriorityTruck.addCargo(packages.getValue(38))
    lowPriorityTruck.addCargo(packages.getValue(39))

    trucks = [highPriorityTruck, mediumPriorityTruck, lowPriorityTruck]

    return trucks
