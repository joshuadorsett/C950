from DataStructures.HashTable import *

class Truck:
    def __init__(self, truckId):
        self.truckId = truckId
        self.maxCargo = 16
        self.speed = 18
        self.cargoSize = 0
        self.packages = HashTable(16)

    def addCargo(self, packageId, weight):
        if self.cargoSize < self.maxCargo:
            self.packages.insert(packageId, weight)
            self.cargoSize += 1
        else:
            print("cargo is full.")

    def removeCargo(self, packageId):
        self.packages.delete(packageId)



